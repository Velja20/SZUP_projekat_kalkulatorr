# Početna verzija kalkulatora
def saberi(a, b):
    return a + b

def oduzmi(a, b):
    return a - b

def mnozi(a, b):
    return a * b

def main():
    print("Kalkulator")
    print("Izaberite operaciju:")
    print("1. Sabiranje")
    print("2. Oduzimanje")
    print("3. Množenje")
    izbor = input("Unesite broj operacije (1/2/3): ")
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    if izbor == '1':
        print("Rezultat:", saberi(a, b))
    elif izbor == '2':
        print("Rezultat:", oduzmi(a, b))
    elif izbor == '3':
        print("Rezultat:", mnozi(a, b))
    else:
        print("Nepoznata operacija.")

if __name__ == "__main__":
    main()
