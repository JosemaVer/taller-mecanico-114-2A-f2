# Definicion de la clase Vehiculo
class Vehiculo:
    # Metodo constructor que inicializa los atributos de la instancia
    def __init__(self, patente: str, anio: int):
        # Validar que la patente sea una cadena de texto y no este vacia
        if not isinstance(patente, str) or not patente.strip():
            # Lanza un error si la patente no es valida
            raise ValueError("La patente no puede estar vacia y debe ser un texto valido.")
        
        # Validar que el anio sea un entero positivo de 4 digitos
        if not isinstance(anio, int) or anio < 1000 or anio > 9999:
            # Lanza un error si el anio no cumple con las condiciones
            raise ValueError("El anio debe ser un numero entero positivo de 4 digitos.")
        
        # Asignacion del atributo patente
        self.patente: str = patente.strip()
        # Asignacion del atributo anio
        self.anio: int = anio
        # Inicializacion automatica del atributo privado _en_taller en False
        self._en_taller: bool = False
