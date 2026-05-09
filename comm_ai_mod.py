import requests,os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY not set")

#url = 'https://openrouter.ai/api/v1/responses'
url = 'https://openrouter.ai/api/v1/chat/completions'

system= (
        "You are a helpful and intelligent AI assistant. "
        "Your tone is professional yet friendly. "
        "Always use markdown for formatting when appropriate: "
        "use bold for emphasis, lists for multiple points, and code blocks with language identifiers for any code snippets. "
        "Keep responses concise and well-structured. "
        "If you are the second AI model in this chain, fact check the output of the first AI model's output provided along side the user input and if the output of the privious modle is fatually correct, then return the output of the privious model as it is."
    )

class CommAIModel:
    def __init__(self,userInput,userChatHistory):
        self.usrIn = userInput
        self.hist = userChatHistory

    def talk(self):
        payload = {
            "model":"nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            "messages":[
                {"role": "system", "content": system}
            ] + self.hist + [
                {"role":"user", "content": self.usrIn}
            ],
            "max_tokens": 1000,
            "reasoning": {
                "effort": "none"
            },
        }
        response = requests.post(
            url,
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            },
            json=payload
        )

        result = response.json()
        reply = ""

        for item in result.get('output', []):
            if item.get('type') == 'message':
                for content in item.get('content', []):
                    if content.get('type') == 'output_text':
                        reply = content.get('text', '')

        if reply:
            return f"Model:\n{reply}"
        else:
            return f"error:\n{result}"


class CommAIModelCostumizebel:
    def __init__(self,userInput,userChatHistory,userFavModel):
        self.usrIn = userInput
        self.usrFvMod = userFavModel
        self.hist = userChatHistory

    def talk(self):
        payload = {
            "model":self.usrFvMod,
            "messages":[
                {"role": "system", "content": system}
            ] + self.hist + [
                {"role":"user", "content": self.usrIn}
            ],
            "max_tokens": 1000,
            "reasoning": {
                "effort": "none"
            },
        }


        response = requests.post(
            url,
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            },
            json=payload
        )

        result = response.json()

        reply = ""
        if "choices" in result:
            reply = result["choices"][0].get("message", {}).get("content", "")
        elif "output" in result:
            for item in result.get("output", []):
                if item.get("type") == "message":
                    for content in item.get("content", []):
                        if content.get("type") == "output_text":
                            reply = content.get("text", "")

        if reply:
            return reply
        else:
            return f"error:\n{result}"