import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

with gr.Blocks(title="高校助学备考系统", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏫 高校大学生课程助学备考多Agent系统")
    gr.Markdown("专为大学生打造的一站式学习备考系统")
    
    with gr.Tab("1. 课程初始化"):
        course_name = gr.Textbox(label="课程名称", placeholder="例如：高等数学")
        init_btn = gr.Button("初始化课程", variant="primary")
        init_status = gr.Textbox(label="状态", interactive=False)
        
        def init_course(name):
            if not name:
                return "请输入课程名称！"
            return f"✅ 课程《{name}》初始化成功！"
        
        init_btn.click(init_course, inputs=[course_name], outputs=[init_status])
    
    with gr.Tab("2. 更多功能"):
        gr.Markdown("### 完整功能请查看项目代码")
        gr.Markdown("包括：知识图谱生成、学情诊断、学习计划、习题生成、论文辅助")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
