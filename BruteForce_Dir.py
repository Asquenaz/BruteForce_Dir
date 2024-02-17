# Utilize  python >=3 para rodar o script

# Certifique-se de que a wordlist a ser usada esta na mesma pasta do projeto.
# Certifique-se de que todos os arquivos estão no formato UTF 8

#Lembre-se : 
      #Com grandes poderes, vem sempre grandes responsabilidades.
      #Contribua com o mundo da ciberseguranca.

import requests
import sys 

#URLs validas
path_saida = r"C:\Users\GuilhermeFernandesLi\OneDrive - Bricon IT Solution\Documentos\Bricon\Scripts\BruteForce_Dir/200.txt"

#Caminho para wordlist padrao
path_word_default = r"C:\Users\GuilhermeFernandesLi\OneDrive - Bricon IT Solution\Documentos\Bricon\Scripts\BruteForce_Dir/small.txt"


path_URL_testadas = r"C:\Users\GuilhermeFernandesLi\OneDrive - Bricon IT Solution\Documentos\Bricon\Scripts\BruteForce_Dir/urls_testadas.txt"
path_URL_Fail = r"C:\Users\GuilhermeFernandesLi\OneDrive - Bricon IT Solution\Documentos\Bricon\Scripts\BruteForce_Dir/fail.txt"


def save_output(path_saida, site, mensagem = None):
    with open (path_saida, 'a', encoding='utf-8') as saida:
        saida.write(f" {site}\n")
        

def status_code (site) :
    response = requests.get(site)
    
    if response.status_code == 200 :
        save_output(path_saida, site)
    elif response.status_code >= 400 and response.status_code <=599 :
        save_output (path_URL_Fail, site)
    else :
        save_output (path_URL_testadas, site)
  
    return response.status_code


def find_dir (URL, list):
    with open (list, 'r', encoding='utf-8') as wordlist:
        for diretorio in wordlist :
            diretorio = diretorio.strip()
            site = f"http://{URL}/{diretorio}"

            try:
                status_code(site)
                print(f'+  {site} (CODE: {status_code(site)}) ', end='\r')

            except ConnectionError as ce:
                print(f"Erro de conexao: {ce}")
            except KeyboardInterrupt as e:
                print(f"Erro: {e}")
                sys.exit(0)
   # next_brute()

def find_subDir (wordlist, wordlist_sub):
    with open(wordlist_sub, "r", encoding='utf-8') as word_sub:
        for site in word_sub:
            site = site.strip()
            
            with open(wordlist, "r", encoding='utf-8') as wordlist_file:
                for url in wordlist_file:
                    url = url.strip()
                    sub_dir = "{}/{}".format(url, site)

                    try:
                         status_code(sub_dir)
                         print(f'+  {sub_dir} (CODE: {status_code(sub_dir)}) ', end='\r')

                    except ConnectionError as ce:
                        print(f"Erro de conexao: {ce}")
                    except KeyboardInterrupt as e:
                        print(f"Erro: {e}")
                        sys.exit(0)
    print('Programa encerrado, seus resultados postivos estao no arquivo 200.txt')
    
def next_brute():
    print('')
    resposta = input(str('Deseja testar subdiretorios : (S/N): ')).lower()
    if resposta == 's' : 
        find_subDir(path_saida, path_word_default )
    else :
        print('Programa encerrado, seus resultados postivos estao no arquivo 200.txt')
        sys.exit(0)

if __name__ == '__main__':
    url = sys.argv[1]
    wordlist = sys.argv[2]

    if len(sys.argv) != 3:
        print('Numero de argumentos invalidos. Tente: python3 script.py exemplo.com wordlist.txt')
    else:
        find_dir (url, wordlist)


#Ass: Asquen@z 
