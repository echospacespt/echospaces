from fastapi import FastAPI

from app.core.supabase import supabase

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    try:
        result = (
            supabase
            .table("users")
            .select("*")
            .limit(1)
            .execute()
        )

        return {
            "status": "ok",
            "database": "connected"
        }

    except Exception as ex:
        return {
            "status": "error",
            "message": str(ex)
        }