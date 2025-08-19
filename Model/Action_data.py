import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
from sklearn.pipeline import make_pipeline

def RenderData_Action():
    Sentences = [
        "Quero criar um novo campo",
        "Crie um campo com a variavel",
        "criar um novo elemento",
        "crie um elemento novo",
        "Excluir campo existente",
        "remover um elemento",
        "apagar variavel",
        "consultar todos os dados",
        "buscar elemento no sistema",
        "modifique o elemento para",
        "modificar o texto para",
        "mude a variavel"
    ]

    Intenttion = [
        "criar",
        "criar",
        "criar",
        "criar",
        "deletar",
        "deletar",
        "deletar",
        "consultar",
        "consultar",
        "modificar",
        "modificar",
        "modificar"
    ]

    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(Sentences, Intenttion)

    joblib.dump(model, "Action_model.pkl")
    print("✅ Modelo salvo com sucesso!")