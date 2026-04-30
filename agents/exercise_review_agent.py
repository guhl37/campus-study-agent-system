from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"),
    model_name=os.getenv("MODEL_NAME"),
    temperature=0.3,
)

class ExerciseReviewAgent:
    def __init__(self):
        pass
