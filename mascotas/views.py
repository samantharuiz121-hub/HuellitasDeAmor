
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>HuellitasDeAmor</title>
        </head>
        <body>
            <h1>Bienvenidos a HuellitasDeAmor</h1>
            <p>Una oportunidad de amor para cada mascota.</p>
        </body>
        </html>
    """)
