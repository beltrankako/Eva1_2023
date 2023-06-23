check = 0 

while check == 0:
   vlan = int(input("¿Cual es la ID de su Vlan? "))
   if vlan >=1 and vlan <=1005:
    print("La Vlan ingresada corresponde a una Vlan basica")
    break
   elif vlan >= 1006 and vlan <= 4095:
       print("La Vlan ingresada corresponde a una Vlan de Rango superior")
       break
   else:
       print("El numero de Vlan ingresado es desconocida")
       check = 0
       