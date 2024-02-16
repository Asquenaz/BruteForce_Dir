#Utilize  python 3 para rodar o script
#Certifique-se de que a wordlist a ser usada está na mesma pasta do projeto.

#Lembre-se : 
      #Com grandes poderes, vem sempre grandes responsabilidades.
      #Contríbua com o mundo da cibersegurança.

#Ass: Asquen@az 


import requests
import sys 


#Lista de diretórios que serão testadas
#URLs válidas
path_saida = r"/home/kali/Documents/Scripts/BruteForce/200.txt"

#Urls inválidas
path_URL_testadas = r"/home/kali/Documents/Scripts/BruteForce/urls_testadas.txt"


def save_output(path_saida, site, mensagem = None):
    with open (path_saida, 'a') as saida:
        saida.write(f"{mensagem} {site}\n")
        saida.close()


def find_dir(URL, path_entrada):

    with open (path_entrada, 'r') as wordlist:
        for diretorio in wordlist :
            diretorio = diretorio.strip()
            site = f"http://{URL}/{diretorio}"

            try:
                response = requests.get(site)
                print(f'Testando: {site} (CODE: {response.status_code})', end='\r')

                if response.status_code == 200 :
                    save_output(path_saida, site, mensagem="URL válida: ")
                if response.status_code <=399 and response.status_code >= 599 :
                    save_output (path_URL_testadas, site, mensagem="Urls que não retornaram erro de sevidor ou usuário : " )

            except ConnectionError as ce:
                print(f"Erro de conexão: {ce}")
            except KeyboardInterrupt as e:
                sys.exit(0)
                print(f"Erro: {e}")

    print('Busca finalizada, para mais detalhes, abra o arquivo 200.txt')

if __name__ == '__main__':
    url = sys.argv[1]
    wordlist = sys.argv[2]

    if len(sys.argv) != 3:
        print('Número de argumentos inválidos. Tente: python3 script.py exemplo.com wordlist.txt')
    else:
        find_dir(url, wordlist)
