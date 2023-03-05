import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticación
scope = ['https://docs.google.com/spreadsheets/d/15mfNe6tcfZYDBAdBxIyqlLs8sGKwy9ESkJ-uWz8LHAs/edit?usp=sharing', 'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)

# Conexión a la hoja de cálculo
sheet = client.open('Python + Sheets').sheet1

# Ingreso de datos
data = ['Dato 1', 'Dato 2', 'Dato 3']
sheet.append_row(data)

print("Datos agregados exitosamente.")
