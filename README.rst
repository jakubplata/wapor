============================
Aplikacja wapor
============================

Projekt ten ma na celu umożliwienie porównywania ze sobą warstw programu EwMapa.
Często w swojej pracy spotykam się z problemem porównywania warstw otrzymanych
w ramach kolejnych aktulizacji danych dla projektu.

W związku z czym utworzyłem to proste narzędzie, które umożliwa porównanie
danych w formacie tekstowym dla wielu warstw

Folder wejściowy powinien zawierać dwa folder:

- old
- new

w przypadku porównywania warstw, każdy z katalogów powinien zawierać plik "Warstwy"

wynikiem działania aplikacji będą dwa pliki:

- DODANE.txt
- USUNIETE.txt

Sposób użycia z wiersza poleceń::
	
	>>>python3 wapor_app.py ./data

W przypadku wystąpienia wyjątków, które nie zostały obsłużone
wszelkie informacje trafią do pliku \*.log

wapory - *"wyziewy, opary"* - gdyby ktoś był ciekaw skąd nazwa