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
                "question 1": "Que es una variable",
                "option": [
                    "1: Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal",
                    "2: Es un espacio en el disco duro en el cual se almacena información que deseamos almacenar de manera temporal",
                    "3: Es un tipo de dato simple ",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal"
            },
            {
                "question 2": "Cual de las opciones no es dato primitivo simple",
                "option": [
                    "1: Numérico",
                    "2: Cadenas",
                    "3: String",
                    "4: Booleanos"
                ],
                "respuesta": "String"
            },
            {
                "question 3": "Cuál de las opciones no es dato primitivo compuesto",
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
        answer= "Es un espacio en memoria en el cual se almacena información que deseamos almacenar de manera temporal"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

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
        validation= False
        if request.json['respuesta'] == 3:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/variables/3', methods=['POST'])
def variables3():
    try:
        answer=   "Arrays"
        validation= False
        if request.json['respuesta'] == "Arrays":
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision')
def estructurasdecision():
    try:
        question= [
            {
                "question 1": "Qué es una estructura de decisión",
                "option": [
                    "Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados",
                    "Es una condición de parada",
                    "Es una estructura iterativa",
                    "Es una estructura que permite hacer saltos de línea en nuestro código"
                ],
                "respuesta": "Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados"
            },
            {
                "question": "Cuál es la sintaxis de la sentencia if en Python",
                "option 2": [
                    "if condicion: ejecutar sentencia",
                    "if (condición): ejecutar sentencia",
                    "if condición{ ejecutar sentencia }",
                    "if (condición){ ejecutar sentencia }"
                ],
                "respuesta":  "if condicion: ejecutar sentencia"
            },
            {
                "question 3": "Cuál es la sintaxis de la sentencia if… else en python",
                "option": [
                    "if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False",
                    "if (condición): ejecutar sentencia else: ejecutar codigo si la condicion es False",
                    "if condición{ ejecutar sentencia } else{ ejecutar codigo si la condicion es False }",
                    "if (condición){ ejecutar sentencia } (else){ ejecutar codigo si la condicion es False }"
                ],
                "respuesta": "if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False"
            },
            {
                "question 4": "Cuál es la sintaxis de la sentencia if… elif…else en python",
                "option": [
                    "if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia",
                    "if (condición): ejecutar sentencia (elif) segunda_condicion: ejecutar sentencia (else): ejecutar sentencia",
                    "if condición { ejecutar sentencia } elif segunda_condicion{ ejecutar sentencia } else { ejecutar sentencia }",
                    "if (condición){ ejecutar sentencia } elif (segunda_condicion) { ejecutar sentencia } (else) { ejecutar sentencia }"
                ],
                "respuesta": "if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia"
            },
            {
                "question 5": "Para que nos sirven los operadores de comparación",
                "option": [
                    "Sirven para comparar datos primitivos",
                    "Sirven para comparar textos",
                    "Sirven para comparar dos o más valores",
                    "Ninguna de las anteriores "
                ],
                "respuesta": "Sirven para comparar dos o más valores"
            },
            {
                "question 6": "Cual de las siguientes opciones no es un operador de comparación",
                "option": [
                    "!=",
                    "<",
                    ">=",
                    "|=="
                ],
                "respuesta": "|=="
            },
            {
                "question 7": "Si quiero hacer una comparación de una serie de valores, y esta comparación me retorna 2 posibles valores, y quiero que se ejecute un bloque de código A, si la comparación da un valor X, o un bloque de código B si la comparación da resultado de valor Y, debo hacer uso de",
                "option": [
                    "Sentencia if",
                    "Sentencia if..else",
                    "Sentencia if…elif..else",
                    "Ninguna de las anteriores"
                ],
                "respuesta": "Sentencia if..else"
            },
            {
                "question 8": "Cual es La sintaxis de if ternario",
                "option": [
                    "condition_if_true if condition else condition_if_false",
                    "condition_if_ false if condition else condition_if_ true",
                    "condition true if condition",
                    "condition else condition_if_false"
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
        answer=  "Una estructura de decisión permite que la ejecución de un algoritmo tome distintos caminos, que llevan a distintos resultados"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

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
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/3', methods=['POST'])
def estructurasdecision3():
    try:
        answer= "if condicion: ejecutar sentencia else: ejecutar codigo si la condicion es False"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecisión/4', methods=['POST'])
def estructurasdecision4():
    try:
        answer= "if condicion: ejecutar sentencia elif segunda_condicion: ejecutar sentencia else: ejecutar sentencia"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/5', methods=['POST'])
def estructurasdecision5():
    try:
        answer= "Sirven para comparar dos o más valores"
        validation= False
        if request.json['respuesta'] == 3:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecision/6', methods=['POST'])
def estructurasdecision6():
    try:

        answer= "|=="
        validation= False
        if request.json['respuesta'] == 4:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecisión/7', methods=['POST'])
def estructurasdecision7():
    try:
        answer= "Sentencia if..else"
        validation= False
        if request.json['respuesta'] == 2:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasdecisión/8', methods=['POST'])
def estructurasdecisión8():
    try:
        answer=  "condition_if_true if condition else condition_if_false"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa')
def estructurasdecisión():
    try:
        question= [
            {
                "question 1": "Que es una Estructuras iterativa",
                "option": [
                    "1: las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición",
                    "2: las Estructuras iterativa nos permiten ejecutar un mismo código una sola vez",
                    "3: las Estructuras iterativa nos permiten comparar funciones",
                    "4: las Estructuras iterativa nos permiten ejecutar el código varias veces mientras una condición no se cumpla"
                ],
                "respuesta": "las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición"
            },
            {
                "question 2": "Cual es la estructura de la while loop",
                "option": [
                    "1: while condition: a block of statements",
                    "2: while condition a block of statements",
                    "3: while (condition){ a block of statements }",
                    "4: while condition{ a block of statements }",
                ],
                "respuesta": "while condition: a block of statements"
            },
            {
                "question 3": "La sentencia break nos permite",
                "option": [
                    "1: Comparar variables",
                    "2: Detener la ejecución de un bloque de código",
                    "3: Detener la ejecución de una Estructuras iterativa",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Detener la ejecución de una Estructuras iterativa"
            },
            {
                "question 4": "La sentencia break nos permite",
                "option": [
                    "1: Comparar variables",
                    "2: Detener la ejecución de un bloque de código",
                    "3: Detener la ejecución de una Estructuras iterativa",
                    "4: Ninguna de las anteriores "
                ],
                "respuesta": "Detener la ejecución de una Estructuras iterativa"
            }, {
                "question 5": "La sentencia continue nos permite",
                "option": [
                    "1: Terminar el ciclo",
                    "2: Devolver la ejecución al comienzo del ciclo",
                    "3: Volver falsa la condición del ciclo ",
                    "4: Ninguna de las anteriores"
                ],
                "respuesta": "Devolver la ejecución al comienzo del ciclo"
            },
            {
                "question 6": "La sentencia continue nos permite",
                "option": [
                    "1: Terminar el ciclo",
                    "2: Devolver la ejecución al comienzo del ciclo",
                    "3: Volver falsa la condición del ciclo ",
                    "4: Ninguna de las anteriores"
                ],
                "respuesta": "Devolver la ejecución al comienzo del ciclo"
            },
            {
                "question 7": "Que es un ciclo anidado ",
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
        answer= "las Estructuras iterativa nos permiten ejecutar un mismo código, de manera repetida, mientras se cumpla una condición"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/2', methods=['POST'])
def estructurasiterativa2():
    try:
        answer= "while condition: a block of statements"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/3', methods=['POST'])
def estructurasiterativa3():
    try:
        answer= "for sequence in val: loop body"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/4', methods=['POST'])
def estructurasiterativa4():
    try:
        answer= "Detener la ejecución de una Estructuras iterativa"
        validation= False
        if request.json['respuesta'] == 3:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/5', methods=['POST'])
def estructurasiterativa5():
    try:
        answer= "Devolver la ejecución al comienzo del ciclo"
        validation= False
        if request.json['respuesta'] == 2:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/6', methods=['POST'])
def estructurasiterativa6():
    try:
        answer=  "Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/estructurasiterativa/7', methods=['POST'])
def estructurasiterativa7():
    try:
        answer= "Son bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas')
def funcionesiterativas():
    try:
        request.json['respuesta']
        question= [
            {
                "question 1": "Que es una función ",
                "option": [
                    "1: Es una estructura repetitiva",
                    "2: Son bloques de código que se pueden reutilizar simplemente llamando a la función",
                    "3: Son bloques de código que no se pueden reutilizar simplemente llamando a la función",
                    "4: Son bloques de código que permite cambiar el orden de ejecución del código"

                ],
                "respuesta": "Son bloques de código que se pueden reutilizar simplemente llamando a la función"
            },
            {"question 2": "Cual es la estructura de una función ",
                "option": [

                    "1: def functionName: code block",
                    "2: def functionName{ code block }",
                    "3: def (functionName){ code block }",
                    "4: def functionName(): code block"

                ],
                "respuesta": "def functionName(): code block"
             },
            {
                "question 3": "Cuándo se habla de argumentos en funciones se refiera a",
                "option": [

                    "1: Un valor que la función espera recibir cuando se define",
                    "2: Una validación dentro de la función",
                    "3: Es un valor que la función espera recibir cuando sea llamada",
                    "4: Ninguna de las anteriores"

                ],
                "respuesta": "Es un valor que la función espera recibir cuando sea llamada"
            },
            {
                "question 4": "Cuál de los siguientes argumentos no son convencionales",
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
        answer= "Son bloques de código que se pueden reutilizar simplemente llamando a la función"
        validation= False
        if request.json['respuesta'] == 2:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/2', methods=['POST'])
def funcionesiterativas2():
    try:
        answer= "def functionName(): code block"
        validation= False
        if request.json['respuesta'] == 4:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/3', methods=['POST'])
def funcionesiterativas3():
    try:
        answer= "Es un valor que la función espera recibir cuando sea llamada"
        validation= False
        if request.json['respuesta'] == 3:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"


@ questionAPI.route('/funcionesiterativas/4', methods=['POST'])
def funcionesiterativas4():
    try:
        answer= "args y kwargs"
        validation= False
        if request.json['respuesta'] == 1:
            validation= True

        return jsonify({
            'validation': validation,
            'answer': answer
            }), 200
    except Exception as e:
        return f"an error ocurred : {e}"
