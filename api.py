import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv(r"C:\Users\Texugo\Documents\sistema-bancario-python\data.csv")


# ✅ Substitui NaN por string vazia
df = df.fillna("")

@app.get("/")
def root():
    return {"message": "API funcionando!", "rotas": ["/users", "/users/{id}"]}

@app.get("/users")
def get_all_users():
    return df.to_dict(orient="records")

@app.get("/users/{id}")
def get_user_by_id(id: int):
    user = df[df["id"] == id]
    if user.empty:
        return {"error": "Usuário não encontrado"}
    return user.to_dict(orient="records")[0]


@app.put("/users/{id}")
def update_user(id: int, updated: dict):
    global df
    mask = df["id"] == id
    if df[mask].empty:
        return {"error": "Usuário não encontrado"}
    for key, value in updated.items():
        if key in df.columns:
            df.loc[mask, key] = str(value)
    return {"success": True, "user_id": id}