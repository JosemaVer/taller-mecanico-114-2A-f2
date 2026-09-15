# 🚗 Taller Mecánico - 114-2A-f2

Repositorio del proyecto y bitácora de seguimiento para el módulo **Taller Mecánico (114-2A-f2)**.

---

## 📋 Información del Módulo

- **Módulo / Asignatura:** Taller Mecánico (114-2A-f2)
- **Autor / Estudiante:** JosemaVer
- **Estado del Proyecto:** En progreso 🚀

---

## 🎯 Objetivos

1. Implementar la solución técnica y de gestión requerida para el taller mecánico.
2. Mantener un registro cronológico y estructurado de los avances, decisiones técnicas y actividades realizadas.
3. Versionar el código fuente y la documentación a través de Git y GitHub.

---

## 📓 Bitácora de Actividades

| Sesión / Fecha | Tema / Actividad Principal | Avances y Entregables | Notas / Pendientes |
| :--- | :--- | :--- | :--- |
| **02/09/2026** | Inicialización del Repositorio | Creación del repositorio público, configuración de Git y plantilla de bitácora. | Definir próximos requerimientos y estructura base del código. |
| **07/09/2026** | Implementación Clase Vehículo | Creación de `vehiculo.py`, clase `Vehiculo` con atributos (`patente`, `anio`, `_en_taller`) y métodos `ingresar()` y `entregar()`. | Implementar siguientes clases y módulos del sistema. |
| **14/09/2026** | Polimorfismo, Tarifas y Validación de Patente | Definición de método abstracto `tarifa_hora()`, implementación en `Auto` ($30.000), `Moto` ($20.000) y `Camion` ($40.000), validación de patentes según legislación chilena y control de excepciones con `try-except` en `main.py`. | Continuar con la integración de los servicios del taller. |

---

### 📝 Registro Detallado de Sesiones

#### Sesión 1: Inicialización del Repositorio (02/09/2026)
- **Actividades realizadas:**
  - Configuración del repositorio local y remoto en GitHub.
  - Creación del archivo de bitácora inicial (README.md).
- **Próximos pasos:**
  - Iniciar la estructura del proyecto según los lineamientos del módulo.

#### Sesión 2: Implementación de la Clase Vehículo (07/09/2026)
- **Actividades realizadas:**
  - Creación del módulo `vehiculo.py`.
  - Definición de la clase `Vehiculo` con tipado estricto de datos.
  - Implementación de los atributos `patente: str`, `anio: int` y el atributo privado `_en_taller: bool` (inicializado en `False`).
  - Implementación de los métodos de negocio `ingresar()` y `entregar()`.
  - Documentación y comentarios explicativos por línea de código.
- **Próximos pasos:**
  - Continuar con el modelado de las clases del taller y su integración.

#### Sesión 3: Polimorfismo, Tarifas por Tipo y Validación de Patentes (14/09/2026)
- **Actividades realizadas:**
  - Implementación del método abstracto `tarifa_hora()` en la clase abstracta `Vehiculo`.
  - Implementación del método `tarifa_hora()` en las subclases:
    - `Moto`: Retorna $20.000.
    - `Auto`: Retorna $30.000.
    - `Camion`: Retorna $40.000.
  - Implementación de la validación de patentes según la legislación chilena (sin espacios, máximo 6 caracteres, formatos válidos para autos, camiones y motos).
  - Manejo de excepciones mediante bloques `try-except` (`ValueError`) en `main.py` para solicitar datos al usuario sin interrumpir la ejecución del programa ante errores de entrada.
- **Próximos pasos:**
  - Continuar con el modelado de clientes, órdenes de trabajo y servicios del taller mecánico.