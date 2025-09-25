# Jednostavan kalkulator za četiri osnovne operacije

def saberi(a, b):
    """Vraća zbir dva broja."""
    return a + b

def oduzmi(a, b):
    """Vraća razliku dva broja."""
    return a - b

def mnozi(a, b):
    """Vraća proizvod dva broja."""
    return a * b

def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje sa nulom nije dozvoljeno!")
    return a / b

# U main funkciji:
    try:
        if izbor == '4':
            ispisi_rezultat(deli(prvi_broj, drugi_broj))
    except ValueError as e:
        print(e)
def main():
    print("Kalkulator")
    print("Izaberite operaciju:")
    print("1. Sabiranje")
    print("2. Oduzimanje")
    print("3. Množenje")
    print("4. Deljenje")
    izbor = input("Unesite broj operacije (1/2/3/4): ")
    prvi_broj = float(input("Unesite prvi broj: "))
    drugi_broj = float(input("Unesite drugi broj: "))
    if izbor == '1':
        print("Rezultat:", saberi(prvi_broj, drugi_broj))
    elif izbor == '2':
        print("Rezultat:", oduzmi(prvi_broj, drugi_broj))
    elif izbor == '3':
        print("Rezultat:", mnozi(prvi_broj, drugi_broj))
    elif izbor == '4':
        print("Rezultat:", deli(prvi_broj, drugi_broj))
    else:
        print("Nepoznata operacija.")

if __name__ == "__main__":
    main()
