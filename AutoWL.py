print('AutoWL V1.0 ~ A1v4n0v (2023)')
print('Esse Programa vai gerar uma WordList com todas as palavras encontradas no site informado ')



import requests
from bs4 import BeautifulSoup
import re

def criar_wordlist(url):
    try:
        # Faz uma solicitação HTTP para obter o conteúdo do site
        response = requests.get(url)
        
        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Analisa o conteúdo HTML da página
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontra todas as palavras no conteúdo HTML usando uma expressão regular
            palavras = re.findall(r'\b\w+\b', soup.get_text())
            
            # Remove palavras duplicadas
            palavras_unicas = set(palavras)
            
            return list(palavras_unicas)
        else:
            print("Falha ao acessar o site. Código de status:", response.status_code)
    except Exception as e:
        print("Erro:", str(e))
    
    return []

if __name__ == "__main__":
    url = input("Digite a URL do site com HTTP ou HTTPS para criar a Wordlist:  ")
    
    wordlist = criar_wordlist(url)
    
    if wordlist:
        nome_arquivo = input("Digite o nome e o formato do arquivo para salvar a Wordlist: ")
        
        with open(nome_arquivo, "w") as arquivo:
            for palavra in wordlist:
                arquivo.write(palavra + "\n")
        
        print("Wordlist salva com sucesso!")
    else:
        print("Nenhuma palavra foi encontrada no site.")
