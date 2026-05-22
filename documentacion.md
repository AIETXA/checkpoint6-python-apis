## 🐍 Documentación Python para CheckPoint 6

- **Autor:** Ailén
- **Nivel:** Iniciación
- **Formato:** Markdown
- **Fecha:** Mayo 2026

---

## 📄Tabla de contenidos:

1. [¿Para qué usamos Clases en Python?](#1-clases-en-python)

2. [¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#2-metodos-en-python)

3. [¿Cuáles son los verbos de API?](#3-verbos-de-apis-en-python)

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

### 🔧 ¿Para qué las usamos?

Las usamos principalmente para organizar el código y aplicar un concepto llamado Programación Orientada a Objetos (POO). Sus mayores ventajas son:

- Evitan duplicar código: Defines el comportamiento una sola vez en la clase y lo reutilizas mil veces.

- Organización: Juntan los datos (variables) y las acciones (funciones) en un solo lugar lógico.

- Modelar el mundo real: Hacen que el código sea más fácil de entender porque programamos pensando en "cosas" (usuarios, productos, enemigos, facturas) en lugar de solo líneas de texto sueltas.

### 📋 Conceptos Claves

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

### 🔧 ¿Para qué se utiliza?

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


## 3. Verbos de APIs en Python

Las APIs REST son fundamentales en el desarrollo de software moderno. Para interactuar con ellas, utilizamos los **verbos HTTP**, que permiten definir el tipo de acción que queremos realizar sobre los recursos de la API.

### ¿Qué son los verbos HTTP?
 
Los verbos HTTP (también llamados métodos HTTP) indican la acción que se desea realizar sobre un recurso en una API. En una API REST, los recursos suelen representarse como URLs.
Por ejemplo, en una API que gestiona recetas de cocina, el recurso principal sería:

https://api.ejemplo.com/recetas

Los verbos HTTP nos permiten:

- Obtener información (GET)
- Crear un nuevo recurso (POST)
- Actualizar un recurso existente (PUT o PATCH)
- Eliminar un recurso (DELETE)

### Verbos HTTP más utilizados en APIs REST

 1. **GET – Obtener recursos**
 El método **GET** se usa para recuperar información de la API.

- Es un método seguro: No modifica ni altera ningún dato en el servidor, solo los lee.
- Es idempotente: Significa que no importa si haces la misma petición GET 1 vez o 100 veces, el resultado en el servidor siempre será el mismo y no causarás efectos secundarios.
- Permite usar parámetros en la URL para filtrar o buscar resultados específicos.

**Ejemplo (Flask):**
```python
#Endpoint para obtener todas las recetas
@app.route("/recetas", methods=["GET"])
def obtener_recetas():
    todas_las_recetas = Receta.query.all()
    resultado = recetas_schema.dump(todas_las_recetas)
    return jsonify(resultado)
```    
💡 La idea es simple: Cuando un cliente (como un navegador web) hace una petición GET a /recetas, este código va a la base de datos, trae todas las recetas registradas, las convierte a formato JSON y las devuelve. Es como decirle al servidor: "dame la lista de recetas que tenés guardada".

2. **POST – Crear un nuevo recurso**
El método **POST** se usa para enviar datos al servidor y crear un nuevo recurso.

- No es seguro ni idempotente: Si envías la misma petición POST tres veces, crearás tres registros duplicados en la base de datos.
- La información viaja oculta y segura dentro del cuerpo (body) de la solicitud, no en la URL.

**Ejemplo (Flask):**
```python
# Endpoint para crear una nueva receta
@app.route('/recetas', methods=["POST"])
def agregar_receta():
    nombre = request.json['nombre']
    ingredientes = request.json['ingredientes']

    nueva_receta = Receta(nombre, ingredientes)

    db.session.add(nueva_receta)
    db.session.commit()

    return receta_schema.jsonify(nueva_receta)
```
Lo que hace paso a paso:
- Recibe los datos que mandaste en el body del POST (nombre, ingredientes).
- Crea un nuevo objeto Receta con esos datos.
- Lo guarda en la base de datos de forma definitiva usando add() y commit().
- Devuelve la receta recién creada en formato JSON para confirmar que se guardó bien.

La diferencia clave con GET es que acá sí usás el body para mandar los datos, algo así en Postman:
```json
{
    "nombre": "Milanesa",
    "ingredientes": "carne, pan rallado, huevo"
}
```

3. **PUT – Reemplazar un recurso completo**
El método **PUT** se usa para actualizar un recurso existente reemplazando todos sus atributos por los nuevos datos enviados.

- Es idempotente:Si mandas la misma actualización muchas veces, el recurso quedará exactamente igual desde la primera vez.
- Si el recurso no existe, algunas APIs lo crean (pero no es recomendable).

**Ejemplo (Flask):**
```python
# Endpoint para actualizar una receta completa por su ID
@app.route("/recetas/<id>", methods=["PUT"])
def actualizar_receta(id):
    receta = Receta.query.get(id)

    #Reemplazar todos los campos obligatorios con los nuevos datos recibidos
    receta.nombre = request.json['nombre']
    receta.ingredientes = request.json['ingredientes']

    db.session.commit()
    return receta_schema.jsonify(receta)
```
Lo que hace paso a paso:

- Recibe el id directamente desde la URL, por ejemplo /recetas/3.
- Busca la receta con ese id en la base de datos.
- Recibe los datos nuevos del body
- Pisa los valores viejos con los nuevos
- Guarda los cambios (commit)
- Devuelve la receta actualizada

La diferencia clave con POST es que acá ya existe el registro, no lo creás sino que lo modificás. En Postman mandarías algo así a /recetas/3:    
```json
{
    "nombre": "Milanesa Napolitana",
    "ingredientes": "carne, pan rallado, huevo, tomate, queso"
}
```


**💡 ¿Y qué pasa con PATCH?– Actualizar parcialmente un recurso**
A diferencia de PUT (que sobrescribe todo el objeto), el método **PATCH** se utiliza para realizar actualizaciones parciales. Si una receta tuviera 20 campos y solo quieres cambiar el tiempo de cocción, usas PATCH para enviar únicamente ese dato específico, dejando el resto intacto.

- No requiere enviar todos los atributos.
- Es útil cuando el recurso es muy grande.


4. **DELETE – Eliminar un recurso**
El método **DELETE** se usa para borrar de forma definitiva un recurso del servidor.

- Puede ser idempotente: La primera vez que borras el recurso con ID 3, se elimina. Si vuelves a mandar el mismo DELETE al ID 3, el servidor te dirá que ya no existe, pero el estado del servidor no cambia (el recurso sigue borrado).
- Generalmente no devuelve datos, solo un código HTTP (204 No Content).

**Ejemplo (Flask):**
```python
# Endpoint para eliminar una receta por su ID
@app.route("/recetas/<id>", methods=["DELETE"])
def eliminar_receta(id):
    receta = Receta.query.get(id)

    db.session.delete(receta)
    db.session.commit()

    # Devolvemos un mensaje de confirmación
    return jsonify({"mensaje": f"La receta con ID {id} fue eliminada con éxito"})
``` 
Lo que hace paso a paso:

- Recibe el ID por la URL, por ejemplo /recetas/3
- Localiza ese registro en la base de datos.
- La elimina de la base de datos
- Guarda los cambios (commit)
- Devuelve un mensaje JSON confirmando la acción. Es el método más limpio, ya que no necesita un cuerpo de datos, solo apuntar al ID correcto.

