import coresum

f = open("./texto-2.txt", "r")
txt = f.read()

t = coresum.Texto(txt)
resumo = t.resumir()
print(resumo)

