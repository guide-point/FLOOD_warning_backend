from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, reports, sos

# bring in database metadata
from models.db import engine
from models import orm

app = FastAPI(title="Flood Warning Backend")

# enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables at startup (simple approach)
orm.Base.metadata.create_all(bind=engine)

# include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
app.include_router(sos.router, prefix="/sos", tags=["sos"])

@app.get("/")
def read_root():
    return {"message": "Flood warning backend is running"}
