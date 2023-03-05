from SortArray import*
import random
import timeit
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


def initArray(size=100, maxValue=100, seed=3.14159):
    """Create an Array of the specified size with a fixed sequence of
       'random' elements"""
    arr = Array(size)                   # Create the Array object
    random.seed(seed)                   # Set random number generator
    for i in range(size):               # to known state, then loop
        arr.insert(random.randrange(maxValue)) # Insert random numbers
    return arr                          # Return the filled Array

arr = initArray()
print("Array containing", len(arr), "items:\n", arr)

for test in ['initArray().bubbleSort()',
             'initArray().selectionSort()',
             'initArray().insertionSort()']:
    elapsed = timeit.timeit(test, number=100, globals=globals())
    print(test, "took", elapsed, "seconds", flush=True)

arr.insertionSort()
print('Sorted array contains:\n', arr)


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = 'https://docs.google.com/spreadsheets/d/15mfNe6tcfZYDBAdBxIyqlLs8sGKwy9ESkJ-uWz8LHAs/edit?usp=sharing'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Llamada a la api
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:A8').execute()
# Extraemos values del resultado
values = result.get('values',[])
print(values)


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = 'https://docs.google.com/spreadsheets/d/15mfNe6tcfZYDBAdBxIyqlLs8sGKwy9ESkJ-uWz8LHAs/edit?usp=sharing'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Debe ser una matriz por eso el doble [[]]
values = [['Prueba!']]
# Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")

from typing import List

def bubbleSort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertionSort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selectionSort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Leer datos de la hoja de cálculo
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:A8').execute()
values = result.get('values', [])

# Convertir los datos a una lista de enteros
data = [int(val[0]) for val in values]

# Ordenar los datos usando los distintos algoritmos de ordenamiento
print('Datos sin ordenar:', data)
print('Datos ordenados con bubbleSort:', bubbleSort(data))
print('Datos ordenados con insertionSort:', insertionSort(data))
print('Datos ordenados con selectionSort:', selectionSort(data))