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
podczas porównania baz działek/konturów/użytków, każdy z katalogów powinien zawierać pliki "Dzialki.edz" oraz "Punkty.acs"

wynikiem działania programu będą następujące pliki:

- Dla warstw:

	- DODANE.txt
	- USUNIETE.txt
	
- Dla działek (zależnie od różnic w danych):

	- PKT_DODANE.txt
	- PKT_USUNIETE.txt
	- PKT_ZM_DANE_POD.txt
	- PKT_ZM_DANE_DOD.txt
	
Gdy w podanym katalogu brak będzie wymaganych plików zostanie wyświetlony komunikata o brak danych dla warstw lub dzialek/konturow/uzytkow.
	
	
Sposób użycia z wiersza poleceń::
	
	>>>python3 wapor_app.py ./data

W przypadku wystąpienia wyjątków, które nie zostały obsłużone
wszelkie informacje trafią do pliku \*.log

wapory - *"wyziewy, opary"* - gdyby ktoś był ciekaw skąd nazwa