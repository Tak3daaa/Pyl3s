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

def copiar_diretorio_completo(src, dst): #arrumar
    shutil.copytree(src, dst)

diretorio = diretorio_atual()

# print(os.listdir(diretorio_atual()))

listar_diretorio(diretorio, extensao)


# nome_arquivo = "teste" 


# if abrir_arquivo_txt(nome_arquivo) is True:
#     escrever_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo) 
# else:
#     criar_arquivo_txt(nome_arquivo)
#     abrir_arquivo_txt(nome_arquivo)



