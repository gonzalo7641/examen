import re

print("Prueba de Python")

print("Ingresa los siguientes datos:")

tabla = []
nroDatos = int(input("Ingresa el numero de registros para guardar: "))


def verificarIP(ip):
    pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
    test = pat.match(ip)
    return test

for var in range(nroDatos):
    ip = input("Ingresa la IP: ")
    resp = verificarIP(ip)
    if resp:
        print ("Ip Correcta")
    else:
        print ("Ip Incorrecta")
        break
    nombre = input("Ingresa el Nombre del PC :")
    objCompu = {"IP": ip, "Nombre":nombre}
    tabla.append(objCompu)

print("Estos son los datos de la tabla")
print("IP\t\t\tNOMBRE PC")
for item in tabla:
    print(item["IP"]+"\t\t"+item["Nombre"])

