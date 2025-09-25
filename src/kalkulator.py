# Početna verzija kalkulatora
def saberi(a, b):
    return a + b

def main():
    print("Kalkulator")
    a = float(input("Unesite prvi broj: "))
    b = float(input("Unesite drugi broj: "))
    print("Rezultat:", saberi(a, b))

if __name__ == "__main__":
    main()
