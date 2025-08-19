
import joblib

class ProgEngine():
    def __init__(self):
        self.Text = ""
        self.Pipeline = ""
        self.ReturnData = []

    def GetContextData(self,textMode:str):
       textMode = textMode.split(",")
       CountWords = len(textMode)-1
       Sentences = []
       for i in textMode:
            self.ResponseData(i)


    def ResponseData(self,Text):
        self.Pipeline = Text
        self.ReturnData = {
            "Action": self.GetAction(Text).split("np.str_")[0],
            "Target": self.GetTarget(Text).split("np.str_")[0],
            "Vars": Text
        }
        self.GenerateFilePython([self.ReturnData["Action"],self.ReturnData["Target"]],self.ReturnData)
        return self.ReturnData

    def GetAction(self,text):
        self.Pipeline = joblib.load(r"Model\Action_model.pkl")
        pred = self.Pipeline.predict([text])[0]
        return str(pred)
    
    def GetTarget(self,text):
        self.Pipeline = joblib.load(r"Model\Element_model.pkl")
        pred = self.Pipeline.predict([text])[0]
        return str(pred)
    
    def VarElements(self,text):
        Var_with = text.split('"')
        return Var_with[1]
    
    def GenerateFilePython(self,Value,Context,Output="test.py"):

        p = open(Output,"a")
        ValueCompiler = self.GetEngine(Value)
        ValueCompiler = self.GetContext(Context,ValueCompiler)
        p.write(ValueCompiler)
        p.close()
        

    def GetContext(self,Context,Interpreter):
        if "&T*" in Interpreter:
            values = Context["Vars"].split(" ")
            for i in values:
                if '"' in i :
                    if "&v" in Interpreter:
                        Interpreter = Interpreter.replace("&v",Context["Vars"].split(" ")[len(Context["Vars"].split(" "))-1])
                    return Interpreter.replace("&T*",i.replace('"',"").replace(" ","").replace("\n",""))
            return " "
        if "&T&v+" in Interpreter:
            values:list = Context["Vars"].split('"')
            values.remove(values[0])
            ListValidValues =[]
            ValueA = ""
            for i in values:
                if len(str(i).strip(' ')) > 0:
                   ListValidValues.append(i)
                   ValueA += i+"+"
                   
            return str(ListValidValues[0])+"="+ValueA[:-1]

        

    def GetEngine(self,Value,Engine="Engine.txt"):
        DataCommand = ""
        Search = False
        f = open(Engine,"r")
        for i in f.readlines():
            if Search == True and "&END" not in i:
                DataCommand += i
            
            if   i.replace("\n","").split(",") == Value and "&END" not in i:
                Search = True

            if "&END" in i and Search == True:
                return DataCommand
            
