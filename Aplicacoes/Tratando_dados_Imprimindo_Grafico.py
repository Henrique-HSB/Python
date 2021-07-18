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

def get_datasets(y, labels): #Função para definir os dados
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data':y[i]  
            })
        return datasets
    else:
        return[
            {
                'label': labels[0],
                'data': y
            }
        ]
     
def set_title(title=''): # Função para definir o titulo
    if title != "":
        display= 'true'
    else:
        display = 'false'
    return{
        'title': title,
        'display': display
    }

def creat_chart(x, y, labels, kind='bar', title=''):# Função para definir o grafico
    
    datasets = get_datasets(y, labels)
    options = set_title(title)
    
    chart = { # dicionario representativo dos dados 
        'type': kind,
        'data':{
            'labels': x,
            'datasets': datasets
        },
        'options': options # identificação de eixos
    }

    return chart
   
def get_api_chart(chart):# Função que realiza a requisição da API utilizando o dicionario da finção anterior
    url_base = 'https://quickchart.io/chart' # faz a requisição dos dados
    resp = r.get(f'{url_base}?c={str(chart)}') # Retorna o arquivo da imagem
    return resp.content #armazena o valor em binario

def save_image(path, content): # Comando para salvar a imagem carregada
    with open(path, 'wb') as image:
        image.write(content)

from PIL import Image# importa da biblioteca PIL  a função Imagem
from IPython.display import display# importa da biblioteca IPython.display a função display

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::10]: #pula de 10 em 10 dias a coleta de informações para plotar no grafico
    y_data_1.append(obs[CONFIRMADOS]) # popula a variavel y_data_1 com os dados da da coluna CONFIRMADOS

y_data_2 = []
for obs in final_data[1::10]: #pula de 10 em 10 dias a coleta de informações para plotar no grafico
    y_data_2.append(obs[RECUPERADOS]) # popula a variavel y_data_2 com os dados da da coluna RECUPERADOS

labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]: #pula de 10 em 10 dias a coleta de informações para plotar no grafico
    x.append(obs[DATA].strftime('%d/%m/%Y'))# popula a variavel x com os dados da da coluna DATA
    
chart = creat_chart(x, [y_data_1, y_data_2], labels, title= 'Grafico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png') #Imprime o Grafico


