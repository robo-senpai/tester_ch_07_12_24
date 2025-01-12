import time
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

# ta funkcja wysyla pojedyncze zapytanie do naszego api
# i bedzie zwracala kod statusu (200, 400, 500 itp.)

def send_request():
    response = requests.get(url) # zapytania synchroniczne, czyli jedno po drugim
    return response.status_code

print('Rozpoczynamy prosty test, bedziemy wysylac 10 zapytan do API.')

start_time = time.time() # timestamp

# w petli bedziemy wysylac 10 zapytan

for i in range(10):
    status = send_request()
    print(f'Zapytanie nr {i + 1} ma status: {status}.')

end_time = time.time()

elapsed_time = end_time - start_time

print(f'Suma czasu dla 10 zapytan: {elapsed_time} sek.')