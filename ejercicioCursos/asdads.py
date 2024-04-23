palabraUser = str(input("Hola ingresa alguna palabra"))
palabraUser = palabraUser.upper()
palabraSinVocal = ""
for eliminarVocal in palabraUser:
    if eliminarVocal == "A" or eliminarVocal == "E" or eliminarVocal == "I" or eliminarVocal == "O" or eliminarVocal == "U":
        continue
    if eliminarVocal == "1":
        continue
    else:
        palabraSinVocal = eliminarVocal 
        print(palabraSinVocal,end="")