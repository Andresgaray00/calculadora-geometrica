

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except:
            print("Valor inválido, intenta de nuevo.")


def rectangulo():
    base = pedir_numero("Ingresa la base: ")
    altura = pedir_numero("Ingresa la altura: ")
    area = base * altura
    print("Área del rectángulo:", area)
    print("")


def cuadrado():
    lado=pedir_numero("Ingrese el lado: ")
    area=lado**2
    print("Área del Cuadrado :", area)
    print("")

def triangulo_rectangulo():
    base = pedir_numero("Ingresa la base: ")
    altura = pedir_numero("Ingresa la altura: ")
    area = (base * altura) / 2
    print("Area del triángulo:", area)
    print("")


def cubo():
    lado = pedir_numero("Ingresa el lado: ")
    volumen = lado ** 3
    densidad = pedir_numero("ingresa la densidad: ")
    masa = densidad * volumen
    print("Volumen del cubo:", volumen)
    print("masa del cubo:", masa)
    print("")


def esfera():
    radio = pedir_numero("Ingresa el radio: ")
    volumen = (4/3) * 3.1416 * (radio ** 3)
    print("Volumen de la esfera:", volumen)
    print("")

def triangulo(): 
    base = pedir_numero("ingresa la base: ")
    altura = pedir_numero("ingresa la altura ")
    area = (base * altura) /2
    print("area del triangulo:", area)

def circulo():
    radio = pedir_numero("ingresa el radio: ")
    area = 3.1416 * (radio ** 2)
    print("el area del circulo:", area)

def paralelepipedo():
    largo = pedir_numero("ingresa el largo: ")
    ancho = pedir_numero("ingresa el ancho: ")
    alto = pedir_numero("ingresa el alto: ")
    
    volumen = largo * ancho * alto
    area = 2 * (largo*ancho + largo*alto + ancho*alto)

    densidad = pedir_numero("ingresa la densidad: ")
    masa = densidad * volumen 
    
    print("area del paralelepipodo:", area)
    print("volumen del paralelepipedo:", volumen)
    print("masa del paralelepipodo:", masa)


# --- MENÚ ---
def menu():
    while True:
        print("-----CALCULADORA GEOMÉTRICA-----")
        print("1. Rectángulo (Área)")
        print("2. Triángulo Rectángulo (Área)")
        print("3. Cubo (Volumen)")
        print("4. Esfera (Volumen)")
        print("5. Cuadrado (Area)")
        print("6. triangulo (area)")
        print("7. circulo (area)" )
        print("8. paralelepipodo")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            rectangulo()
        elif opcion == "2":
            triangulo_rectangulo()
        elif opcion == "3":
            cubo()
        elif opcion == "4":
            esfera()
        elif opcion=="5":
            cuadrado()
        elif opcion=="6":
            triangulo()
        elif opcion=="7":
            circulo()
        elif opcion=="8":
            paralelepipedo()
        elif opcion =="9":
            print("Saliendo  de la calculadora...")
            break
        else:
            print("Opción inválida")


menu()