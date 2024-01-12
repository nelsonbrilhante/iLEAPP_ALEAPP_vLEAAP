# scripts/artifacts/callFrequent.py

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, open_sqlite_db_readonly

__artifacts_v2__ = {
    "callfrequent": {
        "name": "Frequent Call Numbers",
        "description": "Shows the most dialed and most received call numbers",
        "author": "Nelson Brilhante & Rúben Mendes",
        "version": "0.1",
        "date": "2024-01-12",
        "requirements": "none",
        "category": "Call History",
        "notes": "Updated to include in/out column.",
        "paths": ('**/CallHistory.storedata*',),
        "function": "get_callFrequent"
    }
}

def get_callFrequent(files_found, report_folder, seeker, wrap_text, time_offset):
    logfunc("If you can read this its working.")

    # Initialize the variables to None for the most dialed and received numbers
    most_dialed = None
    most_received = None

    for file_found in files_found:
        logfunc(f'Found file: {file_found}')
        file_found = str(file_found)
        if file_found.endswith('.storedata'):
            db = open_sqlite_db_readonly(file_found)
            cursor = db.cursor()
            cursor.execute('''
            select ZADDRESS, CASE ZORIGINATED WHEN 1 then 'Outgoing' ELSE 'Incoming' END
            from ZCALLRECORD
            ''')

            all_rows = cursor.fetchall()
            db.close()

            if not all_rows:
                logfunc('No Call History data available')
                return

            # Count the frequency of each contact number
            dialed = {}
            received = {}
            for row in all_rows:
                number, direction = row
                if direction == 'Outgoing':
                    dialed[number] = dialed.get(number, 0) + 1
                else:
                    received[number] = received.get(number, 0) + 1

            # Find the most frequent contact numbers
            most_dialed = max(dialed, key=dialed.get, default='None')
            most_received = max(received, key=received.get, default='None')
            break

    # Make sure we have found a .storedata file and processed it
    if most_dialed is None or most_received is None:
        logfunc('No .storedata file found or no call records processed.')
        return

    # Prepare the list for the report
    data_list = [
        ("Out", most_dialed, dialed.get(most_dialed, 'None')),
        ("In", most_received, received.get(most_received, 'None'))
    ]

    # Create the report
    report = ArtifactHtmlReport('Frequent Call Numbers')
    report.start_artifact_report(report_folder, 'Frequent Call Numbers')
    report.add_script()
    data_headers = ('in/out', 'Phone Number', 'Frequency')
    report.write_artifact_data_table(data_headers, data_list, file_found)
    report.end_artifact_report()

    # Write a TSV report as well - framework requirement
    tsvname = 'Frequent Call Numbers'
    tsv(report_folder, data_headers, data_list, tsvname)

# Standalone version
if __name__ == '__main__':
    pass
