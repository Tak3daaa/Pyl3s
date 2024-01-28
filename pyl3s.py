import os
import shutil
from fpdf import FPDF
# import chardet
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

extensao = ".txt"
        
def criar_arquivo_txt(nome): 
    if os.path.exists(nome + extensao):
        with open(nome + extensao, "r", encoding="utf-8") as arq:
            arquivo = arq.read()
            print(arquivo)
        return True
    else:
        with open(nome + extensao, "w", encoding="utf-8") as arq:
            conteudo = input('-> ')
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
            conteudo = input('-> ')
            arq.write(conteudo + " ")
        return True
    else:
        return False
  

def listar_diretorio(diretorio, extensao):
    #raiz - dirs - arquivos
    for raiz , _ , arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                print(os.path.join(raiz, arquivo))

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
    
def tamanho_diretorio_kb(caminho):
    total = 0
    # total_arq = 0
    # total_dir = 0
    for caminho_atual, sub_dir, arquivos in os.walk(caminho):
        for a in arquivos:
            aux = os.path.join(caminho_atual, a)
            total += os.path.getsize(aux)
            # total_arq = total_arq + 1
        for sub in sub_dir:
            aux_2 = os.path.join(caminho_atual, sub)
            # total_dir = 1 + total_dir 
            total += tamanho_diretorio_kb(aux_2)
            
    return total/1024

def tamanho_arquivo_kb(caminho, nome_arq):
    return os.path.getsize(caminho + '\\' + nome_arq)

# def palavra_chave(arquivo, palavra):
#     with open(arquivo, 'r', encoding='utf-8') as file:
#         for numero_linha, linha in enumerate(file, 1):
#             if palavra in linha:
#                 return numero_linha, palavra
def palavra_chave(arquivo, palavra):
    ocorrencias = []

    with open(arquivo, 'r', encoding='utf-8') as file:
        for numero_linha, linha in enumerate(file, 1):
            if palavra in linha:
                ocorrencias.append((numero_linha, linha.strip()))

    return ocorrencias

def contar_caracteres(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        quantidade_caracteres = len(conteudo)
    
    return quantidade_caracteres


def txt_pdf(arquivo):
    pdf = FPDF()
    pdf.add_page()
    file = open(arquivo, 'r')
    for texto in file:
        if len(texto) <= 20:
            pdf.set_font("Arial", "B", size=18)
            pdf.cell(w=200,h=10,txt=texto,ln=1,align='C')
        else:
            pdf.set_font("Arial", size=15)
            pdf.cell(w=0,h=10,txt=texto,align='L')
    pdf.output('saida.pdf')
    
txt_pdf('teste2.txt')
# diretorio = diretorio_atual()
# print(contar_caracteres('teste3.txt'))
# print(tamanho_diretorio_kb(diretorio_atual()))
# print(tamanho_arquivo_kb(diretorio_atual(), 'teste2.txt'))
# deletar_diretorio('teste')
# deletar_arquivo('teste.txt')
# palavra = palavra_chave('teste2.txt', 'amor')
# palavra = palavra_chave('teste2.txt', 'amor')
# print(palavra)

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



