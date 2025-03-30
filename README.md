# Buscador de Números Primos Especiales

----------
***

## Tabla de Contenido
1. [Informacion General](#informacion-general)
2. [Tecnologias](#tecnologias)
3. [Instalacion](#instalacion)
4. [Caracteristicas Principales](#caracteristicas-principales)
5. [Estructura del Sistema](#estructura-del-sistema)
6. [Colaboracion](#colaboracion)
7. [FAQs](#faqs)

### Informacion General
***
Este proyecto consiste en el desarrollo de un programa en Python que permite encontrar dos tipos especiales de números primos:

-   **Números primos gemelos**: Son pares de números primos cuya diferencia es exactamente 2 unidades. Ejemplo: (3,5), (5,7), (11,13).
    
-   **Números primos palindrómicos**: Son números primos que pueden leerse igual de izquierda a derecha y de derecha a izquierda. Ejemplo: 131, 757.

## Tecnologias
***

Este sistema ha sido desarrollado utilizando las siguientes tecnologías:

-   **Python**: Lenguaje de programación principal.
-   **GitHub**: Para la gestión de versiones y colaboración en el desarrollo.

## Instalacion
***
Siga estos pasos para instalar y ejecutar el sistema:
```
$ git clone [BryanVillabona/Numeros-Primos-Especiales](https://github.com/BryanVillabona/Numeros-Primos-Especiales)
$ cd Numeros-Primos-Especiales-main
$ python main.py
```

## Caracteristicas Principales
***
El programa proporciona un menú interactivo para que el usuario seleccione entre las siguientes opciones:

1.  Encontrar y mostrar pares de números primos gemelos en un rango dado.
    
2.  Encontrar y mostrar números primos palindrómicos en un rango dado.
    
3.  Salir del programa.

## Estructura del Sistema
***
El programa está estructurado de la siguiente manera:

-   **Menú interactivo**: Permite al usuario elegir entre encontrar primos gemelos o primos palindrómicos.
    
-   **Funciones principales**:
    
    -   Verifica si un número es primo.
        
    -   Busca y muestra los pares de primos gemelos dentro del rango dado.
        
    -   Determina si un número es palindrómico.
        
    -   Busca y muestra los primos palindrómicos dentro del rango dado.
        
-   **Entrada del usuario**: Solicita el límite superior del rango de búsqueda y ejecuta la opción seleccionada.

## Colaboracion
***

Si deseas colaborar en el proyecto, puedes:

1.  Hacer un fork del repositorio.
    
2.  Crear una rama con tus cambios (`git checkout -b mi-rama`).
    
3.  Realizar un commit (`git commit -m "Descripción de cambios"`).
    
4.  Enviar un pull request.
    

Cualquier aporte es bienvenido, ya sea en el código, la documentación o sugerencias para mejorar el sistema.

## FAQs
***
1.  **¿Cuál es el límite máximo recomendado para la búsqueda de primos?**  _Depende del rendimiento del equipo, pero se recomienda un límite de hasta 100,000 para obtener resultados rápidos._
    
2.  **¿Se puede modificar el rango de búsqueda?**  _Sí, el usuario ingresa el límite superior en la ejecución del programa._
    
3.  **¿Es posible agregar otros tipos de números especiales?**  _Sí, el programa puede ampliarse para incluir otros tipos de números especiales._
