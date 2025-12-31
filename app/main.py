from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth, feedback, insights

app = FastAPI(title="Clueso Clone")

# CORS SETTINGS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow all (safe in dev)
    allow_credentials=True,
    allow_methods=["*"],          # IMPORTANT
    allow_headers=["*"],          # IMPORTANT
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(feedback.router)
app.include_router(insights.router)

@app.get("/")
def root():
    return {"status": "Backend Running"}
