import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

AuditivoAPI = Blueprint('AuditivoAPI', __name__)

@AuditivoAPI.route('/list/auditivo')
def read():
    try:
        urlYoutube = [
            {
                "temas": "Variables y Tipos de datos",
                "contenido": [
                    {
                        "titulo": "Variables y Tipos de datos",
                        "url": 'https://youtu.be/bW5S07R6ds8'
                    }
                ]
            },
            {
                "temas": "Estructuras de decisión",
                "contenido": [
                    {
                        "titulo": "Estructuras de decisión - Sentencia If",
                        "url": 'https://youtu.be/ceo53Bg5CtU'
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If......else",
                        "url": 'https://youtu.be/40Cq5kbmhXw'
                    },
                    {
                        "titulo": "Estructuras de decisión - Sentencia If....elif.....else",
                        "url": 'https://youtu.be/c977VBrJxow'
                    },
                    {
                        "titulo": "Estructuras de decisión - If ternario",
                        "url": 'https://youtu.be/BNwGy9qEE_g'
                    }
                ]
            },
            {
                "temas": "Estructuras iterativas",
                "contenido": [
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Part 1",
                        "url": 'https://youtu.be/ZiKdcwok9sw'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia while loop Pat 2",
                        "url": 'https://youtu.be/4oQawl4soyQ'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop ",
                        "url": 'https://youtu.be/LzISwY71KkI'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop uso de range()",
                        "url": 'https://youtu.be/evpBfOTU0go'
                    },
                    {
                        "titulo": "Estructuras iterativas - Sentencia For loop anidados",
                        "url": 'https://youtu.be/0R4CP_kGODQ'
                    }
                ]
            },
            {
                "temas": "Funciones iterativas",
                "contenido": [
                    {
                        "titulo": "Funciones iterativas - Definición de función",
                        "url": 'https://youtu.be/pQZPcX1tAbI'
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función ",
                        "url": 'https://youtu.be/yCnb9Ys7EoM'
                    },
                    {
                        "titulo": "Funciones iterativas - Argumentos de una función de tipo args y kwargs",
                        "url": 'https://youtu.be/laQjXt9ML-M'
                    },
                    {
                        "titulo": "Funciones iterativas - Sentencia return en funciones",
                        "url": 'https://youtu.be/NSt5bdSbc-w'
                    }
                ]
            },
        ]
        return jsonify(urlYoutube), 200
    except Exception as e:
        return f"an error ocurred : {e}"
