inicio, fim = int(input("Digite o valor inicial: ")), int(input("Digite o valor final: "))
print([i for i in range(inicio, fim + 1) if i % 2 != 0])
