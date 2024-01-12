import os
import shutil

extensao = ""
        
def criar_arquivo_txt(nome): 
    if os.path.exists(nome + extensao):
        with open(nome + extensao, "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        with open(nome + extensao, "w", encoding="utf-8") as arq:
            conteudo = input('Fale o que quiser: ')
            arq.write(conteudo + " ")
        return False
    

def abrir_arquivo_txt(nome):
    if os.path.exists(nome + extensao):    
        with open(nome + extensao, "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        return False
        

def escrever_arquivo_txt(nome):
    if os.path.exists(nome + extensao):
        with open(nome + extensao, "a", encoding="utf-8") as arq:
            conteudo = input('Fale o que quiser a mais: ')
            arq.write(conteudo + " ")
        return True
    else:
        return False
  

def listar_diretorio(diretorio, extensao):
    #raiz - dirs - arquivos
    for _ , _ , arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                print(os.path.join(arquivo))

def diretorio_atual():
    return os.getcwd()

def criar_diretorio(nome_dir):
    os.mkdir(diretorio_atual()+'./'+nome_dir)

def copiar_diretorio_completo(src, dst):
    try:
        for raiz, dirs, arquivos in os.walk(src):
            for arquivo in arquivos:
                src_arquivo = os.path.join(raiz, arquivo)
                dst_arquivo = os.path.join(dst, arquivo)
                shutil.copy2(src_arquivo, dst_arquivo)
        return True
    except Exception as e:
        print(f"Error during file copy: {e}")
        return False


def mover_diretorio_completo(src, dst):
    lista = os.listdir(src)
    qtnd_arq = len(lista)
    aux = 0
    try:
        if os.path.isdir(dst):
            while aux < qtnd_arq:
                antigo = os.path.join(src, lista[aux])
                novo = os.path.join(dst, lista[aux])
                if os.path.exists(antigo):  
                    shutil.move(antigo, novo)
                else:
                    print(f"Arquivo nao existe: {antigo}")
                aux += 1
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao mover arquivo: {e}")
        return False

def deletar_arquivo(nome_arquivo):
    try:
        os.remove(nome_arquivo)
        print(f"O arquivo '{nome_arquivo}' foi removido com sucesso.")
        return True
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao tentar remover o arquivo '{nome_arquivo}': {e}")
        return False

def deletar_diretorio(nome_diretorio):
    try:
        shutil.rmtree(nome_diretorio)
        print(f"O diretório '{nome_diretorio}' foi removido com sucesso.")
        return True
    except FileNotFoundError:
        print(f"O diretório '{nome_diretorio}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao tentar remover o diretório '{nome_diretorio}': {e}")
        return False
    
# Example usage:

diretorio = diretorio_atual()


deletar_diretorio('teste')
# deletar_arquivo('teste.txt')

# if copiar_diretorio_completo(diretorio, r'C:\Users\nyddo\OneDrive\Área de Trabalho\Faculdade\POOII\teste') is True:
#     print('Arquivos copiados com sucesso!')
# else:
#     print('Arquivos nao copiados!')


# if mover_diretorio_completo(diretorio, r'C:\Users\nyddo\OneDrive\Área de Trabalho\Faculdade\POOII\teste') is True:
#     print('Arquivos movidos com sucesso!')
# else:
#     print('Arquivos nao movidos!')
    
# print(os.listdir(diretorio_atual()))

#listar_diretorio(diretorio, extensao)


# nome_arquivo = "teste" 


# if abrir_arquivo_txt(nome_arquivo) is True:
#     escrever_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo) 
# else:
#     criar_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo)



