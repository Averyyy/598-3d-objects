from LLM.config.config import API_KEY
from openai import OpenAI


def get_embedding(text: str, model: str = "text-embedding-ada-002") -> list[float]:
    client = OpenAI(api_key=API_KEY)
    result = client.embeddings.create(
        model=model,
        input=text,
    )
    return result.data[0].embedding
