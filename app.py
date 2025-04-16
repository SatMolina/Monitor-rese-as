from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Simulación de reseñas negativas con fechas
    simulated_reviews = [
        {
            'location': 'Sucursal Málaga Centro',
            'rating': 'ONE',
            'comment': 'No me gustó el trato.',
            'reviewer': 'Juan Pérez',
            'date': '15/04/2025 10:45',
            'datetime': datetime.strptime("2025-04-15T10:45:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal Teatinos',
            'rating': 'TWO',
            'comment': 'Demasiada espera para clases prácticas.',
            'reviewer': 'Ana García',
            'date': '14/04/2025 16:20',
            'datetime': datetime.strptime("2025-04-14T16:20:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal El Palo',
            'rating': 'ONE',
            'comment': 'No me resolvieron las dudas.',
            'reviewer': 'Carlos Ruiz',
            'date': '13/04/2025 09:15',
            'datetime': datetime.strptime("2025-04-13T09:15:00", "%Y-%m-%dT%H:%M:%S")
        }
    ]

    # Ordenar de más reciente a más antigua
    sorted_reviews = sorted(simulated_reviews, key=lambda x: x['datetime'], reverse=True)

    return render_template("index.html", reviews=sorted_reviews)

if __name__ == "__main__":
    app.run(debug=True)
