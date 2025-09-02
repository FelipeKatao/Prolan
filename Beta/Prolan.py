
    

class Prolan:
    def __init__(self):
        self.DictionaryBase = {}
        self.Intent = {}
        self.VectorResult = []
        self.StopSetences = []
        self.ImportantTerm = 1
        self.ErrorIntent = "Intent error: Not exists"
        self.GetContext = []
        self.KeyContext = []
        self.flag = False


    def Tokenize(self,Text:str):
        List_Tokens = ""
        self.flag  = False
        for i in Text.split(" "):
             v = self.DictionaryBase.get(i.lower())
             if v is not None:
                List_Tokens+= str(v.get("Id"))
                self.VectorResult.append(str(v.get("Id")))
                # if self.flag == True:
                #     self.GetContext.append(i)
                if str(v.get("Type")) == "2":
                    self.flag = True
                    self.GetContext.append([])
                    self.KeyContext.append(i)
                else:
                    self.flag = False
             else:
                if self.flag == True:
                    self.GetContext[len(self.GetContext)-1].append(i)
                
        if List_Tokens == "" : List_Tokens =0
        return int(List_Tokens)
    
    def CreateVector2d(self):
        Dict_base = {}
        id_base = 0 
        for i in self.KeyContext:
            Dict_base[i+str(id_base)] = [self.GetContext[id_base]]            
            id_base+=1
        return Dict_base

    def ReturnData(self,Text:str):
        
        return self.Intent.get(self.Tokenize(Text),self.ErrorIntent)
    
    def AddNewWord(self,Word,Id,Type,op):
        self.DictionaryBase[Word.lower()] = {"Id":Id,"Type":Type,"Bias":op}
    
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
        self.bias = []
        self.FeaturesCalcs = []
        if self.Object:
             self.Value =  [self.CreateVector()]
             self.CreateProps()

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
                if Value != 0 : 
                    Tokens.append(Value["Id"]) 
                    self.bias.append(Value["Bias"])
                else:  
                    if len(x) >=1:
                        self.bias.append(0)
                        Tokens.append(0)
        return Tokens
    
    def CreateProps(self):
        self.FeaturesCalcs = []
        value_valid = 0
        for i in self.ClearZeros():
            for x in i:
                value_valid+=1
        self.FeaturesCalcs.append(value_valid)
        self.FeaturesCalcs.append((abs(len(self.Value) - value_valid)))
        self.FeaturesCalcs.append(self.Med())
        self.FeaturesCalcs.append(self.bias)
        return self.FeaturesCalcs

    def Med(self):
        value_ = 0
        for i in self.Value:
            for x  in i:
                value_ +=int(x)
        return value_/len(self.Value)

    def ClearZeros(self):
        return [[x for x in y if x!=0] for y in self.Value]   



        

v =  Prolan()
v.AddNewIntent(132,"Criacao_variavel","Criar uma variavel")
v.AddNewIntent(125,"Criacao_variavel_valor","Criar uma variavel com valor")
v.AddNewWord("Criar",1,"",1)
v.AddNewWord("variavel",2,2,0.5)
v.AddNewWord("Nova",3,"",0.5)
v.AddNewWord("valor",5,2,0.5)
Frase = "Eu quero criar   uma  nova variavel chamada abc criar variavel com valor 4"

# criação de um novo tipo chamda Vetor de tokens
Vetor = TokenVector(v,Frase)
print(Vetor.ClearZeros())
print(Vetor.FeaturesCalcs)
v.Tokenize(Frase)

print(v.GetContext)
print(v.KeyContext)
print(v.CreateVector2d())