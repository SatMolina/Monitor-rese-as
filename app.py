from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Simulación de reseñas con fechas
    simulated_reviews = [
        {
            'location': 'Sucursal Molina Ronda',
            'rating': '3.7',
            'comment': 'No me gustó el trato.',
            'reviewer': 'Juan Pérez',
            'date': '15/04/2025 10:45',
            'datetime': datetime.strptime("2025-04-15T10:45:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal Rally Motril',
            'rating': '4.1',
            'comment': 'Demasiada espera para clases prácticas.',
            'reviewer': 'Ana García',
            'date': '14/04/2025 16:20',
            'datetime': datetime.strptime("2025-04-14T16:20:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal Molina Bola',
            'rating': '3.8',
            'comment': 'Mala experiencia, No lo recomiendo.',
            'reviewer': 'Carlos Ruiz',
            'date': '13/04/2025 09:15',
            'datetime': datetime.strptime("2025-04-13T09:15:00", "%Y-%m-%dT%H:%M:%S")
        }
    ]

    # Filtrar solo reseñas negativas (de 1 o 2 estrellas)
    negative_reviews = [review for review in simulated_reviews if float(review['rating']) <= 2]

    # Calcular las puntuaciones por sucursal
    ratings = []
    for location in set(review['location'] for review in simulated_reviews):
        location_reviews = [review for review in simulated_reviews if review['location'] == location]
        avg_rating = sum(float(review['rating']) for review in location_reviews) / len(location_reviews)
        ratings.append({'name': location, 'rating': round(avg_rating, 1)})

    # Ordenar reseñas de más reciente a más antigua
    sorted_reviews = sorted(simulated_reviews, key=lambda x: x['datetime'], reverse=True)

    return render_template("index.html", reviews=sorted_reviews, ratings=ratings, negative_reviews=negative_reviews)

if __name__ == "__main__":
    app.run(debug=True)
