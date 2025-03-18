from src.config.llm_cofig import TextRequest
from fastapi import FastAPI, HTTPException # type: ignore
import ollama # type: ignore

app = FastAPI()



@app.post("/")
def read_root(request: TextRequest):
	if not request.text:
		raise HTTPException(status_code=400, detail="deu ruim")

	try:
		response = ollama.chat(model="llama3.2", messages=[
		{
			"role": "system",
			"content": "You're a pretty straightfoward assistant, don't need to explain a lot your answers, your name is new."
		},
		{
			"role":"user",
			"content": request.text
		}
		], options={"temperature": 0})
		llm_res = response.get('message', {}).get('content', '')

		return {"resposta": llm_res}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e)) 