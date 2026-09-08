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
