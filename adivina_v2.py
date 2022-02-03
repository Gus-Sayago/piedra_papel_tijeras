from random import randint
# el usuario debe adivinar un número que se genera al azar
# esta primera versión solo permite un intento
# en la siguiente version daremos más oportunidades y pistas




print("******* ADIVINA EL NÚMERO!!! ********")

#pdimos al usuario que seleccione nivel de dificultad

print("Selecciona el nivel de dificultad.")
print("Fácil: Advinar un número entre 1 y 10.")
print("Medio: Adivinar un número entre 1 y 50.")
print("Difícil: Adivinar un número entre 1 y 100.")

dificultad = input("Fácil(f) - Medio (m) - Difícil(d): ").lower()

if dificultad == 'f':
    numero_a_adivinar = randint(1,10)
    #pedimos al usuario que adivine el número
    numero_usuario = int(input("Adivina un número entre 1 y 10: "))
elif(dificultad == 'm'):
    numero_a_adivinar = randint(1,50)
    numero_usuario = int(input("Adivina un número entre 1 y 50: "))
else:
    numero_a_adivinar = randint(1,100)
    numero_usuario = int(input("Adivina un número entre 1 y 100: "))

#verificamos si acertó el número

if(numero_usuario == numero_a_adivinar):
    print("ACERTASTE!!!!")
    
else:
    print("PERDISTE!!!")

#mostramos el número a adivinar
print(f"El número era {numero_a_adivinar}")