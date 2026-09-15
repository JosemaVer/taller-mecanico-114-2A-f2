import re
from abc import ABC, abstractmethod

# Definicion de la clase Vehiculo
class Vehiculo(ABC):
    # Metodo para validar que la patente cumpla con la legislacion chilena
    @staticmethod
    def validar_patente(patente: str) -> str:
        if not isinstance(patente, str):
            raise ValueError("La patente debe ser texto.")
        
        if " " in patente:
            raise ValueError("La patente no es valida: no debe contener espacios.")
        
        if len(patente) > 6:
            raise ValueError(f"La patente no es valida: no puede tener mas de 6 caracteres (recibidos: {len(patente)}).")
        
        patente_limpia = patente.strip().upper()
        # Formatos segun legislacion chilena:
        # - Autos/Camiones: 4 letras + 2 digitos (BBBB10) o 2 letras + 4 digitos (AA1000) -> 6 caracteres
        # - Motos: 3 letras + 2 digitos (BBB10) o 2 letras + 3 digitos (AA100) -> 5 caracteres
        patron_chile = r"^([A-Z]{4}\d{2}|[A-Z]{2}\d{4}|[A-Z]{3}\d{2}|[A-Z]{2}\d{3})$"
        if not re.match(patron_chile, patente_limpia):
            raise ValueError(f"La patente '{patente}' no es valida segun la legislacion chilena.")
            
        return patente_limpia

    # Metodo constructor que inicializa los atributos de la instancia
    def __init__(self, patente: str, anio: int):
        # Asignacion del atributo patente validada
        self.patente: str = self.validar_patente(patente)
        # Asignacion del atributo anio
        self.anio: int = anio
        # Inicializacion automatica del atributo privado _en_taller en False
        self._en_taller: bool = False

    # Metodo para registrar el ingreso del vehiculo al taller
    def ingresar_al_taller(self) -> None:
        # Cambia el estado de _en_taller a True indicando que el vehiculo esta en el taller
        self._en_taller = True

    # Alias / metodo ingresar
    def ingresar(self) -> None:
        self.ingresar_al_taller()

    # Metodo para registrar la entrega del vehiculo al cliente
    def entregar_al_cliente(self) -> None:
        # Cambia el estado de _en_taller a False indicando que el vehiculo salio del taller
        self._en_taller = False

    # Alias / metodo entregar
    def entregar(self) -> None:
        self.entregar_al_cliente()

    # Metodo abstracto que retorna la tarifa por hora del vehiculo
    @abstractmethod
    def tarifa_hora(self) -> int:
        pass

    def patente_v(self) -> str:
        return self.patente
