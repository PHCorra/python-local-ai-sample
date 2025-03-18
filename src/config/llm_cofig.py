import ollama
from pydantic import BaseModel

class TextRequest(BaseModel):
	text: str


class AIConfig:
	def __init__(self, model: str, temperature: float, system_prompt: str = "you're an assistant named testAI, that helps in general doubts"):
		self.model = model
		self.temperature = temperature
		self.system_prompt = system_prompt

	def chat(self, user_message: str) -> dict:
		if not user_message:
			return {"error": "Empty message"}
		response = ollama.chat(model=self.model, messages=[
		{
			"role": "system",
			"content": self.system_prompt
		},
		{
			"role": "user",
			"content": user_message
		}
		], options={"temperature": self.temperature})
		if "error" in response:
			return { "error": response["error"] }
		llm_res = response.get('message', {}).get('content', '')
		
		return {"answer": llm_res }
		