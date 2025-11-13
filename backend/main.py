from fastapi import FastAPI 

app = FastAPI(title="Online Exam Management API.")

@app.get('/')
async def index():
    return {"message": "Welcome."}