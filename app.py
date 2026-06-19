from fastapi import FastAPI
from pydantic import BaseModel
from main import chain
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



class ChatRequest(BaseModel):
    session_id: str
    message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # testing ke liye sab allow, baad mein specific origin daal dena
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(req: ChatRequest):

    response = chain.invoke(
        {
            "question": req.message
        },
        config={
            "configurable": {
                "session_id": req.session_id
            }
        }
    )

    return {
        "answer": response
    }