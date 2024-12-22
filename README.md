# Analizator Wyników

Aplikacja przewidująca wyniki na podstawie dostarczonych danych.

## 1. Klonowanie repozytorium

git clone https://github.com/twoje_uzytkownik/analizator-wynikow.git
cd analizator-wynikow

## 2. Uruchomienie lokalnie

Zainstaluj zależności:
pip install -r requirements.txt

Uruchom aplikację:
python app.py

Aplikacja będzie dostępna pod adresem:
http://localhost:5000

## 3. Uruchomienie z użyciem Dockera

Zbuduj obraz Dockera:
docker build -t analizator-wynikow .

Uruchom kontener:
docker run -p 5000:5000 analizator-wynikow

Aplikacja powinna działać pod adresem:
http://localhost:5000

## 4. Pobranie obrazu z Docker Hub

Pobierz obraz:
docker pull twoje_uzytkownik/analizator-wynikow

Uruchom obraz:
docker run -p 5000:5000 twoje_uzytkownik/analizator-wynikow

## 5. Testowanie API (Postman/Curl):
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"values\": [1, 2, 3]}"

Oczekiwana odpowiedź:
{"prediction": 6}