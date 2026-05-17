import random
import string

print("""\033[1;34m' 
==================================================>>
               
          ░██████╗░███████╗███╗░░██╗  
          ██╔════╝░██╔════╝████╗░██║  
          ██║░░██╗░█████╗░░██╔██╗██║  
          ██║░░╚██╗██╔══╝░░██║╚████║  
          ╚██████╔╝███████╗██║░╚███║  
          ░╚═════╝░╚══════╝╚═╝░░╚══╝  

        ██████╗░░█████╗░░██████╗░██████╗
       ██╔══██╗██╔══██╗██╔════╝██╔════╝
       ██████╔╝███████║╚█████╗░╚█████╗░
       ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗
       ██║░░░░░██║░░██║██████╔╝██████╔╝
       ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░
==================================================>>
[] AUTOR    :  ANGEL DEL VILLAR
[] TOOLS    :  GENERADOR DE PASS
[] VERSION  :  PREMIUM 
[] GITHUB   :  Angel-iluminaty 
==================================================>>""")

def generar_contrasena_con_nombres(nombre, cantidad):
    nombres_latinos = [
        'Juan', 'Diego', 'Pedro', 'Maria', 'Sofia', 'Luis', 'Ana', 'Carlos', 'Laura', 'Antonio', 'Camila', 'Alejandro',
        'Valentina', 'Javier', 'Manuela', 'Rafael', 'Isabella', 'Pablo', 'Catalina', 'Miguel', 'Juliana', 'Jorge',
        'Estefania', 'Fernando', 'Valeria', 'Roberto', 'Daniela', 'Gustavo', 'Carolina', 'Gabriel', 'Paola', 'Alberto',
        'Diana', 'Andres', 'Monica', 'Ramon', 'Elena', 'Nestor', 'Adriana', 'Luisa', 'Sebastian', 'Martha', 'Juanita',
        'Rodrigo', 'Claudia', 'Francisco', 'Natalia', 'Gonzalo', 'Angela', 'Arturo', 'Mercedes', 'Felipe', 'Veronica',
        'Leonardo', 'Tatiana', 'Hector', 'Patricia', 'Manuel', 'Renata', 'Ricardo', 'Estela', 'Adrian', 'Teresa',
        'Enrique', 'Juana', 'Martin', 'Olga', 'Hernan', 'Pamela', 'Julio', 'Lorena', 'Victor', 'Yolanda', 'Xavier',
        'Yolanda', 'Vicente', 'Rosa', 'Adolfo', 'Carmen', 'Raul', 'Silvia', 'hola', 'contraseña', 'segura', 'random', 'criptografia', 'python', 'azul', 'naranja', 'verde', 'plata',
                'luna', 'estrella', 'playa', 'montaña', 'rojo', 'amarillo', 'rosa', 'nube', 'perro', 'gato',
                'casa', 'coche', 'bicicleta', 'sol', 'noviembre', 'diciembre', 'enero', 'febrero', 'marzo', 'abril',
                'agua', 'fuego', 'tierra', 'aire', 'flor', 'arbol', 'libro', 'lapiz', 'papel', 'telefono',
                'internet', 'navegador', 'musica', 'pelicula', 'juego', 'computadora', 'celular', 'tableta', 'television',
                'gafas', 'sombrero', 'camisa', 'pantalon', 'zapatos', 'calcetines', 'reloj', 'anillo', 'collar', 'aretes',
                'mesa', 'silla', 'cama', 'ventana', 'puerta', 'cocina', 'baño', 'sala', 'comedor', 'patio',
                'fiesta', 'cumpleaños', 'navidad', 'vacaciones', 'trabajo', 'escuela', 'universidad', 'examen', 'tarea', 'proyecto',
                'viaje', 'avion', 'tren', 'barco', 'carretera', 'ciudad', 'pueblo', 'playa', 'campo', 'montaña',
                'corazon', 'mente', 'alma', 'cuerpo', 'vida', 'familia', 'amigos', 'amor', 'paz', 'feliz'
    ]

    simbolos = '@#$%&*+'
    
    contrasenas = []
    for _ in range(cantidad):
        nombre_random = random.choice(nombres_latinos)
        simbolo_random = random.choice(simbolos)
        numero_random = random.randint(0, 100)
        contrasena = nombre_random + str(numero_random) + simbolo_random
        contrasenas.append(contrasena)

    guardar_en_archivo(nombre, contrasenas)

def generar_contrasena_solo_simbolos_numeros(nombre, cantidad, longitud):
    simbolos_numeros = string.ascii_letters + string.digits

    contrasenas = []
    for _ in range(cantidad):
        contrasena = ''.join(random.choices(simbolos_numeros, k=longitud))
        contrasenas.append(contrasena)

    guardar_en_archivo(nombre, contrasenas)

def guardar_en_archivo(nombre_archivo, contrasenas):
    with open(f'/sdcard/{nombre_archivo}.txt', 'w') as file:
        file.write('\n'.join(contrasenas))
    print(f'Contraseñas guardadas en /sdcard/{nombre_archivo}.txt')

cantidad_contraseñas = int(input("Ingrese la cantidad de contraseñas a generar: "))
nombre_archivo = input("Ingrese el nombre del archivo de salida: ")

generar_contrasena_con_nombres(nombre_archivo + '_con_nombres', cantidad_contraseñas)
generar_contrasena_solo_simbolos_numeros(nombre_archivo + '_solo_numeros_letras', cantidad_contraseñas, 12)
