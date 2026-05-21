## 🐍 Documentación Python para CheckPoint 6

- **Autor:** Ailén
- **Nivel:** Iniciación
- **Formato:** Markdown
- **Fecha:** Mayo 2026

---

## 📄Tabla de contenidos:

1. [¿Para qué usamos Clases en Python?](#1-clases-en-python)

2. [¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#2-metodos-en-python)

3. [¿Cuáles son los tres verbos de API?](#3-verbos-de-apis-en-python)

4. [¿Es MongoDB una base de datos SQL o NoSQL?](#4-mongodb)

5. [¿Qué es una API?](#5-que-es-una-api)

6. [¿Qué es Postman?](#6-postman)

7. [¿Qué es el polimorfismo?](#7-que-es-el-polimorfismo)

8. [¿Qué es un método dunder?](#8-metodo-dunder)

9. [¿Qué es un decorador de python?](#9-decoradores-en-python)



## 1. Clases en Python

Una clase es una plantilla o molde que define cómo se creará un objeto. Permiten empaquetar datos (atributos) y comportamientos (métodos) juntos, lo que facilita la creación de objetos.

### ⚙️ Sintaxis Básica

En Python, definimos una clase usando la palabra reservada class seguida del nombre en mayúscula (CamelCase) y dos puntos (:). Todo lo que pertenece a la clase va indentado (con cuatro espacios) debajo.

### ¿Para qué las usamos?

Las usamos principalmente para organizar el código y aplicar un concepto llamado Programación Orientada a Objetos (POO). Sus mayores ventajas son:

- Evitan duplicar código: Defines el comportamiento una sola vez en la clase y lo reutilizas mil veces.

- Organización: Juntan los datos (variables) y las acciones (funciones) en un solo lugar lógico.

- Modelar el mundo real: Hacen que el código sea más fácil de entender porque programamos pensando en "cosas" (usuarios, productos, enemigos, facturas) en lugar de solo líneas de texto sueltas.

### Conceptos Claves

- **Constructor (__init__):** 
Es un método especial que se ejecuta automáticamente cuando creas un objeto a partir de la clase. Se utiliza para asignar los valores iniciales a los atributos.
- **self:** 
Representa la instancia actual de la clase. Es obligatorio incluirlo como el primer parámetro en los métodos para poder acceder a los atributos propios del objeto.
- **Instancias:**
 Son los objetos individuales creados a partir de la clase. Cada instancia tiene sus propios datos.

**Ejemplo sin clases (desorganizado):**
```python
marca_pickup1 = "toyota"
modelo_pickup1 = "hilux"
 
marca_pickup2 = "volkswagen"
modelo_pickup2 = "amarok"
```
 
**Ejemplo con clases (organizado):**
```python
class Pick_up:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Añadimos un método (comportamiento)
    def describir(self):
        print(f"Esta pick-up es una {self.marca} {self.modelo}.")      

 
# Creamos los objetos
pickup1 = Pick_up("toyota", "hilux")
pickup2 = Pick_up("volkswagen", "amarok")
 
# Ahora todas las pick-ups saben describirse solas
pickup1.describir()  # Imprime: Esta pick-up es una toyota hilux.
pickup2.describir()  # Imprime: Esta pick-up es una volkswagen amarok.
```
 
Con una clase, podemos crear todas las pick-ups que queramos usando el mismo molde.

**💡 ¿Qué significa self.marca = marca?**
Pensalo como una ficha de registro:

- marca (derecha) → es el dato que llega desde afuera cuando creás el objeto, como "toyota"
- self.marca (izquierda) → es donde ese dato queda guardado dentro del objeto para usarlo después

No tienen que llamarse igual, pero se hace por convención para que quede claro que son el mismo dato.

## 2. Métodos en Python

El método que se ejecuta automáticamente cuando se crea una instancia de una clase es __init__ (abreviación de initialize o inicializar en inglés). En el mundo de la programación, a este tipo de funciones especiales se les conoce como "Constructores".

### ¿Para qué se utiliza?

Su función principal es inicializar los atributos y preparar el estado inicial del objeto.

Imagínate que la clase es el molde para fabricar teléfonos móviles. No queremos que todos los teléfonos salgan de la fábrica vacíos; necesitamos que cada uno tenga su propio número de serie, color y modelo desde el momento en que se fabrican.

El método __init__ se utiliza para:

- Darle vida al objeto con datos iniciales: Configura las características únicas de cada instancia en el segundo exacto en que nace.

- Automatizar procesos: Evita tener que crear el objeto vacío y luego escribir líneas de código extra para asignarle cada dato uno por uno.

⚙️ Sintaxis y Estructura
En Python, este método se reconoce porque lleva dos guiones bajos antes y dos después (__init__). Esto le indica a Python que es un método especial ("método mágico") con un comportamiento interno propio.

### Sintaxis
```python
class NombreClase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
```

### Ejemplo
```python
class Movil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"¡Se creó un móvil {self.marca}!")

mi_movil = Movil("Iphone", "12 mini")
# Se imprime automáticamente: ¡Se creó un móvil Iphone!
```

💡 Nota clave: No necesitás llamar a `__init__` manualmente, Python lo hace solo
cuando escribís `Movil("Iphone", "12 mini")`.