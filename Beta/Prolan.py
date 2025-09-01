
    

class Prolan:
    def __init__(self):
        self.DictionaryBase = {}
        self.Intent = {}
        self.VectorResult = []
        self.StopSetences = []
        self.ImportantTerm = 1
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
                if self.DictionaryBase.get(i)["Id"] == self.ImportantTerm and len(Sentence) >=self.ImportantTerm or self.DictionaryBase.get(i)["Id"] == self.ImportantTerm and len(Sentence_list) >=1:
                    Sentence_list.append(Sentence)
                    Sentence = ""
            Sentence+=i+" "
        Sentence_list.append(Sentence)
        return Sentence_list

class TokenVector:
    def __init__(self,ObjectProg:Prolan,Text:str):
        self.Object = ObjectProg
        self.Text = Text
        self.Value = None
        if self.Object:
             self.Value =  [self.CreateVector()]

    def __repr__(self):
        return str(self.Value)
    
    def __add__(self,val):
        self.Value.append(val)
        return self.Value

    def CreateVector(self):
        Text_sentence = self.Object.TrimBySentence(self.Text)
        Tokens = []
        for  i in Text_sentence:
            for x in i.split(" "):
                Value = self.Object.DictionaryBase.get(x,0)
                if Value != 0 : Tokens.append(Value["Id"]) 
                else:  
                    if len(x) >=1:
                        Tokens.append(0)
        return Tokens

    def ClearZeros(self):
        return [[x for x in y if x!=0] for y in self.Value]   



        

v =  Prolan()
v.AddNewIntent(132,"Criacao_variavel","Criar uma variavel")
v.AddNewIntent(125,"Criacao_variavel_valor","Criar uma variavel com valor")
v.AddNewWord("Criar",1,"","")
v.AddNewWord("variavel",2,"","")
v.AddNewWord("Nova",3,"","")
v.AddNewWord("valor",5,"","")
Frase = "Eu quero criar   uma  nova variavel criar variavel com valor 4"

# criação de um novo tipo chamda Vetor de tokens
Vetor = TokenVector(v,Frase)
print(Vetor.ClearZeros())
