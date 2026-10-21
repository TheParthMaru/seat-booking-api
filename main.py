from fastapi import FastAPI

app = FastAPI()

seats = ["A1", "A2", "A3"]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/seats")
def get_seats():
    return {"seats": seats}
    