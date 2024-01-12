---

# README para o Módulo iLEAPP: `callFrequent.py` & 'callFrequent_aleapp.py'

Este documento fornece informações essenciais sobre o módulo `callFrequent.py`, desenvolvido para o iLEAPP, ALEAPP, vLEAPP (iOS/Android/Vehicle Logs, Events, And Plists Parser). Este módulo é uma adição personalizada ao projeto, destinada a enriquecer as capacidades de análise forense de dispositivos móveis.

## Descrição Geral do Módulo

O módulo `callFrequent.py` foi criado para identificar e analisar as chamadas mais frequentes realizadas e recebidas em dispositivos móveis. Ele extrai informações relevantes do histórico de chamadas, destacando os números de telefone mais discados e recebidos.

### Funcionalidades Principais

- Extração dos números de telefone mais frequentemente discados e recebidos.
- Análise de arquivos `.storedata` relacionados ao histórico de chamadas.
- Geração de relatórios detalhados em formato HTML e TSV.

### Requisitos

- iLEAPP, ALEAPP, vLEAPP instalado e configurado.
- Não há requisitos adicionais específicos para este módulo.

## Estrutura do Código

O script utiliza as bibliotecas e funções padrão do iLEAPP, ALEAPP, vLEAPP para realizar a leitura e análise dos dados:

## Uso do Módulo

Para utilizar o módulo `callFrequent.py` ou `callFrequent_aleapp.py`:

1. Coloque o script no diretório `scripts/artifacts` do projeto iLEAPP.
2. Execute o iLEAPP, ALEAPP, vLEAPP e selecione o módulo `callFrequent` durante a análise.
3. Revise os relatórios gerados para insights sobre as chamadas frequentes.

## Contribuições e Feedback

Este módulo foi desenvolvido por Nelson Brilhante & Rúben Mendes. Estamos abertos a contribuições e feedback para melhorar continuamente a funcionalidade do módulo. Sinta-se à vontade para abrir issues ou pull requests no repositório do projeto.

## Licença

Este módulo segue a mesma licença do projeto iLEAPP, ALEAPP, vLEAPP. Consulte a documentação do iLEAPP, ALEAPP, vLEAPP para mais detalhes sobre a licença.
