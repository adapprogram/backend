from flask import Blueprint, jsonify

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
                        "url": "Variables <br><br><h2 className='subtitle'>¿Qué es?</h2><br>Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal, a la cual podremos acceder y modificar en cualquier momento que lo necesitemos en el tiempo de ejecución de nuestro código. <br><br><h2 className='subtitle'>¿Cómo declaramos una variable en Python?</h2><br>Declarar una variable en Python es muy sencillo, solo falta con poner el nombre de nuestra variable seguido de un signo de igualdad (=), y al finalizar asignarle un valor a la misma. <br><br><h2 className='subtitle'> Sintaxis</h2><br>nombreVariable = valor<br>Ejemplo: <br>Guardaremos en la variable suma el resultado de la operación 1 + 2. <br>suma = 1 + 2<br>en esta variable se nos quedara almacenado el valor de 3. <br><br><h2 className='subtitle'> Datos primitivos simples y compuesto</h2><br>Los tipos de datos primitivos y compuestos en python son las estructuras de datos elementales del lenguaje de programación. Son los componentes básicos para tratar todo tipo de datos o variables y contienen valores de datos puros y simples. <br> <ul><h2 className='subtitle'>Tipos de datos primitivos simples</h2><br><li className='subtitle__list'> <strong>Números</strong> (numbers): Secuencia de dígitos (pueden incluir el - para negativos y el . para decimales) que representan números. <br><strong> Ejemplo </strong> . 0, -1, 3.1415.</li><br> <li className='subtitle__list'><strong>Cadenas</strong>(strings): Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas simples o dobles.<br><strong> Ejemplo </strong> <br>‘Hola’, “Adiós”. </li><br><li className='subtitle__list'><strong> Booleanos </strong> (boolean): Contiene únicamente dos elementos True y False que representan los valores lógicos verdadero y falso respectivamente.</li></ul>.<ul><h2 className='subtitle'>Tipos de datos primitivos compuestos</h2><br><li className='subtitle__list'><strong>Listas</strong> (lists): Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. Se representan con corchetes y los elementos se separan por comas. <br><strong> Ejemplo </strong> <br> [1, “dos”, [3, 4], True]. </li><br><li className='subtitle__list'><strong> Tuplas  </strong> (tuples). Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. A diferencia de las listas son inmutables, es decir, que no cambian durante la ejecución. Se representan mediante paréntesis y los elementos se separan por comas. <br><strong> Ejemplo </strong><br>  (1, ‘dos’, 3).</li><br><li className='subtitle__list'><strong>Diccionarios </strong>  (dictionaries): Colecciones de objetos con una clave asociada. Se representan con llaves, los pares separados por comas y cada par contiene una clave y un objeto asociado separados por dos puntos.<br><strong> Ejemplo </strong><br> {‘pi’:3.1416, ’e’:2.718}. </li></ul>",
                        "question": ""
                    }
                ]
            },
            {
                "temas": "Estructuras de decisión",
                "contenido": [
                    {
                        "titulo": "Estructuras de decisión - Sentencia If",
                        "url": "Estructura de decisión <br>Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados, dependiendo de la condición o condiciones presentes en la estructura de decisión.<h2 className='subtitle'> Sentencia if</h2><br>Una sentencia if en Python evalúa una condición y si esta resulta ser verdadera (True), entonces ejecuta una vez el código en la expresión. Si sucede el caso contrario y la expresión es falsa, entonces no se ejecutará el código que sigue. <br>La sintaxis general para la sentencia if es la siguiente<br>if condicion: <br>    ejecutar sentencia<br><h2 className='subtitle'> Operadores de comparación</h2><br>Ahora bien, antes de dar un ejemplo de manera formal debemos hablar de los operadores de comparación, estos se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False. <br>En Python tenemos los siguientes operadores de comparación. <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/operadoresDeComparacion.png?alt=media&token=c8072ebc-1899-4dbd-831a-6dd65dcef767'><br><h2 className='subtitle'> Ejemplos de sentencia if con operadores de comparación </h2><br>Ya hemos explicado lo que son los operadores de comparación, ahora veamos un par de ejemplo haciendo uso de los diferentes operadores. <br><strong> Ejemplo 1: </strong> <img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo1.png?alt=media&token=ff5cfeb9-0269-48ea-82f8-3c921ea12e93'><strong> Ejemplo 2: </strong> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo2.png?alt=media&token=8716ae06-01cd-431d-9904-e548fa72a7cc'><br><strong> Ejemplo 3: </strong> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo3.png?alt=media&token=43e2415d-57ec-4cfe-a6ca-865853cb4906'><br><strong> Ejemplo 4: </strong> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo4.png?alt=media&token=824b3a6f-9170-405d-b228-a13dc244dfe9 '><br><strong> Ejemplo 5: </strong> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo5.png?alt=media&token=e8ce06aa-47a6-473b-a5e1-ee76fcc72ca8'><br><strong> Ejemplo 6: </strong> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/ejemplo6.png?alt=media&token=3c3386aa-c351-4d82-8e1c-95e3e425893e'><br>Como podemos observar los operadores nos van a ser de suma ayuda para cuando necesitemos comparar datos.",
                        "question": "Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de 12 años.<br>Entrada, estos valores deben estar escritos en el código de python <br>Edad= 14<br>Salida, este debe ser el mensaje que retorne la solución <br>Es mayor de 12 años",

                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....else",
                        "url": "Estructura de decisión <br><br><h2 className='subtitle'> Sentencia if…else </h2><br>La estructura de control if ... else ... permite que un programa ejecute unas instrucciones cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición. En inglés 'if' significa 'si' (condición) y 'else' significa 'si no'. <br><h2 className='subtitle'>La sintaxis de una sentencia if..else  </h2><br>if condicion: <br>    ejecutar codigo si la condicion es True<br>else: <br>     ejecutar codigo si la condicion es False<br> La ejecución de esta construcción es la siguiente: <br><ul><li className='subtitle__list'> Si el resultado es True se ejecuta solamente el bloque de sentencias 1 </li><li className='subtitle__list'> Si el resultado es False se ejecuta solamente el bloque de sentencias 2.</li></ul><br>La primera línea contiene la condición a evaluar. Esta línea debe terminar siempre por dos puntos (:). <br>A continuación, viene el bloque de órdenes que se ejecutan cuando la condición se cumple (es decir, cuando la condición es verdadera). Es importante señalar que este bloque debe ir sangrado, puesto que Python utiliza el sangrado para reconocer las líneas que forman un bloque de instrucciones. <br>Después viene la línea con la sentencia else, que indica a Python que el bloque que viene a continuación se tiene que ejecutar cuando la condición no se cumpla (es decir, cuando sea falsa). Esta línea también debe terminar siempre por dos puntos (:). La línea con la sentencia else no debe incluir nada más que el else y los dos puntos. <br>En último lugar está el bloque de instrucciones sangrado que corresponde al else. <br><h2 className='subtitle'> Diagrama de flujo de la sentencia condicional if ... else </h2><br>El diagrama de flujo siguiente muestra la ejecución de una sentencia if ... else: <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/if..else1.png?alt=media&token=4e8967de-53ae-4726-b55a-4ea5805eec89'><br><h2 className='subtitle'> Ejemplo de sentencia if….else </h2><br>Nos piden un programa el cual permita determinar si una persona es mayor edad, sabiendo que la edad mínima para considerar a una persona mayor de edad en Colombia es de 18 años. <br> <br><img src='https://firebasestorage.googleapis.com/v0/b/adapprogram-704ac.appspot.com/o/if..else2.png?alt=media&token=960c17c2-899e-41fd-bdfd-bb8f76c52ecd'> <br><br>Al momento de ejecutar este código puede ocurrir 2 casos, en el caso de que la sentencia if sea verdadera se nos imprimirá en pantalla el mensaje de “Es mayor de edad” y en el caso de que la edad no sea la mínima se imprimirá en pantalla “Es menor de edad”.",
                        "question": "Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.<br>Entrada, estos valores deben estar escritos en el código de python <br>Contraseña = python<br>ContraseñaValidation= python<br>Salida, este debe ser el mensaje que retorne la solución <br>La contraseña es correcta"

                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....elif.....else",
                        "url": "Estructura de decisión <br>sentencia if…elif…else <br>Si necesitamos mas de 2 opciones, la sentencia if…elif…else será la que nos proporcione esto, eto quiere decir que, si esto no es verdadero, intenta esto otro, y si todas las condiciones fallan en ser verdaderas, entonces haz esto. <br>elif es lo que buscamos. <br>La sintaxis básica es similar a la siguiente: <br>if primera_condicion: <br>    ejecutar sentencia<br>elif segunda_condicion: <br>    ejecutar sentencia<br>else: <br>    ejecutar sentencia alternativa si todas las condiciones previas son son evaluadas como <br>Ejemplo de sentencia if…elif…else <br><br>Determine por la edad de una persona a cuál es la etapa de la vida pertenece<br>Infancia (0 - 6 años) <br>Niñes (7 – 12 años) <br>Adolescencia (13 - 20 años) <br>Juventud (21 - 25 años) <br>Adultez (26- 59 años) <br>Persona Mayor (60 años o más) envejecimiento y vejez<br><br>edad = 23<br>if edad >= 0 and edad <=6: <br>    print('la persona pertenece a la etapa de infancia')<br>elif edad >= 7 and edad<=12: <br>    print('la persona pertenece a la etapa de niñes')<br>elif edad >= 13 and edad<=20: <br>    print('la persona pertenece a la etapa de Adolecencia')<br>elif edad >= 21 and edad<=25: <br>    print('la persona pertenece a la etapa de juventud')<br>elif edad >= 26 and edad <= 59: <br>    print('la persona pertenece a la etapa de adultez')<br>else: <br>    print('la persona pertenece a la etapa de persona mayor')<br><br>Resultado <br>“la persona pertenece a la etapa de juventud” <br>En este ejemplo, if pone a prueba una condición específica, los bloques elif son alternativas, y el bloque final else es la solución final cuando todas las condiciones previas no se han cumplido.",
                        "question": "Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:<br>Renta	Tipo impositivo<br>Menos de 10000€	5%<br>Entre 10000€ y 20000€	15%<br>Entre 20000€ y 35000€	20%<br>Entre 35000€ y 60000€	30%<br>Más de 60000€	45%<br>Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.<br>Entrada, estos valores deben estar escritos en el código de python <br>rentaAnual = 27500<br>Salida, este debe ser el mensaje que retorne la solución <br>Tienes que pagar 5500€",

                    },
                    {
                        "titulo": "Estructuras de decisión - if ternario",
                        "url": "Estructura de decisión  <br><br>If ternario  <br><br>El operador ternario en Python, al igual que en otros lenguajes, tiene la finalidad de hacer más compacta una condición If, permitiendo generar código condicionado en una sola línea y aunque no es ampliamente usado sí que tiene sus ventajas.  <br><br>La sintaxis de if ternario <br><br>condition_if_true if condition else condition_if_false <br><br>esta sintaxis de if ternario tiene una particularidad y es que primero escribimos las instrucciones que se ejecutaran si nuestra condición es verdadera, seguido de la sentencia if y nuestra condición, luego pondremos nuestra sentencia else seguido de las instrucciones que se ejecutaran en el caso que if sea falso.  <br><br>ejemplo de if ternario <br><br>es_bonito = True <br><br>print('Es bonito')  if es_bonito else print('No es bonito') <br><br>resultado  <br><br>“Es bonito”  <br><br>Como se puede ver, permiten verificar de manera rápida una condición, y lo mejor de todo es que se puede hacer en una sola línea de código. Por lo general hacen que el código sea más compacto y fácil de leer.  <br><br>Otra forma un tanto extraña y no demasiado usada es la siguiente forma:  <br><br>La sintaxis de if ternario 2 <br><br>(if_test_is_false, if_test_is_true)[test]  <br><br>ejemplo de if ternario 2 <br><br>es_bonito = True <br><br>apariencia = ('Feo', 'Bonito')[es_bonito]  <br><br>retultado <br><br>print('El gato es', apariencia)  <br><br>Este ejemplo funciona ya que True=1 y False=0, y puede ser usado también con listas. Es importante decir también que este ejemplo no es muy usado.",
                        "question": "Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.<br>Entrada, estos valores deben estar escritos en el código de python <br>Numero <br>Salida, este debe ser el mensaje que retorne la solución <br>El numero es impar",

                    },
                ]
            },            
            {
                "temas": "Estructuras iterativas",
                "contenido": [
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 1",
                        "url": "Estructuras iterativas  <br><br>Bucle while loop <br><br> A diferencia de las estructuras de decisión, las iterativas nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición.  <br><br>while loop repite la secuencia de acciones muchas veces hasta que alguna condición se evalúa como False. La condición se da antes del cuerpo del bucle y se comprueba antes de cada ejecución del cuerpo del bucle. Típicamente, el while se utiliza bucle cuando es imposible para determinar el número exacto de iteraciones del bucle de antemano.  <br><br>Estructura de while loop  <br><br>while some condition:  <br><br>    a block of statements <br><br>Ejemplo de while loop <br><br>anio = 2001  <br><br>while anio <= 2012:  <br><br>    print ('Informes del Año', anio)  <br><br>    anio += 1 <br><br>Resultado <br><br>Informes del año 2001  <br><br>Informes del año 2002  <br><br>Informes del año 2003  <br><br>Informes del año 2004  <br><br>Informes del año 2005  <br><br>Informes del año 2006  <br><br>Informes del año 2007  <br><br>Informes del año 2008  <br><br>Informes del año 2009  <br><br>Informes del año 2010  <br><br>Informes del año 2011  <br><br>Informes del año 2012 <br><br>Si miramos la última línea:  <br><br>anio += 1 <br><br>se puede notar que en cada iteración, incrementamos el valor de la variable que condiciona el bucle (anio). Si no lo hiciéramos, esta variable siempre sería igual a 2001 y el bucle se ejecutaría de forma infinita, ya que la condición (anio <= 2012) siempre se estaría cumpliendo.",
                        "question": "Escribir un programa dada una palabra, la muestre por pantalla 10 veces.<br> Entrada, estos valores deben estar escritos en el código de python <br>Itera= 1<br>Salida, este debe ser el mensaje que retorne la solución <br>1 2 3 4 5 6 7 8 9 10",
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 2",
                        "url": "Estructuras iterativas <br><br>Bucle while loop uso de break y continue <br><br>break <br><br>¿Qué sucede si el valor que condiciona la iteración no es numérico y no puede incrementarse? En ese caso, podremos utilizar una estructura de control condicional, anidada dentro del bucle, y frenar la ejecución cuando el condicional deje de cumplirse, con la palabra clave reservada break:  <br><br>while True:  <br><br>    nombre = raw_input('Indique su nombre: ') <br><br>   if nombre:  <br><br>        break <br><br> El bucle anterior, incluye un condicional anidado que verifica si la variable nombre es verdadera (solo será verdadera si el usuario tipea un texto en pantalla cuando el nombre le es solicitado). Si es verdadera, el bucle para (break). Si no, seguirá ejecutándose hasta que el usuario, ingrese un texto en pantalla.  <br><br>Continue <br><br> La instrucción Continue en Python devuelve la ejecución al comienzo del ciclo while. La declaración de Continue rechaza todas las declaraciones restantes en la iteración actual del bucle y mueve el control de nuevo a la parte superior del bucle.  <br><br>Ejemplo de continue en ciclo while loop <br><br>var = 10  <br><br>while var > 0:  <br><br>   var = var -1 <br><br>   if var == 5:  <br><br>      continue <br><br>   print ('valor de la variable:', var)  <br><br>Resultado <br><br>valor de la variable :10 <br><br>valor de la variable: 9 <br><br>valor de la variable: 8 <br><br>valor de la variable: 7 <br><br>valor de la variable: 6 <br><br>valor de la variable: 4  <br><br>valor de la variable: 3 <br><br>valor de la variable: 2 <br><br>valor de la variable: 1 <br><br>",
                        "question": "Escribir un programa que imprima los números del 1 al 10, pero que no imprima los numero 4 y 7.<br>Entrada, estos valores deben estar escritos en el código de python <br>Itera= 1<br>Salida, este debe ser el mensaje que retorne la solución <br>1 2 3 5 6 8 9 10",
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop",
                        "url": "Estructuras iterativas <br><br>Bucle foor loop <br><br>El ciclo for loop en Python se usa para iterar sobre una secuencia ( lista , tupla , cadena ) u otros objetos iterables. La iteración sobre una secuencia se llama recorrido.  <br><br>Estructura de bucle foor loop <br><br>for val in sequence:  <br><br>    loop body <br><br>Aquí val es la variable que toma el valor del elemento dentro de la secuencia en cada iteración. El bucle continúa hasta que llegamos al último elemento de la secuencia. El cuerpo del bucle for se separa del resto del código mediante sangría.  <br><br>Ejemplos de bucle foor loop <br><br>numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]  <br><br>sum = 0 <br><br>for val in numbers:  <br><br>    sum = sum+val <br><br>print('El total de la suma es', sum)  <br><br>Resultado <br><br>la suma es 48 <br><br>",
                        "question": "Escriba un programa que multiplique cada valor de una lista por si mismo, e imprima el total de esta. <br>Entrada, estos valores deben estar escritos en el código de python <br>Lista = [1, 5 , 6, 7, 8] <br>Salida, este debe ser el mensaje que retorne la solución <br>La multiplicacion de la lista da un total de 1680",
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop range()",
                        "url": "Estructuras iterativas  <br><br>Bucle foor loop uso de función range() <br><br>Podemos generar una secuencia de números usando range()la función. range(10)generará números del 0 al 9 (10 números). También podemos definir el tamaño de inicio, parada y paso como range(start, stop,step_size). step_size por defecto es 1 si no se proporciona. Esta función no almacena todos los valores en la memoria; sería ineficiente. Por lo tanto, recuerda el inicio, la parada, el tamaño del paso y genera el siguiente número sobre la marcha.  <br><br>Podemos usar la función range()en bucles  for para iterar a través de una secuencia de números. Se puede combinar con la función len() para iterar a través de una secuencia usando la indexación. Aquí hay un ejemplo.  <br><br>Ejemplo de for loop con función range() <br><br>genre = ['pop', 'rock', 'jazz']  <br><br>for i in range(len(genre)):  <br><br>    print(´'Me gusta el ', genre[i])  <br><br>Resultado  <br><br>Me gusta el pop <br><br>Me gusta el rock <br><br>Me gusta el jazz <br><br>",
                        "question": "Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).<br>Entrada, estos valores deben estar escritos en el código de python <br>Edad= 8<br>Salida, este debe ser el mensaje que retorne la solución <br>Has cumplido 1 anos<br>Has cumplido 2 anos<br>Has cumplido 3 anos<br>Has cumplido 4 anos<br>Has cumplido 5 anos<br>Has cumplido 6 anos<br>Has cumplido 7 anos<br>Has cumplido 8 anos<br>",
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop anidados",
                        "url": "Estructuras iterativas <br><br>Bucle foor loop anidado <br><br>Se habla de bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque. Al bucle que se encuentra dentro del otro se le puede denominar bucle interior o bucle interno. El otro bucle sería el bucle exterior o bucle externo. Los bucles pueden tener cualquier nivel de anidamiento (un bucle dentro de otro bucle dentro de un tercero, etc.).  <br><br>Bucle foor loop anidado (variables independientes)  <br><br>Se dice que las variables de los bucles son independientes cuando los valores que toma la variable de control del bucle interno no dependen del valor de la variable de control del bucle externo.  <br><br>Ejemplo de bucle foor loop 1 <br><br>for i in [0, 1, 2]:  <br><br>    for j in [0, 1]:  <br><br>        print(f'i vale {i} y j vale {j}') <br><br>resultado <br><br>i vale 0 y j vale 0 <br><br>i vale 0 y j vale 1 <br><br>i vale 1 y j vale 0 <br><br>i vale 1 y j vale 1 <br><br>i vale 2 y j vale 0 <br><br>i vale 2 y j vale 1 <br><br>En el ejemplo anterior, el bucle externo (el controlado por i) se ejecuta 3 veces y el bucle interno (el controlado por j) se ejecuta dos veces por cada valor de i. Por ello la instrucción print() se ejecuta en total 6 veces (3 veces que se ejecuta el bucle externo x 2 veces que se ejecuta cada vez el bucle interno = 6 veces). En general, el número de veces que se ejecuta el bloque de instrucciones del bucle interno es el producto de las veces que se ejecuta cada bucle.  <br><br>Ejemplo de bucle foor loop 2 <br><br>factoresX = [1,2,3,4,5]  <br><br>factoresY = [1,2,3,4,5]  <br><br>for factorX in factoresX:  <br><br>  for factorY in factoresY:  <br><br>print(f'{factorX} x {factorY} = {factorX * factorY}') <br><br>resultado  <br><br>1 x 1 = 1 <br><br>1 x 2 = 2 <br><br>1 x 3 = 3 <br><br>1 x 4 = 4 <br><br>1 x 5 = 5 <br><br>2 x 1 = 2 <br><br>2 x 2 = 4 <br><br>2 x 3 = 6 <br><br>2 x 4 = 8 <br><br>2 x 5 = 10 <br><br>3 x 1 = 3 <br><br>3 x 2 = 6 <br><br>3 x 3 = 9 <br><br>3 x 4 = 12 <br><br>3 x 5 = 15 <br><br>4 x 1 = 4 <br><br>4 x 2 = 8 <br><br>4 x 3 = 12 <br><br>4 x 4 = 16 <br><br>4 x 5 = 20 <br><br>5 x 1 = 5 <br><br>5 x 2 = 10 <br><br>5 x 3 = 15 <br><br>5 x 4 = 20 <br><br>5 x 5 = 25 <br><br>",
                        "question": "Escribir un programa que imprima las tablas de multiplicar del 1 al 10.<br>Entrada, estos valores deben estar escritos en el código de python <br>Lista1=[1,2,3,4,5,6,7,8,9,10] <br>Lista2=[1,2,3,4,5,6,7,8,9,10] <br>Salida, este debe ser el mensaje que retorne la solución <br>el producto es 1 <br>el producto es 2 <br>el producto es 3 <br>el producto es 4 <br>el producto es 5 <br>el producto es 6 <br>el producto es 7 <br>el producto es 8 <br>el producto es 9 <br>el producto es 10 <br>el producto es 2 <br>el producto es 4 <br>el producto es 6 <br>el producto es 8 <br>el producto es 10 <br>el producto es 12 <br>el producto es 14 <br>el producto es 16 <br>el producto es 18 <br>el producto es 20 <br>el producto es 3 <br>el producto es 6 <br>el producto es 9 <br>el producto es 12 <br>el producto es 15 <br>el producto es 18 <br>el producto es 21 <br>el producto es 24 <br>el producto es 27 <br>el producto es 30 <br>el producto es 4 <br>el producto es 8 <br>el producto es 12 <br>el producto es 16 <br>el producto es 20 <br>el producto es 24 <br>el producto es 28 <br>el producto es 32 <br>el producto es 36 <br>el producto es 40 <br>el producto es 5 <br>el producto es 10 <br>el producto es 15 <br>el producto es 20 <br>el producto es 25 <br>el producto es 30 <br>el producto es 35 <br>el producto es 40 <br>el producto es 45 <br>el producto es 50 <br>el producto es 6 <br>el producto es 12 <br>el producto es 18 <br>el producto es 24 <br>el producto es 30 <br>el producto es 36 <br>el producto es 42 <br>el producto es 48 <br>el producto es 54 <br>el producto es 60 <br>el producto es 7 <br>el producto es 14 <br>el producto es 21 <br>el producto es 28 <br>el producto es 35 <br>el producto es 42 <br>el producto es 49 <br>el producto es 56 <br>el producto es 63 <br>el producto es 70 <br>el producto es 8 <br>el producto es 16 <br>el producto es 24 <br>el producto es 32 <br>el producto es 40 <br>el producto es 48 <br>el producto es 56 <br>el producto es 64 <br>el producto es 72 <br>el producto es 80 <br>el producto es 9 <br>el producto es 18 <br>el producto es 27 <br>el producto es 36 <br>el producto es 45 <br>el producto es 54 <br>el producto es 63 <br>el producto es 72 <br>el producto es 81 <br>el producto es 90 <br>el producto es 10 <br>el producto es 20 <br>el producto es 30 <br>el producto es 40 <br>el producto es 50 <br>el producto es 60 <br>el producto es 70 <br>el producto es 80 <br>el producto es 90 <br>el producto es 100 ",
                    },
                ]
            },
            {
                "temas": "Funciones iterativas",
                "contenido": [
                    {
                        "titulo": "Funciones iterativas - Definición de función",
                        "url": "Funciones  <br><br>Definición de funciones en Python  <br><br>Las funciones son bloques de código que se pueden reutilizar simplemente llamando a la función. Esto permite la reutilización de código simple y elegante sin volver a escribir explícitamente secciones de código. Esto hace que el código sea más legible, facilita la depuración y limita los errores de escritura.  <br><br>Estructura de una función <br><br>def functionName():  <br><br>    code block <br><br>Ejemplo <br><br>def saludo(): <br><br>	print(“hola mundo”)  <br><br>saludo() <br><br>Resultado  <br><br>hola mundo",
                        "question":"Escribir una función que muestre por pantalla el saludo ¡Hola, amiga! cada vez que se la invoque.<br>Entrada, estos valores deben estar escritos en el código de python <br>Salida, este debe ser el mensaje que retorne la solución<br>¡Hola, amigo!",
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función",
                        "url": "Funciones  <br><br>Argumentos en funciones  <br><br>Un argumento es un valor que la función espera recibir cuando sea llamada, a fin de ejecutar acciones en base al mismo. Una función puede esperar uno o más parámetros, los cuales irán separados por una coma.  <br><br>Ejemplo Argumentos 1 <br><br>def saludo(nombre, apellido):  <br><br>    print(f'hola {nombre} {apellido}') <br><br>saludo('steven', 'otalvaro')  <br><br>Resultado  <br><br>Hola Steven otalvaro <br><br>Ahora bien, podemos setear los valores de los parámetros con el fin que el orden no importe, y de esta manera cuando nuestra función reciba los argumentos, los reciba de manera correcta, en el ejemplo anterior vimos como pasar argumentos a la función, ahora lo que haremos será setear los parámetros cuando se envían en la función y para esto, lo que deberos hacer es ponerle a cada nombre del parámetro el valor que este tendrá <br><br>Ejemplo <br><br>def saludo(nombre, apellido):  <br><br>    print(f'hola {nombre} {apellido}') <br><br>saludo(apellido='otalvaro', nombre='steven')  <br><br>Resultado  <br><br>Hola Steven otalvaro <br><br>Vemos que cuando llamamos a la función le indicamos el valor que tendrá cada argumento y de esta manera el orden de los argumentos no importará.  <br><br>",
                        "question": "Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.<br>Entrada, estos valores deben estar escritos en el código de python <br>Nombre = Steven <br>Salida, este debe ser el mensaje que retorne la solución <br>¡hola steven! <br>",
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función de tipo args y kwargs",
                        "url": "Funciones <br><br>Argumentos args y kwargs <br><br>Existen dos tipos de argumentos en Python, los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente. Encontrar un término en el español para estos últimos resulta algo complejo, equivaldría a argumentos de palabras clave, así que simplemente los llamaremos por su nombre original.  <br><br>Una de las principales diferencias entre los dos tipos de argumentos, como observamos anteriormente, es que los convencionales son posicionales, mientras que en los keyword arguments su ubicación es indistinta.  <br><br>Ejemplo de args <br><br>def suma(*args):  <br><br>    resultado = 0 <br><br>    for num in args:  <br><br>        resultado += num <br><br>    print(resultado)  <br><br>suma(1, 2, 3)  <br><br>Resultado  <br><br>6 <br><br>Ejemplo de kwargs <br><br>def concatenacion(**kwargs):  <br><br>    resultado = "" <br><br>    for arg in kwargs.values(): <br><br>        resultado += ' ' + arg <br><br>    print(resultado)concatenacion(a='python', b='es', c='un', d='lenguaje', e='de',f='programacion') <br><br>Resultado <br><br>python es un lenguaje de programacion",
                        "question": "Escriba una función que reciba un argumento **kwargs y realice la suma de los values.<br>Entrada, estos valores deben estar escritos en el código de python <br>Lista = [1,10,84,6,4] <br>Salida, este debe ser el mensaje que retorne la solución <br>La suma total es 105",
                    },
                    {
                        "titulo": "Funciones iterativas - Sentencia return en funciones",
                        "url": "Funciones  <br><br>Return  <br><br> Se utiliza una declaración de return para finalizar la ejecución de la llamada de función y devuelve el resultado (el valor de la expresión que sigue a la palabra clave return) . Las sentencias posteriores a las sentencias de retorno no se ejecutan. Si la declaración de devolución no tiene ninguna expresión, se devuelve el valor especial Ninguno. Una declaración de retorno se usa en general para invocar una función para que las declaraciones pasadas puedan ejecutarse.  <br><br>Syntax:  <br><br>def fun(): <br><br>    statements <br><br>    return [expression]  <br><br>ejemplo  <br><br>def suma(*args):  <br><br>	resultado = 0 <br><br> 	for num in args:  <br><br>		resultado += num <br><br>	return resultado <br><br>print(suma(1,2,3,4,5,6))",
                        "question": "Escribir una función que calcule el máximo común divisor de dos números.<br>Entrada, estos valores deben estar escritos en el código de python <br>Numero1=24<br>Numero2=36<br>Salida, este debe ser el mensaje que retorne la solución <br>12",
                    }
                ]
            },
        ]
        return jsonify(urlYoutube), 200
    except Exception as e:
        return f"an error ocurred : {e}"