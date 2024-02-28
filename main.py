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

precos = [20,100,500,600]
with open("precos_roupas.txt","w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
print(arquivo.closed)