import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

kinesticoAPI = Blueprint('kinestico', __name__)

@kinesticoAPI.route('/list/kinestesico')
def tiposdatos():
    try:
        urlYoutube = [
            {
                "temas": "Variables y Tipos de datos",
                "contenido": [
                    {
                        "titulo": "Variables y Tipos de datos",
                        "url": "Variables <br/> ¿Qué es? <br> Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal, a la cual podremos acceder y modificar en cualquier momento que lo necesitemos en el tiempo de ejecución de nuestro código. <br> ¿Cómo declarar una variable en python? <br> Declarar una variable en Python es muy sencillo, solo falta con poner el nombre de nuestra variable seguido de un signo de igualdad (=), y al finalizar asignarle un valor a la misma. <br> Ejemplo: <br> Guardamos en la variable suma el resultado de la operación 1 + 2 <br> suma = 1 + 2 <br> Datos primitivos simples y compuesto <br> Los tipos de datos primitivos y compuestos en python son las estructuras de datos elementales del lenguaje de programación. Son los componentes básicos para tratar todo tipo de datos o variables y contienen valores de datos puros y simples. <br> Tipos de datos primitivos simples <br> Números (numbers): Secuencia de dígitos (pueden incluir el - para negativos y el . para decimales) que representan números. <br>Ejemplo. 0, -1, 3.1415. <br> Cadenas (strings): Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas simples o dobles. <br>Ejemplo. ‘Hola’, “Adiós”. <br> Booleanos (boolean): Contiene únicamente dos elementos True y False que representan los valores lógicos verdadero y falso respectivamente. <br>Estos datos son inmutables, es decir, su valor es constante y no puede cambiar. <br>Tipos de datos primitivos compuestos (contenedores) <br>Listas (lists): Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. Se representan con corchetes y los elementos se separan por comas. <br> Ejemplo. [1, “dos”, [3, 4], True]. <br> Tuplas (tuples). Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. A diferencia de las listas son inmutables, es decir, que no cambian durante la ejecución. Se representan mediante paréntesis y los elementos se separan por comas. <br>Ejemplo. (1, ‘dos’, 3) <br> Diccionarios (dictionaries): Colecciones de objetos con una clave asociada. Se representan con llaves, los pares separados por comas y cada par contiene una clave y un objeto asociado separados por dos puntos. <br>Ejemplo. {‘pi’:3.1416, ’e’:2.718}."
                    }
                ]
            },
            {
                "temas": "Estructuras de decisión",
                "contenido": [
                    {
                        "titulo": "Estructuras de decisión - Sentencia If",
                        "url": "Estructura de decisión /nUna estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados, dependiendo de la condición o condiciones presentes en la estructura de decisión. /nSentencia if /n Una sentencia if en Python evalúa una condición y si esta resulta ser verdadera (True), entonces ejecuta una vez el código en la expresión. Si sucede el caso contrario y la expresión es falsa, entonces No ejecutes el código que sigue. /nLa sintaxis general para la sentencia if  es la siguiente /nif condicion: /n ejecutar sentencia /nOperadores de comparación /nAhora bien, antes de dar un ejemplo de manera formal debemos hablar de los operadores de comparación, estos se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False /nEn Python tenemos los siguientes operadores de comparación  /n<img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/Operadores%20de%20comparacion%20.png?alt=media&token=739589ed-ac95-40e9-9831-dd3767aab0ab'>/next(Ejemplos de sentencia if con operadores de comparación /nEjemplo 1: /nif 2<3: /n print(“2 es menor que 3”) /nEjemplo 2: /nif 2<=2: /n     print(“2 es menor o igual que 2”) /nEjemplo 3: /nif 22>20: /n  print(“23  es mayor que 20”) /nEjemplo 4: /nif 22>=22: /n     print(“22 es mayor o igual que 2”) /nEjemplo 5: /nif 45==45: /n     print(“45 es igual que 45”) /nEjemplo 6: /nif 45 ¡= 50: /n     print(“45 es diferente que 50”) /n)",
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....else",
                        "url": "Variables/n ¿Qué es? /n Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal, a la cual podremos acceder y modificar en cualquier momento que lo necesitemos en el tiempo de ejecución de nuestro código. /n ¿Cómo declarar una variable en python? /n Declarar una variable en Python es muy sencillo, solo falta con poner el nombre de nuestra variable seguido de un signo de igualdad (=), y al finalizar asignarle un valor a la misma. /n Ejemplo: /n Guardamos en la variable suma el resultado de la operación 1 + 2 /n suma = 1 + 2 /n Datos primitivos simples y compuesto /n Los tipos de datos primitivos y compuestos en python son las estructuras de datos elementales del lenguaje de programación. Son los componentes básicos para tratar todo tipo de datos o variables y contienen valores de datos puros y simples. /n Tipos de datos primitivos simples /n Números (numbers): Secuencia de dígitos (pueden incluir el - para negativos y el . para decimales) que representan números. /nEjemplo. 0, -1, 3.1415. /n Cadenas (strings): Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas simples o dobles. /nEjemplo. ‘Hola’, “Adiós”. /n Booleanos (boolean): Contiene únicamente dos elementos True y False que representan los valores lógicos verdadero y falso respectivamente. /nEstos datos son inmutables, es decir, su valor es constante y no puede cambiar. /nTipos de datos primitivos compuestos (contenedores) /nListas (lists): Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. Se representan con corchetes y los elementos se separan por comas. /n Ejemplo. [1, “dos”, [3, 4], True]. /n Tuplas (tuples). Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. A diferencia de las listas son inmutables, es decir, que no cambian durante la ejecución. Se representan mediante paréntesis y los elementos se separan por comas. /nEjemplo. (1, ‘dos’, 3) /n Diccionarios (dictionaries): Colecciones de objetos con una clave asociada. Se representan con llaves, los pares separados por comas y cada par contiene una clave y un objeto asociado separados por dos puntos. /nEjemplo. {‘pi’:3.1416, ’e’:2.718}."
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....elif.....else",
                        "url": "Estructura de decisión /nSentencia if…else/nCómo mencionamos, una sentencia if ejecuta el código, solo en caso de cumplirse la condición, pero ¿qué sucede si queremos ejecutar un código alternativo en caso de no cumplirse la condición? Es en este caso es necesario usar una sentencia if..else. La cual nos permite que cuando la expresión if se evalúa como True, entonces ejecuta el código que le sigue. Pero si se evalúa como False, entonces ejecuta el código que sigue después de la sentencia else. La sentencia else está escrita en una nueva línea, posterior a la última línea del código indentado, y no puede ser escrita por sí misma. Una sentencia else tiene como prerrequisito una sentencia if, siendo a la vez, parte de él. /nLa sintaxis de una sentencia if..else es parecida a la siguiente: /nif condicion: /n ejecutar codigo si la condicion es True/nelse: /nejecutar codigo si la condicion es False/nEjemplo de sentencia if….else /nNos piden un programa el cual permita determinar si una persona es mayor edad/nedadMin = 18/nprint(“Ingrese su edad”) /nedadCustomer = int(input())/nif edadCustomer >= edadMin : /nprint(“Es mayor de edad”) /nelse: /nprint(“Es menor de edad”) /nAl momento de ejecutar este código puede ocurrir 2 casos, en el caso de que la sentencia if sea verdadera se nos imprimirá en pantalla el mensaje de “Es mayor de edad” y en el caso de que la edad no sea la mínima se imprimirá en pantalla “Es menor de edad”. /n"
                    },
                    {
                        "titulo": "Estructuras de decisión - if ternario",
                        "url": "Estructura de decisión /nIf ternario /nEl operador ternario en Python, al igual que en otros lenguajes, tiene la finalidad de hacer más compacta una condición If, permitiendo generar código condicionado en una sola línea y aunque no es ampliamente usado sí que tiene sus ventajas. /nLa sintaxis de if ternario/ncondition_if_true if condition else condition_if_false/nesta sintaxis de if ternario tiene una particularidad y es que primero escribimos las instrucciones que se ejecutaran si nuestra condición es verdadera, seguido de la sentencia if y nuestra condición, luego pondremos nuestra sentencia else seguido de las instrucciones que se ejecutaran en el caso que if sea falso. /nejemplo de if ternario/nes_bonito = True/nprint('Es bonito')  if es_bonito else print('No es bonito')/nresultado /n“Es bonito” /nComo se puede ver, permiten verificar de manera rápida una condición, y lo mejor de todo es que se puede hacer en una sola línea de código. Por lo general hacen que el código sea más compacto y fácil de leer. /nOtra forma un tanto extraña y no demasiado usada es la siguiente forma: /nLa sintaxis de if ternario 2/n(if_test_is_false, if_test_is_true)[test] /nejemplo de if ternario 2/nes_bonito = True/napariencia = ('Feo', 'Bonito')[es_bonito] /nretultado/nprint('El gato es', apariencia) /nEste ejemplo funciona ya que True=1 y False=0, y puede ser usado también con listas. Es importante decir también que este ejemplo no es muy usado."
                    },
                ]
            },            
            {
                "temas": "Estructuras iterativas",
                "contenido": [
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 1",
                        "url": "Estructuras iterativas /nBucle while loop/n A diferencia de las estructuras de decisión, las iterativas nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición. /nwhile loop repite la secuencia de acciones muchas veces hasta que alguna condición se evalúa como False. La condición se da antes del cuerpo del bucle y se comprueba antes de cada ejecución del cuerpo del bucle. Típicamente, el while se utiliza bucle cuando es imposible para determinar el número exacto de iteraciones del bucle de antemano. /nEstructura de while loop /nwhile some condition: /n    a block of statements/nEjemplo de while loop/nanio = 2001 /nwhile anio <= 2012: /n    print ('Informes del Año', anio) /n    anio += 1/nResultado/nInformes del año 2001 /nInformes del año 2002 /nInformes del año 2003 /nInformes del año 2004 /nInformes del año 2005 /nInformes del año 2006 /nInformes del año 2007 /nInformes del año 2008 /nInformes del año 2009 /nInformes del año 2010 /nInformes del año 2011 /nInformes del año 2012/nSi miramos la última línea: /nanio += 1/nse puede notar que en cada iteración, incrementamos el valor de la variable que condiciona el bucle (anio). Si no lo hiciéramos, esta variable siempre sería igual a 2001 y el bucle se ejecutaría de forma infinita, ya que la condición (anio <= 2012) siempre se estaría cumpliendo."
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 2",
                        "url": "Estructuras iterativas/nBucle while loop uso de break y continue/nbreak/n¿Qué sucede si el valor que condiciona la iteración no es numérico y no puede incrementarse? En ese caso, podremos utilizar una estructura de control condicional, anidada dentro del bucle, y frenar la ejecución cuando el condicional deje de cumplirse, con la palabra clave reservada break: /nwhile True: /n    nombre = raw_input('Indique su nombre: ')/n   if nombre: /n        break/n El bucle anterior, incluye un condicional anidado que verifica si la variable nombre es verdadera (solo será verdadera si el usuario tipea un texto en pantalla cuando el nombre le es solicitado). Si es verdadera, el bucle para (break). Si no, seguirá ejecutándose hasta que el usuario, ingrese un texto en pantalla. /nContinue/n La instrucción Continue en Python devuelve la ejecución al comienzo del ciclo while. La declaración de Continue rechaza todas las declaraciones restantes en la iteración actual del bucle y mueve el control de nuevo a la parte superior del bucle. /nEjemplo de continue en ciclo while loop/nvar = 10 /nwhile var > 0: /n   var = var -1/n   if var == 5: /n      continue/n   print ('valor de la variable:', var) /nResultado/nvalor de la variable :10/nvalor de la variable: 9/nvalor de la variable: 8/nvalor de la variable: 7/nvalor de la variable: 6/nvalor de la variable: 4 /nvalor de la variable: 3/nvalor de la variable: 2/nvalor de la variable: 1/n"
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop",
                        "url": "Estructuras iterativas/nBucle foor loop/nEl ciclo for loop en Python se usa para iterar sobre una secuencia ( lista , tupla , cadena ) u otros objetos iterables. La iteración sobre una secuencia se llama recorrido. /nEstructura de bucle foor loop/nfor val in sequence: /n    loop body/nAquí val es la variable que toma el valor del elemento dentro de la secuencia en cada iteración. El bucle continúa hasta que llegamos al último elemento de la secuencia. El cuerpo del bucle for se separa del resto del código mediante sangría. /nEjemplos de bucle foor loop/nnumbers = [6, 5, 3, 8, 4, 2, 5, 4, 11] /nsum = 0/nfor val in numbers: /n    sum = sum+val/nprint('El total de la suma es', sum) /nResultado/nla suma es 48/n"              
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop range()",
                        "url": "Estructuras iterativas /nBucle foor loop uso de función range()/nPodemos generar una secuencia de números usando range()la función. range(10)generará números del 0 al 9 (10 números). También podemos definir el tamaño de inicio, parada y paso como range(start, stop,step_size). step_size por defecto es 1 si no se proporciona. Esta función no almacena todos los valores en la memoria; sería ineficiente. Por lo tanto, recuerda el inicio, la parada, el tamaño del paso y genera el siguiente número sobre la marcha. /nPodemos usar la función range()en bucles  for para iterar a través de una secuencia de números. Se puede combinar con la función len() para iterar a través de una secuencia usando la indexación. Aquí hay un ejemplo. /nEjemplo de for loop con función range()/ngenre = ['pop', 'rock', 'jazz'] /nfor i in range(len(genre)): /n    print(´'Me gusta el ', genre[i]) /nResultado /nMe gusta el pop/nMe gusta el rock/nMe gusta el jazz/n"
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop anidados",
                        "url": "Estructuras iterativas/nBucle foor loop anidado/nSe habla de bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque. Al bucle que se encuentra dentro del otro se le puede denominar bucle interior o bucle interno. El otro bucle sería el bucle exterior o bucle externo. Los bucles pueden tener cualquier nivel de anidamiento (un bucle dentro de otro bucle dentro de un tercero, etc.). /nBucle foor loop anidado (variables independientes) /nSe dice que las variables de los bucles son independientes cuando los valores que toma la variable de control del bucle interno no dependen del valor de la variable de control del bucle externo. /nEjemplo de bucle foor loop 1/nfor i in [0, 1, 2]: /n    for j in [0, 1]: /n        print(f'i vale {i} y j vale {j}')/nresultado/ni vale 0 y j vale 0/ni vale 0 y j vale 1/ni vale 1 y j vale 0/ni vale 1 y j vale 1/ni vale 2 y j vale 0/ni vale 2 y j vale 1/nEn el ejemplo anterior, el bucle externo (el controlado por i) se ejecuta 3 veces y el bucle interno (el controlado por j) se ejecuta dos veces por cada valor de i. Por ello la instrucción print() se ejecuta en total 6 veces (3 veces que se ejecuta el bucle externo x 2 veces que se ejecuta cada vez el bucle interno = 6 veces). En general, el número de veces que se ejecuta el bloque de instrucciones del bucle interno es el producto de las veces que se ejecuta cada bucle. /nEjemplo de bucle foor loop 2/nfactoresX = [1,2,3,4,5] /nfactoresY = [1,2,3,4,5] /nfor factorX in factoresX: /n  for factorY in factoresY: /nprint(f'{factorX} x {factorY} = {factorX * factorY}')/nresultado /n1 x 1 = 1/n1 x 2 = 2/n1 x 3 = 3/n1 x 4 = 4/n1 x 5 = 5/n2 x 1 = 2/n2 x 2 = 4/n2 x 3 = 6/n2 x 4 = 8/n2 x 5 = 10/n3 x 1 = 3/n3 x 2 = 6/n3 x 3 = 9/n3 x 4 = 12/n3 x 5 = 15/n4 x 1 = 4/n4 x 2 = 8/n4 x 3 = 12/n4 x 4 = 16/n4 x 5 = 20/n5 x 1 = 5/n5 x 2 = 10/n5 x 3 = 15/n5 x 4 = 20/n5 x 5 = 25/n"
                    },
                ]
            },
            {
                "temas": "Funciones iterativas",
                "contenido": [
                    {
                        "titulo": "Funciones iterativas - Definición de función",
                        "url": "Funciones /nDefinición de funciones en Python /nLas funciones son bloques de código que se pueden reutilizar simplemente llamando a la función. Esto permite la reutilización de código simple y elegante sin volver a escribir explícitamente secciones de código. Esto hace que el código sea más legible, facilita la depuración y limita los errores de escritura. /nEstructura de una función/ndef functionName(): /n    code block/nEjemplo/ndef saludo():/n	print(“hola mundo”) /nsaludo()/nResultado /nhola mundo"
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función",
                        "url": "Funciones /nArgumentos en funciones /nUn argumento es un valor que la función espera recibir cuando sea llamada, a fin de ejecutar acciones en base al mismo. Una función puede esperar uno o más parámetros, los cuales irán separados por una coma. /nEjemplo Argumentos 1/ndef saludo(nombre, apellido): /n    print(f'hola {nombre} {apellido}')/nsaludo('steven', 'otalvaro') /nResultado /nHola Steven otalvaro/nAhora bien, podemos setear los valores de los parámetros con el fin que el orden no importe, y de esta manera cuando nuestra función reciba los argumentos, los reciba de manera correcta, en el ejemplo anterior vimos como pasar argumentos a la función, ahora lo que haremos será setear los parámetros cuando se envían en la función y para esto, lo que deberos hacer es ponerle a cada nombre del parámetro el valor que este tendrá/nEjemplo/ndef saludo(nombre, apellido): /n    print(f'hola {nombre} {apellido}')/nsaludo(apellido='otalvaro', nombre='steven') /nResultado /nHola Steven otalvaro/nVemos que cuando llamamos a la función le indicamos el valor que tendrá cada argumento y de esta manera el orden de los argumentos no importará. /n"
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función de tipo args y kwargs",
                        "url": "Funciones/nArgumentos args y kwargs/nExisten dos tipos de argumentos en Python, los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. Encontrar un término en el español para estos últimos resulta algo complejo, equivaldría a argumentos de palabras clave, así que simplemente los llamaremos por su nombre original. /nUna de las principales diferencias entre los dos tipos de argumentos, como observamos anteriormente, es que los convencionales son posicionales, mientras que en los keyword arguments su ubicación es indistinta. /nEjemplo de args/ndef suma(*args): /n    resultado = 0/n    for num in args: /n        resultado += num/n    print(resultado) /nsuma(1, 2, 3) /nResultado /n6/nEjemplo de kwargs/ndef concatenacion(**kwargs): /n    resultado = ""/n    for arg in kwargs.values():/n        resultado += ' ' + arg/n    print(resultado)concatenacion(a='python', b='es', c='un', d='lenguaje', e='de',f='programacion')/nResultado/npython es un lenguaje de programacion",
                    }
                    ,
                    {
                        "titulo": "Funciones iterativas - uso de return",
                        "url": "Funciones /nReturn /n Se utiliza una declaración de return para finalizar la ejecución de la llamada de función y devuelve el resultado (el valor de la expresión que sigue a la palabra clave return) . Las sentencias posteriores a las sentencias de retorno no se ejecutan. Si la declaración de devolución no tiene ninguna expresión, se devuelve el valor especial Ninguno. Una declaración de retorno se usa en general para invocar una función para que las declaraciones pasadas puedan ejecutarse. /nSyntax: /ndef fun():/n    statements/n    return [expression] /nejemplo /ndef suma(*args): /n	resultado = 0/n 	for num in args: /n		resultado += num/n	return resultado/nprint(suma(1,2,3,4,5,6))",
                    }
                ]
            },
        ]
        return jsonify(urlYoutube), 200
    except Exception as e:
        return f"an error ocurred : {e}"