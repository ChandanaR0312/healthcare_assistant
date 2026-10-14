from fastapi import FastAPI

app = FastAPI(
    title="Healthcare Multi-Agent Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}