#Authors: Nelson Brilhante & Rúben Mendes

from collections import Counter
import sqlite3

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, open_sqlite_db_readonly

def get_callFrequent(files_found, report_folder, seeker, wrap_text):
    
    file_found = str(files_found[0])
    db = open_sqlite_db_readonly(file_found)
    cursor = db.cursor()
    cursor.execute('''
    SELECT
    datetime(date /1000, 'unixepoch') as date,
    CASE
        WHEN phone_account_address is NULL THEN ' '
        ELSE phone_account_address
        end as phone_account_address,
    number,
    CASE
        WHEN type = 1 THEN  'Incoming'
        WHEN type = 2 THEN  'Outgoing'
        WHEN type = 3 THEN  'Missed'
        WHEN type = 4 THEN  'Voicemail'
        WHEN type = 5 THEN  'Rejected'
        WHEN type = 6 THEN  'Blocked'
        WHEN type = 7 THEN  'Answered Externally'
        ELSE 'Unknown'
        end as types,
    duration,
    CASE
        WHEN geocoded_location is NULL THEN ' '
        ELSE geocoded_location
        end as geocoded_location,
    countryiso,
    CASE
        WHEN _data is NULL THEN ' '
        ELSE _data
        END as _data,
    CASE
        WHEN mime_type is NULL THEN ' '
        ELSE mime_type
        END as mime_type,
    CASE
        WHEN transcription is NULL THEN ' '
        ELSE transcription
        END as transcription,
    deleted
    FROM
    calls
    ''')

    all_rows = cursor.fetchall()
    usageentries = len(all_rows)
    
    if usageentries > 0:
        report = ArtifactHtmlReport('Call Frequent')
        report.start_artifact_report(report_folder, 'Call Frequent')
        report.add_script()
        data_headers = ('Most Called Number','Number of times')
        data_list = []
        phone_number_counter = Counter()  #Counter to track the count of each phone number

        for row in all_rows:
            #Increment the count for each phone number
            phone_number_counter[row[2]] += 1

        #Find the most called number
        most_called_number, count = phone_number_counter.most_common(1)[0]

        #Write data in log reports
        logfunc(f'Most Called Number: {most_called_number}, Count: {count}')

        #Create table with data collected
        data_list.append((most_called_number,count))

        #Write data in HTML report
        report.write_artifact_data_table(data_headers, data_list, file_found, html_escape=False)
        report.end_artifact_report()
        
        tsvname = f'Call Frequent'
        tsv(report_folder, data_headers, data_list, tsvname)

        tlactivity = 'Call Frequent'
        timeline(report_folder, tlactivity, data_list, data_headers)

        

    else:
        logfunc('No Call Log data available')
    
    db.close()