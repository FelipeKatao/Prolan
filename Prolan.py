
import sys
import Engine.ProgEngine as d

if len(sys.argv) > 1:
    argumento = sys.argv[1]
    Eng =  d.ProgEngine()
    if argumento ==  "open":
        f = open(sys.argv[2],"r")
        for i in f.readlines():
            if i[0] == '#':
                continue
            Eng.ResponseData(i)
else:
    print("Nenhum argumento foi passado.")
