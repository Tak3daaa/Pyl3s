# libpyles
========================================================

### Atraves desse pacote, o usuário poderá fazer a manipulação de arquivos de maneira mais simples e otimizada, além de poder criar, mover, excluir e copiar diretórios. E mais algumas funções extras de conversão de arquivos de texto.

## Instalação
Para instalar o pacote, basta executar o comando abaixo:
<pre><code>pip install libpyles</code></pre>

## Funções da biblioteca

=======================================================

### def criar_arquivo_txt(nome)<br>
### def abrir_arquivo_txt(nome)<br>
### def escrever_arquivo_txt(nome)<br>
### def criar_arquivo_bin(nome)<br>
### def abrir_arquivo_bin(nome)<br>
### def escrever_arquivo_bin(nome)<br>
### def listar_diretorio(diretorio, extensao)<br>
### def diretorio_atual()<br>
### def criar_diretorio(nome_dir)<br>
### def copiar_diretorio_completo(src, dst)<br>
### def mover_diretorio_completo(src, dst)<br>
### def deletar_arquivo(nome_arquivo)<br>
### def deletar_diretorio(nome_diretorio)<br>
### def tamanho_diretorio_kb(caminho)<br>
### def tamanho_arquivo_kb(caminho, nome_arq)<br>
### def palavra_chave(arquivo, palavra)<br>
### def contar_palavras_mais_frequentes(nome_arquivo)<br>
### def contar_caracteres(arquivo)<br>
### def txt_pdf(arquivo, nome_arquivo)<br>
### def pdf_to_txt(arquivo, arquivo_txt)<br>
### def txt_bin(arquivo, nome_arquivo_bin)<br>
### def bin_to_txt(nome_arquivo_bin, nome_arquivo_txt)<br>

=======================================================

## Importação

<pre><code>import libpyles</code></pre>

=======================================================

## Uso de cada função

=======================================================

>Será utilizado uma abreviação para fácil entendimento. Nesse sentido, será utilizado o __lp__ (import libpyles as lp).

<pre><code>

lp.criar_arquivo_txt(nome) 

""" 
    A variável 'nome' é apenas o nome do arquivo sem a extensão(.txt) e entre aspas simples, por exemplo 'teste'. 
    Saída: É criado um arquivo .txt se ele não existir no diretório atual, caso contrário, ela apenas lê e exibe o arquivo .txt. Além disso é retornado True ou False para ser utilizado dependendo da ocasião do uso. 
    Exemplo:
        if lp.criar_arquivo_txt(nome) is True:
            print('Arquivo criado!!')
        else:
            print('Arquivo já existente!!')
"""

lp.abrir_arquivo_txt(nome)

"""
    A variável 'nome' é apenas o nome do arquivo sem a extensão(.txt) e entre aspas simples, por exemplo 'teste'.
    Saída: Abrir um arquivo .txt, se ele existir no diretório. Além disso é retornado True ou False para ser utilizado dependendo da ocasião do uso.
    Exemplo:
        if lp.criar_arquivo_txt(nome) is True:
            print('Arquivo lido!!')
        else:
            print('Arquivo não existe!!')
"""

</code></pre>

