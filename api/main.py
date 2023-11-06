from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return "Wf the application"


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):