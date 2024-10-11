# Funcions per a cada operació
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacio(x, y):
    return x * y

def divisio(x, y):
    if y == 0:
        return "Error: No es pot dividir entre zero."
    return x / y

# Menú de la calculadora
def calculadora():
    print("Selecciona una operació:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")

    while True:
        # Demanar a l'usuari que selecciona una operació
        eleccio = input("Introdueix el número de l'operació (1/2/3/4): ")

        # Comprovar si l'elecció és vàlida
        if eleccio in ['1', '2', '3', '4']:
            num1 = float(input("Introdueix el primer número: "))
            num2 = float(input("Introdueix el segon número: "))

            if eleccio == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif eleccio == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")
            elif eleccio == '3':
                print(f"{num1} * {num2} = {multiplicacio(num1, num2)}")
            elif eleccio == '4':
                print(f"{num1} / {num2} = {divisio(num1, num2)}")
        else:
            print("Elecció no vàlida. Torna a intentar.")

        # Preguntar si volen fer una altra operació
        continuar = input("Vols fer una altra operació? (si/no): ")
        if continuar.lower() != 'si':
            break

# Executar la calculadora
if __name__ == "__main__":
    calculadora()
