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

4. [¿Es MongoDB una base de datos SQL o NoSQL?](#4-base-de-datos-mongodb)

5. [¿Qué es una API?](#5-que-es-una-api)

6. [¿Qué es Postman?](#6-postman-el-laboratorio-de-pruebas-de-APIs)

7. [¿Qué es el polimorfismo?](#7-que-es-el-polimorfismo)

8. [¿Qué es un método dunder?](#8-metodo-dunder)

9. [¿Qué es un decorador de python?](#9-decoradores-en-python)



# 1. Clases en Python

Una clase es una plantilla o molde que define cómo se creará un objeto. Permiten empaquetar datos (atributos) y comportamientos (métodos) juntos, lo que facilita la creación de objetos.

## ⚙️ Sintaxis Básica

En Python, definimos una clase usando la palabra reservada class seguida del nombre en mayúscula (CamelCase) y dos puntos (:). Todo lo que pertenece a la clase va indentado (con cuatro espacios) debajo.

## 🔧 ¿Para qué las usamos?

Las usamos principalmente para organizar el código y aplicar un concepto llamado Programación Orientada a Objetos (POO). Sus mayores ventajas son:

- Evitan duplicar código: Defines el comportamiento una sola vez en la clase y lo reutilizas mil veces.

- Organización: Juntan los datos (variables) y las acciones (funciones) en un solo lugar lógico.

- Modelar el mundo real: Hacen que el código sea más fácil de entender porque programamos pensando en "cosas" (usuarios, productos, enemigos, facturas) en lugar de solo líneas de texto sueltas.

## 📋 Conceptos Claves

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

# 2. Métodos en Python

El método que se ejecuta automáticamente cuando se crea una instancia de una clase es __init__ (abreviación de initialize o inicializar en inglés). En el mundo de la programación, a este tipo de funciones especiales se les conoce como "Constructores".

## 🔧 ¿Para qué se utiliza?

Su función principal es inicializar los atributos y preparar el estado inicial del objeto.

Imagínate que la clase es el molde para fabricar teléfonos móviles. No queremos que todos los teléfonos salgan de la fábrica vacíos; necesitamos que cada uno tenga su propio número de serie, color y modelo desde el momento en que se fabrican.

El método __init__ se utiliza para:

- Darle vida al objeto con datos iniciales: Configura las características únicas de cada instancia en el segundo exacto en que nace.

- Automatizar procesos: Evita tener que crear el objeto vacío y luego escribir líneas de código extra para asignarle cada dato uno por uno.

⚙️ Sintaxis y Estructura
En Python, este método se reconoce porque lleva dos guiones bajos antes y dos después (__init__). Esto le indica a Python que es un método especial ("método mágico") con un comportamiento interno propio.

## Sintaxis
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


# 3. Verbos de APIs en Python

Las APIs REST son fundamentales en el desarrollo de software moderno. Para interactuar con ellas, utilizamos los **verbos HTTP**, que permiten definir el tipo de acción que queremos realizar sobre los recursos de la API.

## ¿Qué son los verbos HTTP?
 
Los verbos HTTP (también llamados métodos HTTP) indican la acción que se desea realizar sobre un recurso en una API. En una API REST, los recursos suelen representarse como URLs.
Por ejemplo, en una API que gestiona recetas de cocina, el recurso principal sería:

https://api.ejemplo.com/recetas

Los verbos HTTP nos permiten:

- Obtener información (GET)
- Crear un nuevo recurso (POST)
- Actualizar un recurso existente (PUT o PATCH)
- Eliminar un recurso (DELETE)

## Verbos HTTP más utilizados en APIs REST

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


# 4. Base de datos MongoDB
---
## ¿Qué es MongoDB?

**MongoDB** es una base de datos **no relacional** (también llamada **NoSQL**), y más concretamente del tipo **orientada a documentos**. 
> En lugar de guardar los datos en tablas con filas y columnas, los guarda en **documentos** con formato similar a JSON, llamados BSON.

## ¿Cómo funciona MongoDB?##

Para entenderlo, pensá en cómo guardás la información en carpetas de tu ordenador usando archivos de texto editables.

MongoDB utiliza el formato BSON (que es una versión binaria de JSON, el estándar de la web). Si alguna vez has visto un JSON, se estructura con pares de clave: valor.

### Jerarquía básica
 
| Concepto | Equivalente en SQL | Descripción |
|---|---|---|
| **Documento** | Fila | El registro individual |
| **Colección** | Tabla | El grupo donde se guardan los documentos |

Así se vería un documento:
```json
{
  "_id": "64f1a2b3c4d5e6f7a8b9c012",
  "nombre": "Carlos",
  "edad": 28,
  "hobbies": ["fútbol", "videojuegos"],
  "direccion": {
    "ciudad": "Madrid",
    "pais": "España"
  }
}
```
> 💡 Fijate que el documento puede tener **listas**, **objetos anidados** y campos distintos entre documentos. No hay una estructura rígida obligatoria.


---
 
## Características principales

- **🔓 Esquema flexible** - Cada documento puede tener campos diferentes. No estás obligado a seguir una estructura rígida, lo que facilita la evolución de tu aplicación.
- **⚡ Alto rendimiento y escalabilidad** - Está diseñada para manejar grandes volúmenes de información y cargas de trabajo masivas.
- **🔎 Lenguaje de consultas enriquecido** - A pesar de ser no relacional, permite realizar consultas complejas, filtrado y agregación de datos.
- **🚀 Baja latencia** - Ideal para aplicaciones web, móviles, e-commerce y redes sociales que requieren respuestas en tiempo real.

## La gran batalla: SQL vs. NoSQL

Para entender por qué existe MongoDB, hay que compararlo con el modelo tradicional (SQL).

### Bases de Datos SQL (Relacionales)

> Son las de toda la vida: **MySQL**, **PostgreSQL** o **SQL Server**.

- **Cómo funcionan:** Organizan los datos en tablas con filas y columnas fijas. Las tablas se "relacionan" entre sí mediante llaves o identificadores.
- **Su punto fuerte:** Son increíblemente organizadas y seguras para transacciones complejas (como un sistema bancario).
- **Su talón de Aquiles:** Son inflexibles. Añadir una nueva columna a una tabla con millones de registros puede convertirse en un problema serio.
---

### Bases de datos NoSQL (No Relacionales)

> Aquí es donde entra **MongoDB**. Nacieron para resolver los problemas de rigidez y escalabilidad de la era de internet.
 
- **Cómo funcionan:** No usan tablas. Pueden usar documentos (como MongoDB), grafos, o sistemas clave-valor.
- **Su punto fuerte:** Son **flexibles** y escalan **horizontalmente** sin fricción —es muy fácil repartir los datos en muchos servidores si tu aplicación crece de golpe—.
---

### Comparativa rápida
 
| | **SQL (Relacional)** | **NoSQL (No Relacional)** |
|---|---|---|
| **Ejemplos** | MySQL, PostgreSQL | MongoDB, Redis, Cassandra |
| **Estructura** | Tablas con filas y columnas | Documentos, clave-valor, grafos… |
| **Esquema** | Fijo, definido antes de usar | Flexible, puede cambiar |
| **Relaciones** | JOINs entre tablas | Datos anidados o referencias |
| **Escalado** | Vertical (más potencia al servidor) | Horizontal (más servidores) |
| **Ideal para** | Datos muy estructurados y relacionados | Datos variables, gran volumen, velocidad |
 
---

## ¿Cuándo usar cada una?
 
**✅ Usá SQL cuando:**
- Los datos tienen muchas relaciones entre sí (ej. pedidos → clientes → productos)
- Necesitás consistencia y transacciones seguras (banca, contabilidad)
**✅ Usá MongoDB cuando:**
- Los datos cambian de estructura frecuentemente
- Necesitás escalar rápido con mucho volumen (redes sociales, catálogos)
- Los datos se leen más de lo que se relacionan entre sí
---
 
> **En resumen:** MongoDB te da **flexibilidad y velocidad** a cambio de renunciar a la rigidez estructurada del mundo relacional. Ninguna es mejor en absoluto — depende del problema que quieras resolver.

---

# 5. ¿Qué es una API?

Una API (por sus siglas en inglés, Application Programming Interface) o Interfaz de Programación de Aplicaciones, es un conjunto de reglas que permite que diferentes programas o aplicaciones se comuniquen entre sí. Actúa como un **puente o intermediario**, permitiendo que un sistema solicite datos o funciones a otro de forma automática y segura.

## La analogía del restaurante 🍽️
Imaginá que estás en un restaurante:

- Vos sos la aplicación que quiere algo (el cliente).
- La cocina es el sistema que tiene lo que necesitás (el servidor / base de datos).
- El camarero es la API — el intermediario que lleva tu pedido, lo comunica a la cocina, y trae la respuesta de vuelta.

💡 Vos nunca entrás a la cocina. No sabés cómo funciona por dentro. Solo le decís al camarero qué querés, y él se encarga del resto.

### 📱 ¿Cómo funciona en la práctica?
Cuando abrís una app del tiempo y ves la temperatura de tu ciudad, esto es lo que ocurre por detrás:

- ➡️ Tu app le manda una petición (**request**) a una API → "Dame el clima de Bilbao". 
- 🔎 La API busca esa información en su servidor
- ⬅️ La API te devuelve una respuesta (**response**) → generalmente en formato JSON

```json
{
  "ciudad": "Bilbao",
  "temperatura": 18,
  "estado": "lluvia"
}
```

### ¿Por qué son tan importantes para un programador?

Las APIs son los bloques de construcción del software moderno por tres razones principales:

- **No reinventas la rueda:** Si estás creando una app de reparto de comida, no vas a programar un mapa desde cero. Usas la API de Google Maps.

- **Seguridad:** Permiten compartir funciones o datos sin enseñar cómo está hecho tu código por dentro ni exponer tu base de datos directamente al público.

- **Separación de tareas:** Permiten que el equipo de Frontend (los que hacen la interfaz visual en React, HTML, etc.) trabaje de forma independiente al equipo de Backend (los que programan la lógica y las bases de datos en Flask, Node.js, etc.). Ambos mundos se unen gracias a la API.

### 📌 En Resumen

Una API es una herramienta que te permite conectar sistemas, usar herramientas de otros creadores en tu propia aplicación, y estructurar tu código de forma limpia y profesional.


# 6. Postman: el laboratorio de pruebas de APIs

**Postman** es, sin duda, la herramienta estrella para cualquiera que trabaje desarrollando o consumiendo APIs. Si estás construyendo tu propio backend o necesitas usar datos de un servicio externo, Postman va a ser tu mejor amigo. 

💡Importante: Es **gratuito** y se descarga como **aplicación de escritorio**.

## ¿Qué es Postman? 

**Postman** es una herramienta visual que te permite probar APIs sin necesidad de escribir código. Funciona como un laboratorio de pruebas para APIs.

Imaginá que estás programando el backend de tu aplicación con Python y Flask, y creas una ruta para que los usuarios puedan registrarse. En una situación normal, para probar si esa ruta funciona, tendrías que programar también la pantalla del frontend (el formulario en HTML/CSS), escribir los datos, hacer clic en el botón y ver qué pasa.

Postman existe para evitarte todo ese trabajo. Te permite simular ser el frontend y enviar peticiones directas a tu backend para comprobar si responde correctamente.

## ¿Para qué sirve? (Sus 3 usos principales)

- 💉 **Probar APIs (Testing)**
Te permite enviar peticiones (`requests`) a cualquier URL y analizar minuciosamente la respuesta (`response`). Puedes ver qué datos te devuelve, en qué formato (generalmente JSON), cuánto tarda en responder y si el código de estado es el correcto (como un 200 OK o un 404 Not Found).

- 🔧 **Diseñar y Desarrollar APIs**
Mientras estás escribiendo el código de tu servidor, utilizas Postman para asegurarte de que cada "ruta" o endpoint hace exactamente lo que querés antes de conectarla con la interfaz visual.

- 📁 **Documentar y Organizar (Colecciones)**
Postman te permite guardar tus peticiones en carpetas llamadas Collections (Colecciones). Si tu aplicación tiene 20 rutas diferentes (para usuarios, para productos, para el carrito), podés guardarlas todas organizadas. Incluso podés compartir esa colección con otros programadores para que sepan cómo usar tu API.

## ¿Cómo funciona Postman?

El funcionamiento de Postman replica exactamente el flujo de Petición ➡️ Respuesta que viste al estudiar las APIs, pero ofreciéndote una interfaz gráfica muy cómoda.

### Veamos cómo se ve en la práctica:

Para este ejemplo haremos una búsqueda del siguiente link de muestra que nos ofrece la plataforma web: https://postman-echo.com/get

Para probarlo tú mismo, realizaremos los siguientes pasos:

- Selecciona el método **GET** en el menú desplegable que se encuentra a la izquierda de la barra de búsqueda.

- Coloca la URL de prueba (https://postman-echo.com/get) en el panel de búsqueda superior.

- Presiona el botón azul **Send** ubicado a la derecha.

💡 Tip: Si deseas guardar esta configuración para no tener que escribirla de nuevo en el futuro, puedes presionar el botón **Save** que se encuentra en la parte superior derecha.

![request](img/image.png)

**Analizando la Respuesta**

Una vez que presionas Send, la mitad inferior de Postman cobrará vida y te mostrará el resultado del servidor. En esa zona deberás buscar tres datos fundamentales:

- El **JSON de respuesta** (con colores y sangrías para que se lea fácil).

- El **Status Code** (el número que indica si todo salió bien o hubo un error).

- El **Tiempo de respuesta** (útil para ver si tu base de datos o tu código están yendo lentos).

![response](img/image-1.png)

### 📌 La Analogía Final

Si dijimos que una API es el camarero de un restaurante que lleva los pedidos de la mesa a la cocina...

Postman es un cliente de pruebas experto. Es una persona que se sienta en la mesa con un cuaderno, le pide cosas rarísimas al camarero de todas las formas posibles (le pide platos sin sal, menús de postres, intenta pedir cosas que no están en la carta) para comprobar si el camarero hace bien su trabajo y si la cocina responde correctamente a cada situación.

## En resumen: 

**Postman** es el entorno de pruebas de las APIs. Así como usás el navegador para probar una web, usás Postman para probar una API.

