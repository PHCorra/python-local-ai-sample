from src.config.llm_cofig import AIConfig, TextRequest
from fastapi import FastAPI, HTTPException # type: ignore
from dotenv import load_dotenv
import os
import ollama # type: ignore



load_dotenv()

app = FastAPI()
model = os.getenv("LLM_MODEL")

if model is None:
	raise ValueError("LLM_MODEL NOT DEFINED IN .ENV")

llm = AIConfig(model, 0)


@app.post("/")
def read_root(request: TextRequest):
	if not request.text:
		raise HTTPException(status_code=400, detail="missing request")
	try:
		response = llm.chat(request.text)
		return response
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e)) 