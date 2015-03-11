# Encapsulamiento o Abstracción de atributos en la POO en Python

A diferencia de lo que sucede con otros lenguajes orientados a objetos, como pueden ser
Java o C#, en Python no contamos con la definición de atributos como Privado, Protegido
o Público.

En Python, cualquier atributo o método declarado dentro de una clase es, por definición,
de carácter público. Esto provoca que un determinado atributo pueda ser directamente
accesible desde el exterior de la clase.

### Abstracción por convenio

Para tratar de resolvar esta situación, los desarrolladores de Python han llegado al
concenso de que, cualquier atributo y/o método que comience por un guión bajo, deberá
ser reconocido como un elemento privado de la clase y por lo tanto, no se deberá operar
directamente con él. Por ejemplo:

```sh
class MyClass:
  def __init__(self):
    x = 0   # Atributo público.
    _z = 0  # Atributo que se debe entender que es privado. Se accede a él mediante MyClass._z.
```

Dado que este concenso debe ser acatado según la discreción del desarrollador que esté
trabajando con una determinada clase, existe una alternativa para tratar de "aislar" los
atributos privados.

### Abstracción formal mediante "property"

Esta alternativa está compuesta por dos partes:

1. Declarar todos los atributos privados de manera que comiencen con doble guión bajo, es decir,
```sh
    _z = 0  ==>  __z = 0
```
2. Emplear la clase [**property**](https://docs.python.org/3.4/library/functions.html#property Site oficial del proyecto Pytho donde se expone la sintaxis y el uso de la clase property).

Un primer ejemplo se podría ver en el siguiente código (contenido del archivo 01_basic_use_of_property.py)
donde se emplea la clase **property** pero aún no se está utilizando el doble guión bajo:

```sh
class MyClass:
    def __init__(self, x = 0):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "This is the 'x' property")

if __name__ == "__main__":
    object = MyClass()
    print("[RES ] Initial value:", object.x)            # This line returns 0
    print("[INFO] Setting a new value")
    object.x = 78                                       # Using the setter method
    print("[RES ] Getting the new value:", object.x)    # Using the getter method
    print("[RES ] Getting the new value:", object._x)   # Direct access to the "private" attribute
    print("[INFO] Set of attributes:", object.__dict__) # Listing the set of attributes {'_x': 78}
```

Si se ejecuta este código se podrá apreciar que el resultado por consola será similar a este:

```sh
[RES ] Initial value: 0
[INFO] Setting a new value
[RES ] Getting the new value: 78
[RES ] Getting the new value: 78
[INFO] Set of attributes: {'_x': 78}
```

Como se puede observar, mediante el comando ```print("[RES ] Getting the new value:", object._x)```
podemos acceder directamente al atributo que a priori, debería ser privado.

Si modificamos el código anterior para que quede como el siguiente (contenido del archivo 02_advanced_use_of_property.py),

```sh
class MyClass:
    def __init__(self, x = 0):
        self.x = x
        # At the end of the class script, the 'x' attribute which is been
        # used as input parameter, will be turned into a "property" type
        # object.

    # I'm going to declare the '__x' attribute as "private" through
    # two underscores. This operation is going to be dinamically run
    # into the same methods.
    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def del_x(self):
        del self.__x

    x = property(get_x, set_x, del_x, "This is a property")

if __name__ == "__main__":
    object = MyClass()
    print("[RES ] Initial value:", object.x)            # This line returns 0
    print("[INFO] Setting a new value")
    object.x = 78                                       # Using the setter method
    print("[RES ] Getting the new value:", object.x)    # Using the getter method
    # print("[RES ] Getting the new value:", object.__x)  # This line will threw an AttributeError
                                                        # exception because we cannot directly
                                                        # access to a double underscored attribute.
    print("[INFO] Set of attributes:", object.__dict__) # Listing the set of attributes {'_MyClass__x': 78}
```

Lo primero que podemos apreciar es que en el interior de los métodos ```get_x```, ```set_x``` y ```del_x``` estamos declarando el atributo privado mediante **doble guión bajo**.

Si ejecutamos este último código, obtendremos un resultado similar al siguiente:

```sh
[RES ] Initial value: 0
[INFO] Setting a new value
[RES ] Getting the new value: 78
[INFO] Set of attributes: {'_MyClass__x': 78}
```

En este código hay que destacar dos cosas:

La primera de ellas es que la sentencia ```print("[INFO] Set of attributes:", object.__dict__)``` nos
devolverá los atributos que posea la clase. Esto no es nada nuevo pero lo que sí podemos apreciar es que, en
esta ocasión, para poder acceder al atributo privado, deberemos hacerlo mediante la sintaxis: _nombre de la clase__nombre del atributo.

El segundo detalle es que, en base a lo indicado en el párrafo anterior, si tratamos de ejecutar la sentencia
```print("[RES ] Getting the new value:", object.__x)``` vamos a obtener una excepción del tipo
AttributeError con el siguiente resultado:

```sh
Traceback (most recent call last):
  File "D:\Mis Documentos\Tmp\Pruebas Python\property\02_advanced_use_of_property.py", line 28, in <module>
    print("[RES ] Getting the new value:", object.__x)  # This line will threw an AttributeError
AttributeError: 'MyClass' object has no attribute '__x'
```
### Abstracción común mediante "property"

Hay una manera más natural de crear propiedades usando la palabra reservada **@property** de manera
que el código quedaría de la siguiente manera (contenido del archivo 03_common:use_of_property.py):

```sh
class MyClass:
    def __init__(self, x = 0):
        self.x = x
        # At the end of the class script, the 'x' attribute which is been
        # used as input parameter, will be turned into a "property" type
        # object.

    # I'm going to declare the '__x' attribute as "private" through
    # two underscores. This operation is going to be dinamically run
    # into the same methods.
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x

    # The last three methods are equivalent to this one:
    # x = property(get_x, set_x, del_x)

if __name__ == "__main__":
    object = MyClass()
    print("[RES ] Initial value:", object.x)            # This line returns 0
    print("[INFO] Setting a new value")
    object.x = 78                                       # Using the setter method
    print("[RES ] Getting the new value:", object.x)    # Using the getter method
    # print("[RES ] Getting the new value:", object.__x)  # This line will threw an AttributeError
                                                        # exception because we cannot directly
                                                        # access to a double underscored attribute.
    print("[INFO] Set of attributes:", object.__dict__) # Listing the set of attributes {'_MyClass__x': 78}
```

Como se puede apreciar en el código anterior, cuando empleamos **@property**, el método al que está
asociado se convierte directamente en un objeto tipo property y al mismo tiempo, hace las veces de **getter**.

A partir de ese momento, para crear los métodos **setter** y **delete**, lo que haremos será, mediante
@ y el objeto property, usar las declaraciones *.setter* y *.deleter* para definir los correspondiente métodos.
