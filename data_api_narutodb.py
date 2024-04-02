import requests
import pandas as pd

# Solicita ao usuário que digite o clã desejado
cla = input("Digite o nome do clã desejado: ")

# Faz a solicitação à API
response = requests.get(f'https://narutodb.xyz/api/clan/search?name={cla}')

# Verifica se a response foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print("Resposta bem sucedida!")
    print(f"Status: {response.status_code}")
    print("-----------------------------------------\n")
    
    # Obtém a lista de personagens
    characters = data.get('characters', [])
    # Cria uma lista para armazenar os jutsus de cada personagem
    jutsus_list = []
    # Cria uma lista para armazenar o "natureType" de cada personagem
    nature_type_list = []
    
    # Extrai os jutsus e natureType de cada personagem e os armazena nas listas
    for character in characters:
        jutsus = "; ".join(character.get('jutsu', []))
        jutsus_list.append(jutsus)
        
        nature_type = "; ".join(character.get('natureType', []))
        nature_type_list.append(nature_type)
    
    # Cria um DataFrame do pandas para armazenar os dados
    df = pd.DataFrame(characters)
    
    # Adiciona as colunas 'jutsu' e 'natureType' ao DataFrame
    df['jutsu'] = jutsus_list
    df['natureType'] = nature_type_list
    
    # Seleciona apenas as colunas desejadas
    df = df[['id', 'name', 'jutsu', 'natureType']]
    
    # Exibe o DataFrame
    print(df, "\n")
    
    # Salva o DataFrame em um arquivo Excel
    df.to_excel(f'personagens_cla_{cla}.xlsx', index=False)
    
    print("Planilha criada com sucesso!")
else:
    print("Falha ao obter os dados da API")
    print(f"Status: {response.status_code}")
