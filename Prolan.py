
import sys
import Engine.ProgEngine as d


def ModeInline():
        f = open(sys.argv[3],"r")
        for i in f.readlines():
            if i[0] == '#':
                continue
            Eng.ResponseData(i)

def ModeText():
    f = open(sys.argv[3],"r")
    ContextValue= ""
    for i in f.readlines():
            if i[0] == '#':
                continue
            ContextValue += i.replace("\n","")
    Eng.GetContextData(ContextValue)

if len(sys.argv) > 1:
    argumento = sys.argv[1]
    Eng =  d.ProgEngine()
    if argumento ==  "open":
        if sys.argv[2] == "text-mode":
            # mode Text
            ModeText()
        else:
             ModeInline()
else:
    print("Nenhum argumento foi passado.")

