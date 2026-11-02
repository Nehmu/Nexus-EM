from fastapi import FastAPI

app = FastAPI(title="Nexus EM")


@app.get("/health")
def health():
    return {"status": "ok"}
