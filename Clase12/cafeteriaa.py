with open ("ventas.txt","r") as texCom:
    textComp = texCom.readlines()

panBace = []
pieLimon = []
cafe = []
te = []
alfajor = []

for indice, datos in enumerate(textComp):
    almDatos = [int(i) for i in datos.strip().split(',')]
    if indice == 0:
        panBace.extend(almDatos)
    elif indice == 1:
        pieLimon.extend(almDatos)
    elif indice == 2:
        cafe.extend(almDatos)
    elif indice == 3:
        te.extend(almDatos)
    elif indice == 4:
        alfajor.extend(almDatos)

panBaceC = sum(panBace)
pieLimonC = sum(pieLimon)
cafeC = sum(cafe)
teC = sum(te)
alfajorC = sum(alfajor)

print(f"--------Ventas------","Cantidad promedio vendida")
print(f"Pan ciabbata: {panBaceC}  Cantidad promedio: {panBaceC/4}")
print(f"Pie de limon: {pieLimonC}   Cantidad promedio: {pieLimonC/4}")
print(f"Cafe:\t {cafeC}\t   Cantidad promedio: {cafeC/4}")
print(f"Te:\t {teC}\t   Cantidad promedio: { teC/4}")
print(f"Alfajor: {alfajorC} \t   Cantidad promedio: {alfajorC/4}")


"""
Después de analizar las ventas de la cafetería, se te ha solicitado generar un informe de
ventas que muestre las ventas de cada producto por día y el total de ventas por día. El
informe debe guardarse en un archivo llamado "informe_ventas.txt"
"""
with open("informe_ventas.txt","w",encoding="utf-8")as InformeVentas:
   
    InformeVentas.write("Producto \t\t\t\t|Ventas por día|\t\t\t\t \t\t|Cantidad por dia|  \n")
    InformeVentas.write("\t\t\t\tLunes\t Martes\t Miercoles\t Jueves\n")
    InformeVentas.write(f"Pan Ciabatta:\t {panBace[0]}\t\t\t{panBace[1]}\t\t {panBace[2]}\t\t   {panBace[3]}\t\t\t\t\t\t{panBaceC}\n")
    InformeVentas.write(f"Pie de limón:\t {pieLimon[0]}\t\t    {pieLimon[1]}\t\t {pieLimon[2]}\t\t   {pieLimon[3]}\t\t\t\t\t\t{pieLimonC} \n")
    InformeVentas.write(f"Cafe:\t\t\t {cafe[0]}\t\t\t{cafe[1]}\t\t {cafe[2]}\t\t   {cafe[3]}\t\t\t\t\t\t{cafeC}\n")
    InformeVentas.write(f"Te:\t\t\t\t {te[0]}\t\t\t{te[1]}\t\t {te[2]}\t\t   {te[3]}\t\t\t\t\t\t{teC}\n")
    InformeVentas.write(f"Alfajór:\t\t {alfajor[0]}\t\t    {alfajor[1]}\t\t {alfajor[2]}\t\t   {alfajor[3]}\t\t\t\t\t\t{alfajorC}\n")


