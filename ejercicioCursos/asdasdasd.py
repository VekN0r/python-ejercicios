"""toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2"""

num = int(input("Ingresa un numero"))
paso = 0

while num != 1:
    if num % 2 == 0:
        num = num / 2
        if num != 1:
            paso += 1
            print(num)
            continue
        elif num == 1:
            paso += 1
            print(num)
            break
    elif num % 2 == 1:
        num = 3 * num + 1
        if num != 1:
         paso += 1
         print(int(num))
         continue

print(paso)