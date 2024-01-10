def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a,b):
    return a/b

def dividir_controlado(a,b):
    if b == 0:
        return "No se puede dividir por cero"
    return a/b

if __name__ == "__main__":
    
    print(sumar(5, 3))
    print(restar(3, 50))
    print(multiplicar(-2, 30))
    print(dividir_controlado(8,0))
    
    try:
        print(dividir(8, 0))
    except ZeroDivisionError as e:
        print(f"Error: {e}")