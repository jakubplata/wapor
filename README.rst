============================
Aplikacja wapor
============================

Projekt ten ma na celu umożliwienie porównywania ze sobą warstw programu EwMapa.
Często w swojej pracy spotykam się z problemem porównywania warstw otrzymanych
w ramach kolejnych aktulizacji danych dla projektu.

W związku z czym utworzyłem to proste narzędzie, które umożliwa porównanie
danych w formacie tekstowym dla wielu warstw

Folder wejściowy powinien zawierać dwa pliki:
- Warstwy_old
- Warstwy_new

wynikiem działania aplikacji będą dwa pliki:
- DODANE.txt
- USUNIETE.txt

Sposób użycia z wiersza poleceń::
	
	>>>python wapor.py ./data
