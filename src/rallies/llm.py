import os
import json
import google.generativeai as genai
from rallies.config import get_llm_provider
from openai import OpenAI
from functools import wraps

def retry_json_decode(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(self, messages, model="gpt-4.1", requires_json=False):
            if not requires_json:
                return func(self, messages, model, requires_json)
            
            for attempt in range(max_retries):
                try:
                    return func(self, messages, model, requires_json)
                except json.JSONDecodeError:
                    if attempt == max_retries - 1:
                        return []
                    continue
            
        return wrapper
    return decorator

class LLM:
    def __init__(self):
        self.llm_provider = get_llm_provider()
        if self.llm_provider == "gemini":
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.client = genai.GenerativeModel('gemini-2.5-pro')
        else:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    @retry_json_decode()
    def prompt(self, messages, model = "gpt-4.1", requires_json = False):
        if self.llm_provider == "gemini":
            return self.prompt_gemini(messages, requires_json)
        else:
            response = self.client.responses.create(
                model=model,
                input=messages
            )
            response = response.output_text
            if requires_json:
                response = json.loads(response)
            return response

    def prompt_gemini(self, messages, requires_json=False):
        # Assuming messages is a list of dicts, concatenate content
        prompt = "\n".join(m["content"] for m in messages)
        response = self.client.generate_content(prompt)
        if requires_json:
            return json.loads(response.text)
        return response.text

    def prompt_stream(self, messages, model = "gpt-4.1"):
        if self.llm_provider == "gemini":
            # Assuming messages is a list of dicts, concatenate content
            prompt = "\n".join(m["content"] for m in messages)
            response = self.client.generate_content(prompt, stream=True)
            for chunk in response:
                yield chunk.text
        else:
            response = self.client.responses.create(
                model=model,
                input=messages,
                stream=True
            )
            for event in response:
                # Listen for text delta events to get streaming content
                if event.type == "response.output_text.delta":
                    yield event.delta
