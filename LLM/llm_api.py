# LLM/llm_api.py

import base64
import requests
from LLM.config.config import API_KEY
from LLM.prompt.initial_prompt import generate_initial_prompt
from LLM.prompt.step_prompt import generate_step_prompt


class LLMAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def send_request(self, prompt, images=None, max_tokens=300):
        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "max_tokens": max_tokens
        }

        if images:
            for image_path in images:
                base64_image = self.encode_image(image_path)
                payload["messages"][0]["content"].append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                )

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=payload)
        print(response.json())
        print(response.json()['choices'][0]['message']['content'])
        return response.json()['choices'][0]['message']['content']

    def generate_initial_prompt(self, images):
        return generate_initial_prompt(images)

    def generate_step_prompt(self, action, images):
        return generate_step_prompt(action, images)
