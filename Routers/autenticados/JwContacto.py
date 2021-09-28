from typing import List
from fastapi import APIRouter,status, HTTPException,Depends
from sql_app import schemas,main,crud
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth")