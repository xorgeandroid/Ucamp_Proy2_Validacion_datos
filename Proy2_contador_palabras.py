palabra = input("Ingresa una palabra (entre 4 y 8 caracteres): ")
longitud = len(palabra)

if not palabra.isalpha():
    print("Lo siento, sólo puede contener letras.")
elif longitud >= 4 and longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")