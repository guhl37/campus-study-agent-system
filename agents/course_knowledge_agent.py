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

class CourseKnowledgeAgent:
    def __init__(self, course_name="default_course"):
        self.course_name = course_name
    
    def generate_knowledge_graph(self):
        return f"《{self.course_name}》知识图谱生成功能（完整版本请查看项目详情）"
