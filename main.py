from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.post("/comments")
def create_comment(request: Request):
    comment = request.json().get("comment")
    if not comment:
        raise HTTPException(status_code=400, detail="Comment field is required")
    print(comment)
    return {"message": "OK"}