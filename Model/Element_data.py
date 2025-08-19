import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
from sklearn.pipeline import make_pipeline

def RenderData_Element():
    Sentences = [
        "crie uma variavel x",
        "criar variavel ",
        "varivel criar uma",
        "criar um menu",
        "crie menu",
        "elemento quadrado"
    ]

    Intenttion = [
        "variavel",
        "variavel",
        "variavel",
        "menu",
        "menu",
        "elemento"
    ]

    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(Sentences, Intenttion)

    joblib.dump(model, "Element_model.pkl")
    print("✅ Modelo salvo com sucesso!")