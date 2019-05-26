# -*- coding: utf-8 -*-

import sqlite3
import urllib.request


def findComma(s):
    return[i for i, character in enumerate(s) if character == ';']

def readFromFileToBase(url,db):


    file = urllib.request.urlopen(url).read()
    c = db.cursor()

    polish_letters = {165:'Ą', 198: 'Ć ', 202:'Ę', 163:'Ł', 209: 'Ń', 211: 'Ó', 140:'Ś', 143:'Ź', 175:'Ż', 185:'ą',
                      230:'ć', 234:'ę', 179:'ł', 241:'ń', 243:'ó', 156:'ś', 159:'ź', 191:'ż'}
    line = ""
    count_lines = 0

    for character in file:

        if(character == 10):

            count_lines += 1
            if count_lines != 1:

                commas = findComma(line)

                table_row = []
                table_row.append(line[1:commas[0]])
                table_row.append(line[commas[0]+1:commas[1]])
                table_row.append(line[commas[1]+1:commas[2]])
                table_row.append(line[commas[2]+1:commas[3]])
                table_row.append(line[commas[3] + 1:len(line)-1])

                c.execute("""INSERT INTO matury VALUES (?,?,?,?,?)""", table_row)




            line = ""

        if character in polish_letters:
            line = line + polish_letters[character]
        else:
            line= line + chr(character)

def recognizeSex(sex):
    if sex.lower() == 'k':
        sex =  'kobiety'
    elif sex.lower() == 'm':
        sex = 'mężczyźni'
    elif sex == "":
        sex = ""
    else:
        print("Podano zły parametr płci. Podaj K dla kobiet lub M dla mężczyzn. Nie podawaj nic jeżeli dla obu.")
    return sex

def getListOfYears():
    base = sqlite3.connect('matury.db')
    c = base.cursor()

    c.execute("""SELECT Rok
                                   FROM matury
                                   WHERE Przystąpiło_zdało =  ?
                                   AND Płeć = ?
                                   """, ('przystąpiło', 'kobiety'))

    get = [item[0] for item in c.fetchall()]
    base.close()

    years = []
    for g in get:
        if g not in years:
            years.append(g)

    return years

def getVoivodshipsList():
    base = sqlite3.connect('matury.db')
    c = base.cursor()

    c.execute("""SELECT Terytorium
                            FROM matury
                            WHERE Przystąpiło_zdało =  ?
                            AND Płeć = ?
                            """, ('przystąpiło',  'kobiety'))

    get = [item[0] for item in c.fetchall()]

    base.close()

    voivodships = []
    for g in get:
        if g not in voivodships:
            voivodships.append(g)
    return voivodships

def howManyParticipated(voivodships, sex, years):
    participated = []

    base = sqlite3.connect('matury.db')
    c = base.cursor()
    for x in voivodships:
        for y in years:
            c.execute("""SELECT Liczba_osób
                           FROM matury
                          WHERE Przystąpiło_zdało = ?
                          AND Terytorium = ?
                          AND Płeć = ?
                          AND Rok = ?
                          """, ('przystąpiło', x, sex, y))
            participated.append(c.fetchone()[0])
    base.close()
    return participated

def howManyPassed(voivodships, sex, years):
    passed = []

    base = sqlite3.connect('matury.db')
    c = base.cursor()
    for x in voivodships:
        for y in years:
            c.execute("""SELECT Liczba_osób
                           FROM matury
                          WHERE Przystąpiło_zdało = ?
                          AND Terytorium = ?
                          AND Płeć = ?
                          AND Rok = ?
                          """, ('zdało', x, sex, y))
            passed.append(c.fetchone()[0])
    base.close()
    return passed

def calculatePassRate(voivodships, sex, years):
    if sex:
        passed = howManyPassed(voivodships, sex, years)
        participated = howManyParticipated(voivodships, sex, years)
    else:
        male_participated = howManyParticipated(voivodships, 'mężczyźni', years)
        female_participated = howManyParticipated(voivodships, 'kobiety', years)
        participated = [f + m for f, m in zip(female_participated, male_participated)]
        male_passed = howManyPassed(voivodships, 'mężczyźni', years)
        female_passed = howManyPassed(voivodships, 'kobiety', years)
        passed = [f + m for f, m in zip(female_passed, male_passed)]

    pass_rate = [x / y for x, y in zip(passed, participated)]
    return pass_rate

def checkYear(year):
    exists = True
    if year not in getListOfYears():
        exists = False
        print(year,": podanego roku nie ma w bazie")
    return exists

def isNumber(year):
    number = False
    if year.isdigit():
        number = True

    else:
        print(year,": to nie jest prawidłowo podany rok")
    return number


def checkVoivodship(voivodship):
    exists = True
    if voivodship not in getVoivodshipsList():
        exists = False
        print(voivodship,": podanego województwa nie ma w bazie")
    return exists

def makeBase():

    link = 'https://www.dane.gov.pl/media/resources/20190520/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv'
    base = sqlite3.connect('matury.db')
    c = base.cursor()

    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='matury' ''')

    if c.fetchone()[0] != 1 :
        c.execute("""CREATE TABLE matury (
                    Terytorium text,
                    Przystąpiło_zdało text,
                    Płeć text,
                    Rok integer,
                    Liczba_osób integer
                    )""")
        readFromFileToBase(link,base)

    base.commit()
    base.close()

class Average:      


    def __init__(self, command):
        self.voivodship = ""
        self.year = 0
        self.sex = ""
        self.sum = 0
        self.amount = 0
        self.avr = 0
        self.command = command.replace(" ","")
        if self.interpretor() ==  True:
            self.calculate()
            self.show()

    def interpretor(self):
        correct = True
        self.commas = findComma(self.command)

        if len(self.commas)==1:
            self.voivodship = self.command[:self.commas[0]].lower().capitalize()
            correct = isNumber(self.command[self.commas[0]+1:])
            if correct:
                self.year = int(self.command[self.commas[0]+1:])
                correct = checkYear(self.year)
        elif len(self.commas)==2:
            self.voivodship = self.command[:self.commas[0]].lower().capitalize()
            correct = isNumber(self.command[self.commas[0] + 1:self.commas[1]])
            if correct:
                self.year = int(self.command[self.commas[0] + 1:self.commas[1]])
                correct = checkYear(self.year)
            self.sex = self.command[self.commas[1]+1:]
            self.sex = recognizeSex(self.sex)
            if self.sex != 'kobiety' and self.sex != 'mężczyźni' and self.sex != "":
                correct = False

        else:
            correct = False
            print("Podano złą ilość parametrów. Podaj kolejno: Województwo, rok, płeć (opcjonalnie). Parametry oddzielaj średnikiem. ")

        if correct:
            if checkVoivodship(self.voivodship)  != True:
                correct = False

        return correct

    def calculate(self):
        all_years = getListOfYears()
        years = []
        for y in all_years:
            if y <= self.year:
                years.append(y)
        v =[]
        v.append(self.voivodship)

        if self.sex:

            sum = 0
            participated = howManyPassed(v,self.sex,years)
            for p in participated:
                sum = sum + p

        else:
            sum = 0

            participated_female = howManyParticipated(v, 'kobiety', years)
            participated_male = howManyParticipated(v, 'mężczyźni', years)
            for m, f in zip(participated_male, participated_female):
                sum = sum + m + f



        self.avr = sum/len(years)


    def show(self):
        print("Na przestrzeni lat do roku",self.year,"włącznie, w województwie",self.voivodship,"średnia wynosi:", round(self.avr,2))


class PercentagePassRate:
    def __init__(self,command):
        self.voivodship = []
        self.sex = ""
        self.command = command.replace(" ", "")
        if self.interpretor():
            self.calculate()
            self.show()

    def interpretor(self):
        correct = True
        self.commas = findComma(self.command)

        if len(self.commas) == 1:
            self.voivodship.append((self.command[:self.commas[0]]).lower().capitalize())
            self.sex = self.command[self.commas[0] + 1:]
            self.sex = recognizeSex(self.sex)
            if self.sex != "mężczyźni" and self.sex != "kobiety" and self.sex != "":
                correct = False
        elif len(self.commas) == 0:
            self.voivodship.append(self.command.lower().capitalize())
        else:
            correct = False
            print("Zła ilość parametrów. Podaj województwo i opcjpnalnie płeć (k,m,lub nie podawaj jeżeli dla obu). Parametry należy roździelić średnikiem")
        if correct:
            correct = checkVoivodship(self.voivodship[0])
        return correct

    def calculate(self):
        self.years = getListOfYears()
        self.pass_rate = calculatePassRate(self.voivodship, self.sex, self.years)



    def show(self):
        for p,y in zip(self.pass_rate, self.years):
            print(y," - ",round(p*100, 2),"%")

class TheBestPassRate:
    def __init__(self, command):
        self.sex = ""
        self.year = []
        self.command = command.replace(" ", "")
        x = self.interpretor()
        if x:
            self.calculate()
            self.show()




    def interpretor(self):

        correct = True
        self.commas = findComma(self.command)
        if len(self.commas) == 1:
            correct = isNumber(self.command[:self.commas[0]])
            if correct:
                self.year.append(int(self.command[:self.commas[0]]))
                correct = checkYear(self.year[0])
            self.sex = self.command[self.commas[0] + 1:]
            self.sex = recognizeSex(self.sex)
        elif len(self.commas) == 0:
            correct = isNumber(self.command)
            if correct:
                self.year.append(int(self.command))
                correct = checkYear(self.year[0])
        else:
            correct = False
            print("Zła ilość parametrów. Podaj rok i opcjpnalnie płeć (k,m,lub nie podawaj jeżeli dla obu). Parametry należy roździelić średnikiem")
        return correct



    def calculate(self):
        self.voivodships = getVoivodshipsList()
        self.pass_rate = calculatePassRate(self.voivodships,self.sex,self.year)

    def show(self):
        highiest = max(self.pass_rate)
        voivodships_with_highiest = []
        highiest_pos = [i for i, x in enumerate(self.pass_rate) if x == highiest ]
        for x in highiest_pos:
            voivodships_with_highiest.append(self.voivodships[x])
        for x in voivodships_with_highiest:
            print(self.year[0],": Województwo",x, ". Zdało: ",round(highiest*100, 2),"% osób.")


class Comparision:
    def __init__(self,command):
        self.command = command.replace(" ", "")
        if self.interpretor() == True:
            self.calculate()

    def interpretor(self):
        correct = True
        self.sex = ""
        self.voivodship1 = []
        self.voivodship2 = []
        self.commas = findComma(self.command)

        if len(self.commas) == 1:
            self.voivodship1.append(self.command[:self.commas[0]].lower().capitalize())
            self.voivodship2.append(self.command[self.commas[0]+1:].lower().capitalize())
        elif  len(self.commas) == 2:
            self.voivodship1.append(self.command[:self.commas[0]].lower().capitalize())
            self.voivodship2.append(self.command[self.commas[0] + 1:self.commas[1]].lower().capitalize())
            self.sex = self.command[self.commas[1]+1:]
            self.sex = recognizeSex(self.sex)
            if self.sex != 'kobiety' and self.sex != 'mężczyźni' and self.sex != "":
                correct = False
        else:
            correct = False
            print("Podano złą ilość parametrów. Podaj kolejno: Pierwsze Województwo, drugie województwo, płeć (opcjonalnie). Parametry oddzielaj średnikiem. ")
        if correct:
            if checkVoivodship(self.voivodship1[0]) != True:
                correct = False
            elif checkVoivodship(self.voivodship2[0]) != True:
                correct = False
        return correct

    def calculate(self):
        years = getListOfYears()
        v1 = calculatePassRate(self.voivodship1,self.sex,years)
        v2 = calculatePassRate(self.voivodship2, self.sex, years)
        i = 0
        for x, y in zip(v1,v2):
            if x>y:
                print(years[i],": Województwo",self.voivodship1[0])
            elif y>x:
                print(years[i], ": Województwo", self.voivodship2[0])
            else:
                print(years[i], ": Województwo", self.voivodship1[0],"i",self.voivodship2[0],"taki sam współczynnik zdawalności.")
            i += 1

class Regression:            
    def __init__(self,command):
        self.command = command.replace(" ", "")
        self.sex = ""
        if self.interpretor():
            self.calculate()

    def interpretor(self):
        correct = True
        if self.command != "":
            self.sex = recognizeSex(self.command)
            if self.sex != 'mężczyźni' and self.sex != "kobiety" and self.sex !="":
                correct = False

        return correct

    def calculate(self):
        years_list = getListOfYears()
        voivodships_list = getVoivodshipsList()
        for v in voivodships_list:
            if v != 'Polska':
                voivodship = []
                voivodship.append(v)
                passRateList = calculatePassRate(voivodship,self.sex,years_list)
                i = 0
                for x, y in zip(passRateList[::], passRateList[1::]):
                    if x > y:
                        print("Województwo",voivodship[0],years_list[i],"(",round(x*100,2),"%)","-->",years_list[i+1],"(",round(y*100,2),"%)")
                    i += 1


def app(text):
    run = True
    text = text.replace(" ", "")
    opening_bracket = -1
    closing_bracket = -1
    opening_bracket = text.find("(")
    closing_bracket = text.find(")")

    if text.lower() == 'x':
        run = False
    elif opening_bracket >= 0 and closing_bracket >= 0 and closing_bracket > opening_bracket:

        command = text[:opening_bracket]
        parameters = text[opening_bracket + 1:closing_bracket]

        if command.lower() == "srednia":
            execute = Average(parameters)
        elif command.lower() == "zdawalnosc":
            execute = PercentagePassRate(parameters)
        elif command.lower() == 'najlepsza':
            execute = TheBestPassRate(parameters)
        elif command.lower() == 'regresja':
            execute = Regression(parameters)
        elif command.lower() == 'porownaj':
            execute = Comparision(parameters)
        else:
            print("Nie rozpoznano komendy.")
    else:
        print("Błędna komenda. Format komend: nazwa_operacji(parametr1;parametr2;...)")

    return run

def main():

    makeBase()
    run = True
    while(run):
        print("Podaj x, aby zakończyć")
        text = input(">> ")
        run = app(text)
main()



