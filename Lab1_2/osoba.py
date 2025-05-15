class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def opisz(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek} lat")


class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, numer_indeksu):
        super().__init__(imie, nazwisko, wiek)
        self.numer_indeksu = numer_indeksu

    def opisz(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek} lat, indeks: {self.numer_indeksu}")


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def opisz(self):
        print(f"{self.imie} {self.nazwisko}, {self.wiek} lat, stanowisko: {self.stanowisko}, pensja: {self.pensja} zł")


if __name__ == '__main__':
# Przykład użycia:
    student1 = Student("Anna", "Nowak", 22, "s12345")
    student1.opisz()  # Wynik: Anna Nowak, 22 lat, indeks: s12345
