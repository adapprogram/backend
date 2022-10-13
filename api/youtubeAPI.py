import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

youtubeAPI = Blueprint('youtubeAPI', __name__)

@youtubeAPI.route('/list/visual')
def read():
    try:
        urlYoutube = [
            {
                "temas": "Variables y Tipos de datos",
                "contenido": [
                    {
                        "titulo": "Variables y Tipos de datos",
                        "url": 'https://youtu.be/ZAEI--hSr9E'
                    }
                ]
            },
            {
                "temas": "Estructuras de decisión",
                "contenido": [
                    {
                        "titulo": "Estructuras de decisión - Sentencia If",
                        "url": 'https://youtu.be/ZlvzUZBW_Ws'
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If......else",
                        "url": 'https://youtu.be/KJ-SFov_kCg'
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....elif.....else",
                        "url": 'https://youtu.be/LM7bl-mocLk'
                    },
                    {
                        "titulo": "Estructuras de decisión - If ternario",
                        "url": 'https://youtu.be/DlQvDf7hmiU'
                    }
                ]
            },
            {
                "temas": "Estructuras iterativas",
                "contenido": [
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 1",
                        "url": 'https://youtu.be/CqA0dwzqj4Y'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Pat 2",
                        "url": 'https://youtu.be/OytmQBhMAlI'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop ",
                        "url": 'https://youtu.be/1YS0is5d1vg'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop uso de range()",
                        "url": 'https://youtu.be/oqWDTO-fA0o'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop anidados",
                        "url": 'https://youtu.be/7fCvUdCoeCs'
                    }
                ]
            },
            {
                "temas": "Funciones iterativas",
                "contenido": [
                    {
                        "titulo": "Funciones iterativas - Definición de función",
                        "url": 'https://youtu.be/sn8kmZbbYFY'
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función ",
                        "url": 'https://youtu.be/zQ05kAOs7uI'
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función de tipo args y kwargs",
                        "url": 'https://youtu.be/7MGKW5CALRM'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia return en funciones",
                        "url": 'https://youtu.be/96r8PzpozgU'
                    }
                ]
            },
        ]
        return jsonify(urlYoutube), 200
    except Exception as e:
        return f"an error ocurred : {e}"
