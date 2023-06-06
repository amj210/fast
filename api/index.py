from fastapi import FastAPI, HTTPException, Request
from os import getenv
import uvicorn
app = FastAPI()

@app.post("/comments")
def create_comment(request: Request):
    comment = request.json().get("comment")
    if not comment:
        raise HTTPException(status_code=400, detail="Comment field is required")
    print(comment)
    return {"message": "OK"}

if __name__=="__main__":
    port=int(getenv("PORT",8000))
    uvicorn.run("api.index:app",host="0.0.0.0",port=port,reload=True)