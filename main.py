from vehiculo import Vehiculo
from auto import Auto
from camion import Camion
from moto import Moto

v=Vehiculo("1234", 1930)
a=Auto("1234",1930)

a.ingresar_al_taller()
print(a.patente)

v.ingresar_al_taller()
print("El vehiculo esta en el taller")

print(v.tarifa_hora())

v.entregar_al_cliente()

print(v._en_taller)

print("La pantete del vehiculo es:",v.patente_v())

