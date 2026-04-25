from fastapi import FastAPI
from ml_pipeline import load_data, process_data, get_summary

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Risk API Running"}

@app.get("/data")
def get_data():
    df = load_data()
    df = process_data(df)

    return df.fillna("").astype(str).to_dict(orient="records")

@app.get("/summary")
def summary():
    df = load_data()
    df = process_data(df)

    return get_summary(df)