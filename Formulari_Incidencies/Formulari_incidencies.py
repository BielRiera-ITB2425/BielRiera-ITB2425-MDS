from rich.table import Table
from rich import print
from rich.console import Console

def obtener_color_urgencia(nivel):
    """Devuelve un color basado en el nivel de urgencia."""
    if nivel == 'Molt Urgent':
        return 'red'
    elif nivel == 'Urgent':
        return 'orange1'
    else:
        return 'yellow'

def formatear_incidencias(datos):
    """Formatea los datos de las incidencias en una tabla colorida.

    Args:
        datos: Una lista de diccionarios, donde cada diccionario representa una incidencia.

    Returns:
        Ninguno. Imprime la tabla formateada en la consola.
    """

    table = Table(title="Incidencias Informáticas", show_lines=True)

    # Definir las columnas de la tabla
    table.add_column("Marca Temporal", justify="center", style="green")
    table.add_column("Usuario", style="blue")
    table.add_column("Sala", style="yellow")
    table.add_column("Equipo", style="yellow")
    table.add_column("Tipo de Incidencia", style="cyan")
    table.add_column("Urgencia", style="magenta")

    # Agregar las filas a la tabla
    for incidencia in datos:
        urgencia_color = obtener_color_urgencia(incidencia['Nivell Urgència de Solució'])
        table.add_row(
            incidencia['Marca temporal'],
            incidencia['Nom i cognoms'],
            incidencia['AULA - SALA'],
            incidencia['Nº de equip afectat'],
            incidencia['Tipus d\'incidència'],
            f"[{urgencia_color}]{incidencia['Nivell Urgència de Solució']}[/{urgencia_color}]"
        )

    print(table)

# Datos de las incidencias en formato Python
datos_incidencias = [
    {
        'Marca temporal': '4/10/2024 8:41:00',
        'Email': 'cristina.martinez@itb.cat',
        'Nom i cognoms': 'Cristina Martínez',
        'Data de la incidència': '4/10/2024',
        'Sistema operatiu': 'Windows',
        'AULA - SALA': '315',
        'Nº de equip afectat': 'PQR-901',
        'Tipus d\'incidència': 'Hardware',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Urgent'
    },
    {
        'Marca temporal': '4/10/2024 8:42:15',
        'Email': 'javier.lopez@itb.cat',
        'Nom i cognoms': 'Javier López',
        'Data de la incidència': '4/10/2024',
        'Sistema operatiu': 'Linux',
        'AULA - SALA': '316',
        'Nº de equip afectat': 'STU-234',
        'Tipus d\'incidència': 'Xarxa',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Molt Urgent'
    },
    {
        'Marca temporal': '4/10/2024 8:43:30',
        'Email': 'alicia.rivera@itb.cat',
        'Nom i cognoms': 'Alicia Rivera',
        'Data de la incidència': '4/10/2024',
        'Sistema operatiu': 'Mac',
        'AULA - SALA': '317',
        'Nº de equip afectat': 'VWX-567',
        'Tipus d\'incidència': 'Software',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Urgent'
    },
    {
        'Marca temporal': '4/10/2024 8:44:45',
        'Email': 'pedro.morales@itb.cat',
        'Nom i cognoms': 'Pedro Morales',
        'Data de la incidència': '4/10/2024',
        'Sistema operatiu': 'Windows',
        'AULA - SALA': '318',
        'Nº de equip afectat': 'YZA-890',
        'Tipus d\'incidència': 'Projector',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Molt Urgent'
    },
    {
        'Marca temporal': '4/10/2024 8:45:00',
        'Email': 'maria.jimenez@itb.cat',
        'Nom i cognoms': 'María Jiménez',
        'Data de la incidència': '4/10/2024',
        'Sistema operatiu': 'Linux',
        'AULA - SALA': '319',
        'Nº de equip afectat': 'BCD-123',
        'Tipus d\'incidència': 'Caiguda Total',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Urgent'
    },
    {
        'Marca temporal': '1/5/2024 9:00:00',
        'Email': 'fernando.ramos@itb.cat',
        'Nom i cognoms': 'Fernando Ramos',
        'Data de la incidència': '5/1/2024',
        'Sistema operatiu': 'Windows',
        'AULA - SALA': '320',
        'Nº de equip afectat': 'ABC-321',
        'Tipus d\'incidència': 'Hardware',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Urgent'
    },
    {
        'Marca temporal': '2/5/2024 10:15:30',
        'Email': 'monica.garcia@itb.cat',
        'Nom i cognoms': 'Monica García',
        'Data de la incidència': '5/2/2024',
        'Sistema operatiu': 'Linux',
        'AULA - SALA': '321',
        'Nº de equip afectat': 'XYZ-654',
        'Tipus d\'incidència': 'Xarxa',
        'Captura del problema si es possible': '',
        'Nivell Urgència de Solució': 'Molt Urgent'
    }
]

# Llamar a la función para mostrar la tabla
formatear_incidencias(datos_incidencias)