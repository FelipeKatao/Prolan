

class Prolan:
    def __init__(self):
        self.DictionaryBase = {}
        self.Intent = {}
        self.VectorResult = []
        self.StopSetences = []
        self.ErrorIntent = "Intent error: Not exists"


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
        
        return self.Intent.get(self.Tokenize(Text),self.ErrorIntent)
    
    def AddNewWord(self,Word,Id,Type,op):
        self.DictionaryBase[Word.lower()] = {"Id":Id,"Type":Type,"Op":op}
    
    def AddNewIntent(self,Id,Name,Return):
        self.Intent[Id] = {"Name":Name,"Return":Return}

    def TrimBySentence(self,text:str):
        Sentence_list = []
        Sentence = ""
        for i in text.split(" "):
            if self.DictionaryBase.get(i):
                if self.DictionaryBase.get(i)["Id"] == 1 and len(Sentence) >=1 or self.DictionaryBase.get(i)["Id"] == 1 and len(Sentence_list) >=1:
                    Sentence_list.append(Sentence)
                    Sentence = ""
            Sentence+=i+" "
        Sentence_list.append(Sentence)
        return Sentence_list

v =  Prolan()
v.AddNewIntent(132,"Criacao_variavel","Criar uma variavel")
v.AddNewIntent(125,"Criacao_variavel_valor","Criar uma variavel com valor")
v.AddNewWord("Criar",1,"","")
v.AddNewWord("variavel",2,"","")
v.AddNewWord("Nova",3,"","")
v.AddNewWord("valor",5,"","")
print(v.TrimBySentence("Eu quero criar   uma  nova variavel criar variavel com valor 4 "))
#print(v.ReturnData("Eu quero criar   uma  nova variavel criar variavel com valor 4 ")["Return"])
Frase = v.TrimBySentence("Eu quero criar   uma  nova variavel criar variavel com valor 4 ")
for i in Frase:
    print(v.ReturnData(i))