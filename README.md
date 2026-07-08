Sistema de Alquiler de Bicicletas
Integrantes del grupo C23 Comisión C
•	Spipp, Matias Hernan
•	Botello Da Silva, German Alexis
•	Escalante Sandoval, Juan Manuel
•	Mello, Braian German
•	Ferreyra, Brian Joel
Descripción general del sistema
Este proyecto se trata del desarrollo de un sistema de gestión de alquiler de bicicletas implementado en Python y ejecutado mediante consola. El mismo permite administrar la información de clientes, bicicletas y alquileres, almacenando los datos de forma persistente mediante archivos de texto (.txt).
Las principales funcionalidades implementadas son:
•	Registro de clientes.
•	Consulta y eliminación de clientes.
•	Registro de bicicletas.
•	Consulta de bicicletas.
•	Cambio de estado de bicicletas.
•	Visualización de bicicletas disponibles.
•	Registro de alquileres.
•	Registro de devoluciones.
•	Cálculo automático del tiempo de uso.
•	Cálculo del importe del alquiler.
•	Estadísticas generales de utilización de las bicicletas.
Durante el desarrollo se aplicaron los contenidos trabajados en la asignatura:
-	estructuras condicionales;
-	estructuras repetitivas;
-	funciones;
-	modularización;
-	validaciones;
-	manejo básico de errores;
-	acumuladores y contadores;
-	lectura y escritura de archivos.
Estructura del Proyecto:
Proyecto/
│
├── main.py
├── clientes.py
├── bicicletas.py
├── alquiler.py
│
├── clientes.txt
├── bicicletas.txt
├── alquileres.txt
│
└── README.md

Instrucciones de ejecución:
Requisitos:
- Python 3.10 o superior.
Ejecución:
1. Clonar o descargar el repositorio.
2. Abrir la carpeta del proyecto.
3. Verificar que se encuentren los archivos:
-	clientes.txt
-	bicicletas.txt
-	alquileres.txt
4. Ejecutar el programa desde la terminal.
5. Utilizar el menú principal para acceder a los distintos módulos del sistema.
Funcionalidades implementadas:
Gestión de clientes
•	Registrar clientes. 
•	Consultar clientes. 
•	Mostrar listado completo. 
•	Eliminar clientes. 
•	Validación de DNI, nombre, correo electrónico y teléfono. 
Gestión de bicicletas
•	Registrar bicicletas. 
•	Consultar bicicletas. 
•	Mostrar todas las bicicletas. 
•	Mostrar bicicletas disponibles. 
•	Cambiar estado de una bicicleta. 
Estados posibles:
•	Disponible 
•	Alquilada 
•	Mantenimiento 
Gestión de alquileres
•	Registrar alquiler. 
•	Registrar devolución. 
•	Verificar disponibilidad. 
•	Actualizar automáticamente el estado de la bicicleta. 
•	Calcular tiempo de uso. 
•	Calcular importe del alquiler. 
Estadísticas
El sistema permite consultar información general del uso de las bicicletas, incluyendo:
•	cantidad total de alquileres registrados; 
•	cantidad de usos por bicicleta; 
•	tiempo total de utilización por bicicleta; 
•	tiempo promedio de uso por bicicleta. 
________________________________________
Tecnologías utilizadas
•	Python 3 
•	Programación estructurada 
•	Funciones 
•	Modularización 
•	Diccionarios 
•	Archivos de texto (.txt) 
•	Git 
•	GitHub 
________________________________________
Uso de Inteligencia Artificial
Durante el desarrollo del proyecto se utilizaron 2 IA como apoyo:
Gemini Pro
Se utilizó para:
•	generación de ideas; 
•	revisión de lógica; 
•	detección y corrección de errores puntuales; 
•	propuestas de mejora del código. 
ChatGPT (OpenAI)
Se utilizó para:
•	diseño de la arquitectura general del proyecto; 
•	explicación de conceptos de Python; 
•	implementación de funciones; 
•	modularización del sistema; 
•	reutilización de código entre módulos; 
•	organización del proyecto; 
•	revisión y optimización del código; 
En todos los casos, las respuestas proporcionadas por la IA se revisaron por los integrantes del grupo antes de agregarlas al proyecto, asegurando la comprensión del funcionamiento de cada módulo y sus decisiones.
