from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Simulación de reseñas con fechas (todas negativas)
    simulated_reviews = [
        {
            'location': 'Sucursal Molina Ronda',
            'rating': '3.7',
            'comment': 'Publicidad engañosa clases anunciadas a un precio 
            cuando luego es al parecer para 45 min y las clases son obligadamente de 1h.
            Trato nefasto, subidas de precio continuas (cuando baja la gasolina, se les debe de olvidar bajarlas)
            y listas de espera trimestrales para un examen. Un cuadro, una prueba más de que mucho aprieta poco abarca,
            de que el dinero es lo que primero entra y la atención al cliente lo último que llega. 
            Hacía tiempo que no veía un establecimiento tan falto de escrúpulos.',
            'reviewer': 'Victor Mariscal Guerra',
            'date': '15/04/2025 10:45',
            'datetime': datetime.strptime("2025-04-15T10:45:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal Rally Motril',
            'rating': '4.1',
            'comment': 'Mi experiencia, a grandes rasgos, no fue satisfactoria.
            Especialmente debido a la secretaria, Mamen, que sin duda es lo peor de la autoescuela. 
            Su manera de comportarse de cara al público es brusca, seca y borde,
            lo que hace la comunicación con ella muy incómoda y difícil:
            desde acordar días para clases prácticas, hasta apuntarte a una fecha de examen.
            Además, se pone muy borde / rácana cuando le pides ventosas para la L.
            Me alegro de no tener que volver a lidiar con ella.
            En cuanto a los profesores, hay de todo. Algunos son más callados,
            otros son más conversadores, pero en general son pacientes y te aconsejan bien
            a la hora de conducir. Por eso, le doy dos estrellas y no una.',
            'reviewer': 'Azariego',
            'date': '26/03/2024 16:20',
            'datetime': datetime.strptime("2024-03-26T16:20:00", "%Y-%m-%dT%H:%M:%S")
        },
        {
            'location': 'Sucursal Molina Bola',
            'rating': '3.8',
            'comment': 'Mala experiencia, No lo recomiendo.',
            'reviewer': 'Luis Jesus',
            'date': '13/04/2025 09:15',
            'datetime': datetime.strptime("2025-04-13T09:15:00", "%Y-%m-%dT%H:%M:%S")
        }
    ]

    # Calcular las puntuaciones por sucursal
    ratings = []
    for location in set(review['location'] for review in simulated_reviews):
        location_reviews = [review for review in simulated_reviews if review['location'] == location]
        avg_rating = sum(float(review['rating']) for review in location_reviews) / len(location_reviews)
        ratings.append({'name': location, 'rating': round(avg_rating, 1)})

    # Ordenar reseñas de más reciente a más antigua
    sorted_reviews = sorted(simulated_reviews, key=lambda x: x['datetime'], reverse=True)

    return render_template("index.html", reviews=sorted_reviews, ratings=ratings)

if __name__ == "__main__":
    app.run(debug=True)
