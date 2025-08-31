

class Prolan:
    def __init__(self):
        self.DictionaryBase = {}
        self.Intent = {}
        self.VectorResult = []
        self.StopSetences = []


    def Tokenize(self,Text:str):
        List_Tokens = ""
        for i in Text.split(" "):
             v = self.DictionaryBase.get(i.lower())

             if v is not None:
                List_Tokens+= str(v.get("Id"))
                self.VectorResult.append(str(v.get("Id")))
        if List_Tokens == "" : List_Tokens =0
        return int(List_Tokens)
    
    def ReturnData(self,Text:str):
        return self.Intent[self.Tokenize(Text)]["Return"]


v =  Prolan()
v.DictionaryBase = {"abacaxi":{"Id":5,"Type":"adj","Op":0}}
v.DictionaryBase["eu"] = {"Id":1,"Type":"adj","Op":0}
v.DictionaryBase["quero"] = {"Id":3,"Type":"adj","Op":0}
v.Intent[135] = {"Id":135,"Return":"Você quer comer abacaxi?"}
print(v.ReturnData("Eu quero AbAcaxi de frutas"))
print(v.VectorResult)