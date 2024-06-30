from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()

pipe = pipeline(model="j-hartmann/emotion-english-distilroberta-base")

# # We define that we expect our input to be a string
class RequestModel(BaseModel):
    input: str

# # ->  In APIs, requests are made to ask the API to perform a certain task — in this case to analyze a piece of text. 
@app.post("/sentiment")
def get_response(request: RequestModel):
    prompt = request.input

#     # We use the hf model to classify the prompt
    response = pipe(prompt)

#     # We get both the label and the score from the input
    label = response[0]["label"]
    score = response[0]["score"]
    return {"prompt": prompt, "label": label, "score": score}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)