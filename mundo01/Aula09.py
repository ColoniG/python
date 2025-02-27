print("#" * 140, "\n")
# Começar o código apartir daqui
frase = "Curso em Video Python"
frase2 = "   Aprenda Python  "

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print("**************************************************")

print(len(frase))
print(frase.count("o"))
print(frase.count("o", 0, 13))
print(frase.find("deo"))
print(frase.find("Android"))
print("Curso" in frase)
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print("**************************************************")

print(frase2, end="") 
print("!")
print(frase2.strip(), end="") 
print("!")
print(frase2.rstrip(), end="") 
print("!")
print(frase2.lstrip(), end="") 
print("!")

print("**************************************************")

frase_splited = frase.split()
print(frase_splited)
print("-".join(frase_splited))

print("**************************************************")

print(frase.upper().count("O"))

print(len(frase2.strip()))



print("""O que é Lorem Ipsum?
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.""")
# Finalizar até aqui
print("")
print("#" * 140)

