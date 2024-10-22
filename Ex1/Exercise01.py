X = int(input("Informe um número: "))
Y = 0

def fibonacci(Num):
    fibonacci = [0, 1]
    while fibonacci[-1] < Num:
        NextNum = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(NextNum)
    return fibonacci

Y = fibonacci(X)

if X in Y:
    print(f"O número {X} pertence à sequência de Fibonacci")
else:
    print(f"O número {X} não pertence à sequência de Fibonacci")