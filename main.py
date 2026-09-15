from vehiculo import Vehiculo
from auto import Auto
from camion import Camion
from moto import Moto

# Solicitar datos al usuario controlando posibles errores con try-except
while True:
    try:
        patente_ingresada = input("Ingrese la patente del auto (max 6 caracteres, sin espacios, formato Chile): ")
        anio_ingresado = int(input("Ingrese el año del vehiculo: "))
        
        # Creacion del objeto: validara la patente automaticamente
        a = Auto(patente_ingresada, anio_ingresado)
        print("\n Vehiculo registrado con exito!")
        print(f"Patente registrada: {a.patente_v()}")
        break
    except ValueError as error:
        # Se captura el error de validacion o de tipo y se muestra el mensaje sin caer el programa
        print(f" Error: {error} Por favor, intente nuevamente.\n")

# Operaciones con el vehiculo creado
a.ingresar_al_taller()
print("Estado en taller:", a._en_taller)
print("Tarifa por hora del vehiculo: $", a.tarifa_hora())

a.entregar_al_cliente()
print("Estado en taller despues de entrega:", a._en_taller)


