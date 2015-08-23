import sys
from model import Model

def main():
    modelfile = sys.argv[1]
    m = Model(modelfile)
    for i,atom in enumerate(m.atoms):
        atom.id = i
    m.write(modelfile, ext='dat')

if __name__ == '__main__':
    main()
