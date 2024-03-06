# arquivo = open("novotexto.txt","w")
'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
print(arquivo.seek(0))
print(arquivo.tell())
arquivo.close()
print(arquivo.closed)

print(arquivo.read())
print(arquivo.seek(10))
print(arquivo.read(8))
print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)'''

# arquivo.write("arquivo de sadasd")
# arquivo.close()

# arquivo =  open('frutas.txt', 'w')
# arquivo.write('banana \n uva \n mamao')
# arquivo.close()

# disciplinas = [ 'RAD \n', 'introdução a C \n', 'programação']
# with open('disciplinas.txt', 'w') as file:
#     file.write( "relaçao de discplinas \n")
#     file.writelines(disciplinas)
# with open('disciplinas.txt', 'r') as file:
#     print(file.read())

# with open('precos_roupas.txt', 'r') as arquivo:
#     print("representação original da linha")
#     for linha in arquivo:
#         print(repr(linha))

# with open("precos_roupas.txt", "r") as arquivo:
#     print('conteudo da linha')
#     for linha in arquivo:
#         linha_ = linha.strip()
#         print(repr(linha_))

'''minha_lista = ['arroz', 'feijao','carne']
lista_ = ';'.join(minha_lista)
with open('precos_roupas.txt','w') as arquivo:
    arquivo.write(lista_)'''

# try:
#     with open("arquivo_test.txt", 'r') as arquivo:
#         print(arquivo.read())
# except FileNotFoundError:
#     print("arquivo inexistente")

import os

# try:
#     os.remove('teste.txt')
#     print('arquviod removido')
# except FileNotFoundError as erro:
#     print("arquivo inexistente")
#     print('descrição: ', erro)

# try:
#     f = open('novo2.txt','r')
#     f.write('hello')
# except IOError as erro:
#     print('erro foi: ', erro)

notas = [('carlos',2.0), ('lucas',10.0), ('maria',5.0)]
try:
    with open('notas.txt', 'w') as n:
        for nome,nota in notas:
            n.write(f'nome{nome} nota:{nota}')
except FileNotFoundError:
    print('erro')


with open('notas.txt','r') as f:
    for linha in f:
        print(f.seek(0))
        print(f.read())
