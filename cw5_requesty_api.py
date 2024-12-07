import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
# response = requests.get("https://jsonplaceholder.typicode.com/user")  # bledna strona

if response.status_code == 200:
    print("Najs, strona dziala!")
    print("Dane uzytkownikow to: ", response.json())  # a dam rade wypisac po kolei?
else:
    print(f"Dammit wysypalo sie!Blad {response.status_code}")