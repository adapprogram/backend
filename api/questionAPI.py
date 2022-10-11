import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

questionAPI = Blueprint('questionAPI', __name__)


@questionAPI.route('/variables')
def variables():
    try:
        question = [
            {
                "question": "Que es una variable",
                "option": [
                    "1: Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal",
                    "2: Es un espacio en el disco duro en el cual se almacena información que deseamos almacenar de manera temporal",
                    "3: Es un tipo de dato simple ",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal"
            },
            {
                "question": "Cual de las opciones no es dato primitivo simple",
                "option": [
                    "1: Numérico",
                    "2: Cadenas",
                    "3: String",
                    "4: Booleanos"
                ],
                "respuesta": "String"
            },
            {
                "question": "Cuál de las opciones no es dato primitivo compuesto",
                "option": [
                    "1: Listas",
                    "2: Tuplas",
                    "3: Arrays",
                    "4: Diccionarios"
                ],
                "respuesta": "Arrays"
            }
        ]
        return jsonify(question), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/variables/1', methods=['POST'])
def variables1():
    try:
        answer = "Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/variables/2', methods=['POST'])
def variables2():
    try:
        answer = "String"
        validation = False
        if request.json['respuesta'] == 3:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/variables/3', methods=['POST'])
def variables3():
    try:
        answer = "Arrays"
        validation = False
        if request.json['respuesta'] == 3:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@questionAPI.route('/estructurasdecision')
@questionAPI.route('/estructurasdecision')
def estructurasdecision():
    try:
        question = [
            {
                "question": "Qué es una estructura de decisión",
                "option": [
                    "1: Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados",
                    "2: Es una condición de parada",
                    "3: Es una estructura iterativa",
                    "4: Es una estructura que permite hacer saltos de línea en nuestro código"
                ],
                "respuesta": "Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados"
            },
            {
                "question": "Cuál es la sintaxis de la sentencia if en Python",
                "option": [
                    "1: if condicion: ejecutar sentencia",
                    "2: if (condición): ejecutar sentencia",
                    "3: if condición{ ejecutar sentencia }",
                    "4: if (condición){ ejecutar sentencia }"
                ],
                "respuesta":  "if condicion: ejecutar sentencia"
            },
            {
                "question": "Cuál es la sintaxis de la sentencia if… else en python",
                "option": [
                    "1: if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False",
                    "2: if (condición): ejecutar sentencia else: ejecutar codigo si la condicion es False",
                    "3: if condición{ ejecutar sentencia } else{ ejecutar codigo si la condicion es False }",
                    "4: if (condición){ ejecutar sentencia } (else){ ejecutar codigo si la condicion es False }"
                ],
                "respuesta": "if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False"
            },
            {
                "question": "Cuál es la sintaxis de la sentencia if… elif…else en python",
                "option": [
                    "1: if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia",
                    "2: if (condición): ejecutar sentencia (elif) segunda_condicion: ejecutar sentencia (else): ejecutar sentencia",
                    "3: if condición { ejecutar sentencia } elif segunda_condicion{ ejecutar sentencia } else { ejecutar sentencia }",
                    "4: if (condición){ ejecutar sentencia } elif (segunda_condicion) { ejecutar sentencia } (else) { ejecutar sentencia }"
                ],
                "respuesta": "if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia"
            },
            {
                "question": "Para que nos sirven los operadores de comparación",
                "option": [
                    "1: Sirven para comparar datos primitivos",
                    "2: Sirven para comparar textos",
                    "3: Sirven para comparar dos o más valores",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta":"Sirven para comparar dos o más valores"
            },
            {
                "question": "Cual de las siguientes opciones no es un operador de comparación",
                "option": [
                    "1: !=",
                    "2: <",
                    "3: >=",
                    "4: |=="
                ],
                "respuesta": "|=="
            },
            {
                "question": "Si quiero hacer una comparación de una serie de valores, y esta comparación me retorna 2 posibles valores, y quiero que se ejecute un bloque de código A, si la comparación da un valor X, o un bloque de código B si la comparación da resultado de valor Y, debo hacer uso de",
                "option": [
                    "1: Sentencia if",
                    "2: Sentencia if..else",
                    "3: Sentencia if…elif..else",
                    "4: Ninguna de las anteriores"
                ],
                "respuesta": "Sentencia if..else"
            },
            {
                "question": "Cual es La sintaxis de if ternario",
                "option": [
                    "1: condition_if_true if condition else condition_if_false",
                    "2: condition_if_ false if condition else condition_if_ true",
                    "3: condition true if condition",
                    "4: condition else condition_if_false"
                ],
                "respuesta": "condition_if_true if condition else condition_if_false"
            }

        ]
        return jsonify(question), 200
    except Exception as e:
        return f"an error ocurred : {e}"

@ questionAPI.route('/estructurasdecision/1', methods=['POST'])
def estructurasdecision1():
    try:
        answer = "Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/2', methods=['POST'])
def estructurasdecision2():
    try:
        answer = "if condicion: ejecutar sentencia"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/3', methods=['POST'])
def estructurasdecision3():
    try:
        answer = "if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/4', methods=['POST'])
def estructurasdecision4():
    try:
        answer = "if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/5', methods=['POST'])
def estructurasdecision5():
    try:
        answer = "Sirven para comparar dos o más valores"
        validation = False
        if request.json['respuesta'] == 3:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/6', methods=['POST'])
def estructurasdecision6():
    try:

        answer = "|=="
        validation = False
        if request.json['respuesta'] == 4:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/7', methods=['POST'])
def estructurasdecision7():
    try:
        answer = "Sentencia if..else"
        validation = False
        if request.json['respuesta'] == 2:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/8', methods=['POST'])
def estructurasdecision8():
    try:
        answer = "condition_if_true if condition else condition_if_false"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa')
def estructurasiterativa():
    try:
        question = [
            {
                "question": "Que es una Estructuras iterativa",
                "option": [
                    "1: las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición",
                    "2: las Estructuras iterativa nos permiten ejecutar un mismo código una sola vez",
                    "3: las Estructuras iterativa nos permiten comparar funciones",
                    "4: las Estructuras iterativa nos permiten ejecutar el código varias veces mientras una condición no se cumpla"
                ],
                "respuesta": "las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición"
            },
            {
                "question": "Cual es la estructura de la while loop",
                "option": [
                    "1: while condition: a block of statements",
                    "2: while condition a block of statements",
                    "3: while (condition){ a block of statements }",
                    "4: while condition{ a block of statements }",
                ],
                "respuesta": "while condition: a block of statements"
            },
            {
                "question": "La sentencia break nos permite",
                "option": [
                    "1: Comparar variables",
                    "2: Detener la ejecución de un bloque de código",
                    "3: Detener la ejecución de una Estructuras iterativa",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Detener la ejecución de una Estructuras iterativa"
            },
            {
                "question": "La sentencia break nos permite",
                "option": [
                    "1: Comparar variables",
                    "2: Detener la ejecución de un bloque de código",
                    "3: Detener la ejecución de una Estructuras iterativa",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Detener la ejecución de una Estructuras iterativa"
            }, {
                "question": "La sentencia continue nos permite",
                "option": [
                    "1: Terminar el ciclo",
                    "2: Devolver la ejecución al comienzo del ciclo",
                    "3: Volver falsa la condición del ciclo ",
                    "4: Ninguna de las anteriores"
                ],
                "respuesta": "Devolver la ejecución al comienzo del ciclo"
            },
            {
                "question": "La sentencia continue nos permite",
                "option": [
                    "1: Terminar el ciclo",
                    "2: Devolver la ejecución al comienzo del ciclo",
                    "3: Volver falsa la condición del ciclo ",
                    "4: Ninguna de las anteriores"
                ],
                "respuesta": "Devolver la ejecución al comienzo del ciclo"
            },
            {
                "question": "Que es un ciclo anidado ",
                "option": [
                    "1: Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque",
                    "2: Son bucles anidados cuando un bucle se encuentra por fuera del bloque de instrucciones de otro ciclo",
                    "3: Se habla de bucles anidados cuando un bucle se encuentra definido dentro entre 2 ciclos",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque"
            }
        ]
        return jsonify(question), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/1', methods=['POST'])
def estructurasiterativa1():
    try:
        answer = "las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/2', methods=['POST'])
def estructurasiterativa2():
    try:
        answer = "while condition: a block of statements"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/3', methods=['POST'])
def estructurasiterativa3():
    try:
        answer = "for sequence in val: loop body"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/4', methods=['POST'])
def estructurasiterativa4():
    try:
        answer = "Detener la ejecución de una Estructuras iterativa"
        validation = False
        if request.json['respuesta'] == 3:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/5', methods=['POST'])
def estructurasiterativa5():
    try:
        answer = "Devolver la ejecución al comienzo del ciclo"
        validation = False
        if request.json['respuesta'] == 2:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/6', methods=['POST'])
def estructurasiterativa6():
    try:
        answer = "Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/7', methods=['POST'])
def estructurasiterativa7():
    try:
        answer = "Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas')
def funcionesiterativas():
    try:
        question = [
            {
                "question": "Que es una función ",
                "option": [
                    "1: Es una estructura repetitiva",
                    "2: Son bloques de código que se pueden reutilizar simplemente llamando a la función",
                    "3: Son bloques de código que no se pueden reutilizar simplemente llamando a la función",
                    "4: Son bloques de código que permite cambiar el orden de ejecución del código"

                ],
                "respuesta": "Son bloques de código que se pueden reutilizar simplemente llamando a la función"
            },
            {"question": "Cual es la estructura de una función ",
                "option": [

                    "1: def functionName: code block",
                    "2: def functionName{ code block }",
                    "3: def (functionName){ code block }",
                    "4: def functionName(): code block"

                ],
                "respuesta": "def functionName(): code block"
             },
            {
                "question": "Cuándo se habla de argumentos en funciones se refiera a",
                "option": [

                    "1: Un valor que la función espera recibir cuando se define",
                    "2: Una validación dentro de la función",
                    "3: Es un valor que la función espera recibir cuando sea llamada",
                    "4: Ninguna de las anteriores"

                ],
                "respuesta": "Es un valor que la función espera recibir cuando sea llamada"
            },
            {
                "question": "Cuál de los siguientes argumentos no son convencionales",
                "option": [

                    "1: args y kwargs",
                    "2: value y totals",
                    "3: name y totals",
                    "4: Ninguna de las anteriores"

                ],
                "respuesta": "args y kwargs"
            }
        ]
        return jsonify(question), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/1', methods=['POST'])
def funcionesiterativas1():
    try:
        answer = "Son bloques de código que se pueden reutilizar simplemente llamando a la función"
        validation = False
        if request.json['respuesta'] == 2:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/2', methods=['POST'])
def funcionesiterativas2():
    try:
        answer = "def functionName(): code block"
        validation = False
        if request.json['respuesta'] == 4:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/3', methods=['POST'])
def funcionesiterativas3():
    try:
        answer = "Es un valor que la función espera recibir cuando sea llamada"
        validation = False
        if request.json['respuesta'] == 3:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/4', methods=['POST'])
def funcionesiterativas4():
    try:
        answer = "args y kwargs"
        validation = False
        if request.json['respuesta'] == 1:
            validation = True

        return jsonify({
            'validation': validation,
            'answer': answer
        }), 200
    except Exception as e:
        return f"an error ocurred : {e}"
