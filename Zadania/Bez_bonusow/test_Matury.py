import Matury


def test_srednia(capfd):

    Matury.app("srednia(Pomorskie;2016)")
    out, err = capfd.readouterr()
    assert out == "Na przestrzeni lat do roku 2016 włącznie, w województwie Pomorskie średnia wynosi: 17595.71\n"

    Matury.app("srednia(pomorskie;2016;)")
    out, err = capfd.readouterr()
    assert out == "Na przestrzeni lat do roku 2016 włącznie, w województwie Pomorskie średnia wynosi: 17595.71\n"

    Matury.app("srednia(l u b e l sk IE;2011;k)")
    out, err = capfd.readouterr()
    assert out == "Na przestrzeni lat do roku 2011 włącznie, w województwie Lubelskie średnia wynosi: 10156.0\n"

    Matury.app("srednia(LUBELSKIE;2011;m)")
    out, err = capfd.readouterr()
    assert out == "Na przestrzeni lat do roku 2011 włącznie, w województwie Lubelskie średnia wynosi: 7685.0\n"

    Matury.app("srednia(LUBELSKIE;2011;m;k)")
    out, err = capfd.readouterr()
    assert out == "Podano złą ilość parametrów. Podaj kolejno: Województwo, rok, płeć (opcjonalnie). Parametry oddzielaj średnikiem. \n"

    Matury.app("srednia(Gdańskie;2011;m)")
    out, err = capfd.readouterr()
    assert out == "Gdańskie : podanego województwa nie ma w bazie\n"

    Matury.app("srednia(Małopolskie;2004)")
    out, err = capfd.readouterr()
    assert out == "2004 : podanego roku nie ma w bazie\n"


def test_zdawalnosc(capfd):
    Matury.app("zdawalnosc(kujawsko-pomorskie)")
    out, err = capfd.readouterr()
    assert out == "2010  -  82.87 %\n2011  -  75.07 %\n2012  -  80.48 %\n2013  -  81.67 %\n2014  -  70.9 %\n2015  -  73.35 %\n2016  -  78.57 %\n2017  -  77.99 %\n2018  -  78.21 %\n"

    Matury.app("zdawalnosc(lubuskie;k;)")
    out, err = capfd.readouterr()
    assert out == "Zła ilość parametrów. Podaj województwo i opcjpnalnie płeć (k,m,lub nie podawaj jeżeli dla obu). Parametry należy roździelić średnikiem\n"

    Matury.app("zdawalnosc(Oregon;m)")
    out, err = capfd.readouterr()
    assert out == "Oregon : podanego województwa nie ma w bazie\n"

    Matury.app("zdawalnosc(małopOl skie;  K)")
    out, err = capfd.readouterr()
    assert out == "2010  -  83.65 %\n2011  -  77.15 %\n2012  -  82.52 %\n2013  -  84.46 %\n2014  -  74.09 %\n2015  -  77.5 %\n2016  -  82.13 %\n2017  -  83.27 %\n2018  -  83.76 %\n"

def test_najlepsza(capfd):
    Matury.app("najlepsza(2014)")
    out, err = capfd.readouterr()
    assert out == "2014 : Województwo Lubuskie . Zdało:  73.67 % osób.\n"

    Matury.app("na jle ps za(2016   ; M)")
    out, err = capfd.readouterr()
    assert out == "2016 : Województwo Małopolskie . Zdało:  82.13 % osób.\n"

    Matury.app("najlepsza(2016   ;; M)")
    out, err = capfd.readouterr()
    assert out == "Zła ilość parametrów. Podaj rok i opcjpnalnie płeć (k,m,lub nie podawaj jeżeli dla obu). Parametry należy roździelić średnikiem\n"

    Matury.app("najlepsza(abc   ; M)")
    out, err = capfd.readouterr()
    assert out == "abc : to nie jest prawidłowo podany rok\n"

    Matury.app("NAJLEPSZA (2012;k)")
    out, err = capfd.readouterr()
    assert out == "2012 : Województwo Małopolskie . Zdało:  82.52 % osób.\n"

def test_porownaj(capfd):

    Matury.app("porownaj (mazowieckie)")
    out, err = capfd.readouterr()
    assert out == "Podano złą ilość parametrów. Podaj kolejno: Pierwsze Województwo, drugie województwo, płeć (opcjonalnie). Parametry oddzielaj średnikiem. \n"

    Matury.app("porownaj (pomorsk ie; ki j ow skie)")
    out, err = capfd.readouterr()
    assert out == "Kijowskie : podanego województwa nie ma w bazie\n"

    Matury.app("porownaj (Dolnośląskie;świętokrzyskie;k)")
    out, err = capfd.readouterr()
    assert out == "2010 : Województwo Świętokrzyskie\n2011 : Województwo Świętokrzyskie\n2012 : Województwo Dolnośląskie\n2013 : Województwo Dolnośląskie\n2014 : Województwo Świętokrzyskie\n2015 : Województwo Świętokrzyskie\n2016 : Województwo Świętokrzyskie\n2017 : Województwo Świętokrzyskie\n2018 : Województwo Świętokrzyskie\n"

    Matury.app("porownaj (świętokrzyskie;dolnośląskie)")
    out, err = capfd.readouterr()
    assert out == "2010 : Województwo Dolnośląskie\n2011 : Województwo Świętokrzyskie\n2012 : Województwo Dolnośląskie\n2013 : Województwo Dolnośląskie\n2014 : Województwo Świętokrzyskie\n2015 : Województwo Świętokrzyskie\n2016 : Województwo Świętokrzyskie\n2017 : Województwo Świętokrzyskie\n2018 : Województwo Świętokrzyskie\n"

    Matury.app("porownaj (wielkopolskie;zachodniopomorskie;a)")
    out, err = capfd.readouterr()
    assert out == "Podano zły parametr płci. Podaj K dla kobiet lub M dla mężczyzn. Nie podawaj nic jeżeli dla obu.\n"


def test_regresja(capfd):

    Matury.app("regresja(a)")
    out, err = capfd.readouterr()
    assert out == "Podano zły parametr płci. Podaj K dla kobiet lub M dla mężczyzn. Nie podawaj nic jeżeli dla obu.\n"

    Matury.app("regresja()")
    out, err = capfd.readouterr()
    assert out == "Województwo Dolnośląskie 2010 ( 81.95 %) --> 2011 ( 74.81 %)\nWojewództwo Dolnośląskie 2013 ( 80.6 %) --> 2014 ( 69.21 %)\n\
Województwo Dolnośląskie 2016 ( 77.38 %) --> 2017 ( 76.08 %)\n\
Województwo Kujawsko-pomorskie 2010 ( 82.87 %) --> 2011 ( 75.07 %)\n\
Województwo Kujawsko-pomorskie 2013 ( 81.67 %) --> 2014 ( 70.9 %)\n\
Województwo Kujawsko-pomorskie 2016 ( 78.57 %) --> 2017 ( 77.99 %)\n\
Województwo Lubelskie 2010 ( 79.83 %) --> 2011 ( 74.03 %)\n\
Województwo Lubelskie 2013 ( 80.26 %) --> 2014 ( 70.23 %)\n\
Województwo Lubelskie 2016 ( 79.41 %) --> 2017 ( 77.81 %)\n\
Województwo Lubuskie 2010 ( 82.32 %) --> 2011 ( 76.65 %)\n\
Województwo Lubuskie 2013 ( 83.15 %) --> 2014 ( 73.67 %)\n\
Województwo Lubuskie 2016 ( 81.52 %) --> 2017 ( 79.76 %)\n\
Województwo Lubuskie 2017 ( 79.76 %) --> 2018 ( 79.29 %)\n\
Województwo Łódzkie 2010 ( 81.91 %) --> 2011 ( 76.0 %)\n\
Województwo Łódzkie 2013 ( 80.55 %) --> 2014 ( 71.31 %)\n\
Województwo Łódzkie 2016 ( 79.89 %) --> 2017 ( 79.47 %)\n\
Województwo Łódzkie 2017 ( 79.47 %) --> 2018 ( 79.29 %)\n\
Województwo Małopolskie 2010 ( 82.57 %) --> 2011 ( 77.26 %)\n\
Województwo Małopolskie 2013 ( 83.54 %) --> 2014 ( 72.83 %)\n\
Województwo Mazowieckie 2010 ( 81.61 %) --> 2011 ( 76.4 %)\n\
Województwo Mazowieckie 2013 ( 80.93 %) --> 2014 ( 71.28 %)\n\
Województwo Mazowieckie 2016 ( 81.51 %) --> 2017 ( 80.33 %)\n\
Województwo Opolskie 2010 ( 81.96 %) --> 2011 ( 74.94 %)\n\
Województwo Opolskie 2013 ( 80.8 %) --> 2014 ( 69.85 %)\n\
Województwo Opolskie 2016 ( 79.2 %) --> 2017 ( 77.61 %)\n\
Województwo Podkarpackie 2010 ( 80.97 %) --> 2011 ( 74.53 %)\n\
Województwo Podkarpackie 2013 ( 81.23 %) --> 2014 ( 70.64 %)\n\
Województwo Podkarpackie 2016 ( 80.05 %) --> 2017 ( 77.86 %)\n\
Województwo Podlaskie 2010 ( 80.81 %) --> 2011 ( 76.77 %)\n\
Województwo Podlaskie 2013 ( 81.83 %) --> 2014 ( 72.9 %)\n\
Województwo Podlaskie 2016 ( 80.89 %) --> 2017 ( 80.42 %)\n\
Województwo Pomorskie 2010 ( 81.65 %) --> 2011 ( 74.6 %)\n\
Województwo Pomorskie 2013 ( 80.8 %) --> 2014 ( 71.03 %)\n\
Województwo Pomorskie 2016 ( 79.45 %) --> 2017 ( 78.12 %)\n\
Województwo Pomorskie 2017 ( 78.12 %) --> 2018 ( 77.44 %)\n\
Województwo Śląskie 2010 ( 81.98 %) --> 2011 ( 75.74 %)\n\
Województwo Śląskie 2013 ( 81.58 %) --> 2014 ( 71.0 %)\n\
Województwo Śląskie 2016 ( 77.74 %) --> 2017 ( 77.31 %)\n\
Województwo Świętokrzyskie 2010 ( 80.09 %) --> 2011 ( 76.29 %)\n\
Województwo Świętokrzyskie 2013 ( 79.4 %) --> 2014 ( 71.08 %)\n\
Województwo Świętokrzyskie 2016 ( 80.1 %) --> 2017 ( 78.28 %)\n\
Województwo Warmińsko-Mazurskie 2010 ( 80.45 %) --> 2011 ( 73.3 %)\n\
Województwo Warmińsko-Mazurskie 2013 ( 80.03 %) --> 2014 ( 67.72 %)\n\
Województwo Warmińsko-Mazurskie 2016 ( 75.9 %) --> 2017 ( 74.07 %)\n\
Województwo Wielkopolskie 2010 ( 81.17 %) --> 2011 ( 75.39 %)\n\
Województwo Wielkopolskie 2013 ( 80.51 %) --> 2014 ( 69.85 %)\n\
Województwo Wielkopolskie 2016 ( 78.44 %) --> 2017 ( 78.0 %)\n\
Województwo Zachodniopomorskie 2010 ( 80.08 %) --> 2011 ( 73.24 %)\n\
Województwo Zachodniopomorskie 2013 ( 79.23 %) --> 2014 ( 66.78 %)\n\
Województwo Zachodniopomorskie 2016 ( 76.29 %) --> 2017 ( 74.2 %)\n"


    Matury.app("regresja(m)")
    out, err = capfd.readouterr()
    assert out != ""

    Matury.app("regresja(k)")
    out, err = capfd.readouterr()
    assert out != ""

