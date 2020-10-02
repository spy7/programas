print ("╔════════════════╗")
for linhas in range(8):
    lista = ""
    for colunas in range(8):
        if (linhas + colunas) % 2 == 0:
            lista = lista + "  "
        else:
            lista = lista + "██"
    print("║" + lista + "║")
print ("╚════════════════╝")
