X = input("Digite uma Palavra: ")
print("-" * 10)
if X.lower().count('a') > 0:
    print(f"a letra 'A' aparece {X.lower().count('a')} vez(es) na Palavra")
else:
    print(f"A letra 'A' não aparece na Palavra")
print("-" * 10)