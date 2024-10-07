import sys
from pathlib import Path 

def main():
    pass
    print(sys.argv)
    print(sys.argv[1])
    print(sys.argv[2])

    print(Path.cwd())
    print(Path.cwd().parent)

    raiz = Path.cwd().parent
    folder =Path("dna/dna/databases")

    archivo = raiz / folder / sys.argv[1]

    print(archivo)

    f = open(archivo)
    for linea in f:
        linea = linea.strip() ## linea = linea[:-1]
        linea = linea.split(",")
        print(linea)

if __name__ == "__main__":
    main()