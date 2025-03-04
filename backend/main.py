from fastapi import FastAPI
from backend.domains.support.authentication.routers import router as auth_router

app = FastAPI(title="Tuner Platform API",
            description="API for Tuner Testing Platform",
            version="0.1.0")

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Tuner Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)