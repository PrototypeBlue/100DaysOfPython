import random

secret_number = random.randint(1,500)

print("Escoge un numero del 1 al 500")

print(secret_number)

while True:
	res = input("Adivina el numero: ")
	print(res)
	if secret_number == secret_number:
		print ("Ganaste")
		break
	else:
		print ("Perdiste")
		continue