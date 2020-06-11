#7. Dane na start wczytujemy z pliku(współrzędne obiektów) pierwsza linia to Robaczek, pozostałe to owoce
# owoce posiadaja 2 dodatkowe atrybuty: jedzenie i nazwa (ktory nalezy wczytac od tylu)
# przygotuj pakiet pliki(ma być możliwość wczytania wszystkiego za pomocą from pliki import * ) z modułem zapisy a w nim funkcję wczytaj
# powinna przyjmować jeden argument, którym jest ścieżka do pliku
# ma go otworzyć i wczytać dane generując słownik ze współrzędnymi dla obiektów w grze: { robaczek: {x:, y:}, owoce: [ {x:,y:, jedzenie:, nazwa:}..... ]}
# dane wczytaj za pomocą python comprehension
from pliki import *

sciezka = "data.txt"
dictionary = zapisy.wczytaj(sciezka)