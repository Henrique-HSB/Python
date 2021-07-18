import requests as r #importa a biblioteca requests e dá um apelido de r

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)

resp.status_code #teste de acesso a pagina #resposta 200 teste ok, se 400 erro (pagina não encontrada)

raw_data = resp.json() #coleta os dados da pagina

raw_data[0] # imprimi a primeira linha (linha [0]) dos dados contidos na lista em raw_data
#####RESPOSTA########
'''
{'ID': '63aa488e-b4a2-4fcd-ae15-07c1ff219903',
 'Country': 'Brazil',
 'CountryCode': 'BR',
 'Province': '',
 'City': '',
 'CityCode': '',
 'Lat': '-14.24',
 'Lon': '-51.93',
 'Confirmed': 1,
 'Deaths': 0,
 'Recovered': 0,
 'Active': 1,
 'Date': '2020-02-26T00:00:00Z'}
 '''

final_data = [] # a lista final_data recebe somente os dados das variaves sitadas
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'],obs ['Date']]) 
    
final_data.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
final_data
#####RESPOSTA########
 ''' 
[['confirmados', 'obitos', 'recuperados', 'ativos', 'data'],
 [1, 0, 0, 1, '2020-02-26T00:00:00Z'],
 [1, 0, 0, 1, '2020-02-27T00:00:00Z'],
 [1, 0, 0, 1, '2020-02-28T00:00:00Z'],
 [2, 0, 0, 2, '2020-02-29T00:00:00Z'],
 [2, 0, 0, 2, '2020-03-01T00:00:00Z'],
 [2, 0, 0, 2, '2020-03-02T00:00:00Z'],
 [2, 0, 0, 2, '2020-03-03T00:00:00Z'],
 [4, 0, 0, 4, '2020-03-04T00:00:00Z'],
 [4, 0, 0, 4, '2020-03-05T00:00:00Z'],
 ...
'''
#valores para referenciar as variaveis
CONFIRMADOS = 0
OBITOS = 1 
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10] #formatando ao campo data, para facilitar visualização
    
final_data
#####RESPOSTA########
'''
[['confirmados', 'obitos', 'recuperados', 'ativos', 'data'],
 [1, 0, 0, 1, '2020-02-26'],
 [1, 0, 0, 1, '2020-02-27'],
 [1, 0, 0, 1, '2020-02-28'],
 [2, 0, 0, 2, '2020-02-29'],
 [2, 0, 0, 2, '2020-03-01'],
 [2, 0, 0, 2, '2020-03-02'],
 [2, 0, 0, 2, '2020-03-03'],
 [4, 0, 0, 4, '2020-03-04'],
 [4, 0, 0, 4, '2020-03-05'],
 ...
 '''
import datetime as dt # importa a biblioteca datetime e dá o apelido de 'dt'

########### EXEMPLO DE CRIAÇÃO DE OBJETO DE TEMPO ##############
print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo.microsegundo')
print('-------------')
print(dt.date(2020 , 4, 25), 'Ano-mês-dia')
print('-------------')
print(dt.datetime(2020 , 4, 25, 12, 6, 21, 7), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')
#####RESPOSTA########
'''
12:06:21.000007 Hora:minuto:segundo.microsegundo
-------------
2020-04-25 Ano-mês-dia
-------------
2020-04-25 12:06:21.000007 Ano-mês-dia Hora:minuto:segundo.microsegundo
'''


import csv # importa a biblioteca CSV
with open ('brasil-covid.csv', 'w') as file: #abre um aquivo chamado brasil-covid no formato csv com a opção 'w' de escrita
    writer = csv.writer(file)
    writer.writerows(final_data)
for i in range(1,len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d') # converte a string final_data para tipo data 

final_data
#####RESPOSTA########
'''[['confirmados', 'obitos', 'recuperados', 'ativos', 'data'],
 [1, 0, 0, 1, datetime.datetime(2020, 2, 26, 0, 0)],
 [1, 0, 0, 1, datetime.datetime(2020, 2, 27, 0, 0)],
 [1, 0, 0, 1, datetime.datetime(2020, 2, 28, 0, 0)],
 [2, 0, 0, 2, datetime.datetime(2020, 2, 29, 0, 0)],
 [2, 0, 0, 2, datetime.datetime(2020, 3, 1, 0, 0)],
 [2, 0, 0, 2, datetime.datetime(2020, 3, 2, 0, 0)],
 [2, 0, 0, 2, datetime.datetime(2020, 3, 3, 0, 0)],
 [4, 0, 0, 4, datetime.datetime(2020, 3, 4, 0, 0)],
 [4, 0, 0, 4, datetime.datetime(2020, 3, 5, 0, 0)],
 ...

'''

