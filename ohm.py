#Este programa calcula la ley de Ohm
print("Ley de Ohm")
print("Selecciona la opcion")
opcion=int(input("1=Voltaje, 2=Corriente, 3=Resistencia: "))
try:
	if opcion == 1:
		# Calcular Voltaje
		I = float(input("Introduce la corriente (amperios): "))
		R = float(input("Introduce la resistencia (ohmios): "))
		V = I * R
		print(f"El voltaje es: {V} voltios")
	elif opcion == 2:
		# Calcular Corriente
		V = float(input("Introduce el voltaje (voltios): "))
		R = float(input("Introduce la resistencia (ohmios): "))
		if R == 0:
			print("Error: La resistencia no puede ser cero.")
		else:
			I = V / R
			print(f"La corriente es: {I} amperios")
	elif opcion == 3:
		# Calcular Resistencia
		V = float(input("Introduce el voltaje (voltios): "))
		I = float(input("Introduce la corriente (amperios): "))
		if I == 0:
			print("Error: La corriente no puede ser cero.")
		else:
			R = V / I
			print(f"La resistencia es: {R} ohmios")
	else:
		print("Opción no válida.")
except Exception as e:
	print(f"Error: {e}")
