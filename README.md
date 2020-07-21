# Zadanie - tworzenie bazy danych na podstawie pliku csv i operacje na utworzonej bazie
Dzień dobry,
W niniejszym repozytorium umieściłem moje rozwiązania zadania.
W folderze głównym "Zadania" znajdują się trzy kolejne: 

- "Bez_bonusow", w którym znajduje się plik Matury.py z właściwym kodem, który nie zawiera żadnych dodatkowych bibliotek i nie 
są w nim realizowane zadania bonusowe. Oba zadania bonusowe znajdują się w dwóch pozostałych folderach. Oprócz pliku właściwego
znajdują się tu także analizowany plik csv oraz plik ze skryptem testującym. W celu uruchomienia skryptu należy umieścić plik Matury.py i plik csv i uruchomić skrypt, np. przez program Pycharm albo z wiersza ploeceń poleceniem >python Matury.py
W celu uruchomienia skryptu testowego należy umieścić plik test_Matury.py z wcześniej wymienionymi dwoma plikami w jednym folderze i uruchomić np. poleceniem >pytest test_Matury.py Matury.py

- "Bonus_database", w którym jest skrypt działający jak poprzedni, tylko że odczytuje plik csv tylko przy pierwszym uruchomieniu, kiedy tworzy bazę danych i zapisuje w niej dane z pliku csv. Po jednokrotnym utworzeniu bazy danych, skrypt operuje już tylko na niej realizując polecenia. Uruchomienie skryptu jak i jego testów w ten sam sposób co w poprzednim przypadku.

- "Bonus_url" zawiera skrypt, który również operuje na bazie danych, z tą różnicą, że nie pobiera danych z pliku csv z komputera, tylko poprzez adres url bezpośrednio z pliku umiesczonego na serwerze. Umożliwia to biblioteka urllib. Odczytywanie w tym 
przypadku wygląda inaczej, ponieważ otrzymyawne są dane pojedynczo (nie w liniach jak podczas czytania bezpośrednio z dysku) w postaci kolejnych znaków w kodzie ASCII. Kody te są odczytywane i zamieniane na odpowiednie znaki (w tym też znak końca linii czy średniki). Ponieważ polskich znaków nie ma w kodzie ACII, został stworzony słownik, który zamienia odpowiednie liczby na odpowiednie znaki polskie. Uruchomienie i testowanie skryptu jak wcześniej, tylko że nie jest wymagany plik csv. 


Wszystkie 3 skrypty z punktu widzenia użytkownika działają tak samo. W nieskończonej pętli skrypt prosi użytkownika o wpisanie komendy (znak zachęty ">>"). Z programu można wyjść wpisując "x" i zatwierdzając enterem (wielkość znaku czy spacje nie mają
znaczenia).

**WAŻNA WIADOMOŚĆ ODNOŚNIE TESTOWANIA:**
Ponieważ skrypty działają w pętli (dopóki nie poda się x aby wyjść) aby łatwiej było użytkownikowi wpisywać wiele komend, to aby 
przetestować skrypt za pomocą pytest należy wykomentować ostatnią linię kodu w skrypcie (main()).
main() --> #main()

**Główne zasady wpisywania komend**
- spacje i wielkość liter jest bez znaczenia
- należy zachować kolejność podawania parametrów
- wszystkie komendy w formacie jakaś_komenda(parametr1;parametr2;...)
- ważne jest aby zachować polskie znaki (np. województwo Slaskie nie zostanie rozpoznane - należy podać Śląskie)
- należy pamiętać aby parametry oddzielać średnikiem i zapisywać zbiórczo w nawiasie okrągłym
- płeć podaje się jako literę k dla kobiet i literę m dla mężczyzn. Jest opcjonalna dla każdej funkcji więc nie trzeba jej 
podawać, przy czym nie ma znaczenia czy nie poda się nic poza resztą wymaganych parametrów czy zostawi puste miejsce po ostatnimśredniku (płeć zawsze jest podawana na końcu)

1. Do obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie:   srednia(województwo;rok;płeć)
Przykładowe poprawne wywołania:

- srednia(Pomorskie;2016)
- srednia(śląskie;  2011;)
- srednia   ( MAŁOPOLSKIE ;2011;k)
- srednia (mało polskie; 20 28;M)

2. Do obliczenia procentowej zdawalności dla danego województwa na przestrzeni lat: zdawalnosc(województwo;płeć)
Przykładowe poprawne wywołania:

- zdawalnosc(Kujawsko - pomorskie;)
- zdawalnosc(kujawsko-pomorskie;k)
- zdawalnosc (Świętokrzyskie)
- zdawalnosc(Pomorskie;M)

3. Podanie województwa o najlepszej zdawalności w konkretnym roku : najlepsza(rok;płeć)
Przykładowe poprawne wywołania:

- najlepsza(2012)
- najlepsza(2012;m)
- najlepsza ( 2012 ; k)

4. Wykrycie województw, które zanotowały regresję: regresja(płeć)
Przykładowe poprawne wywołania:

- regresja()
- regresja(k)
- regresja(m)

5. Dla porównania dwóch województw (wypisanie, które miało lepszą zdawalność na przestrzeni lat): porownaj(województwo1;województwo2;płeć)

Przykładowe poprawne wywołania:

- porownaj(Pomorskie; Zachodniopomorskie;)
- porownaj (Zachodniopomorskie; Pomorskie)
- porownaj ( świętokrzyskie ; warminsko- mazurskie;k)
- porown aj( małopolskie; WIELKOPOLSKIE; M)


