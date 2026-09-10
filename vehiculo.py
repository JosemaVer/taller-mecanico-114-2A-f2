# Definicion de la clase Vehiculo
class Vehiculo:
    # Metodo constructor que inicializa los atributos de la instancia
    def __init__(self, patente: str, anio: int):
        # Asignacion del atributo patente
        self.patente: str = patente
        # Asignacion del atributo anio
        self.anio: int = anio
        # Inicializacion automatica del atributo privado _en_taller en False
        self._en_taller: bool = False

    # Metodo para registrar el ingreso del vehiculo al taller
    def ingresar_al_taller(self) -> None:
        # Cambia el estado de _en_taller a True indicando que el vehiculo esta en el taller
        self._en_taller = True

    # Metodo para registrar la entrega del vehiculo al cliente
    def entregar_al_cliente(self) -> None:
        # Cambia el estado de _en_taller a False indicando que el vehiculo salio del taller
        self._en_taller = False

    # Metodo que retorna la tarifa por hora generica del vehiculo
    def tarifa_hora(self) -> int:
        return 5000

    def patente_v(self) -> str:
        return self.patente
