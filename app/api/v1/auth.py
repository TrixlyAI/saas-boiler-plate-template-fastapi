from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login():
    # Placeholder for login logic
    return {"access_token": "fake-token", "token_type": "bearer"}

@router.post("/register")
def register():
    # Placeholder for registration logic
    return {"msg": "User registered"} 