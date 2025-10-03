import gradio as gr
from pathlib import Path
import random

imgs = [x for x in Path('example_images').iterdir()]
def show_random_img():
    print('working')
    return random.choice(imgs)

with gr.Blocks() as t1:
    output = gr.Image()
    change_btn = gr.Button("change")
    change_btn.click(
        fn=show_random_img, outputs = output
    )
def yes(message, history):
    return "yes"

with gr.Blocks() as t2:
    ci = gr.ChatInterface(fn = yes, type='messages')
    output = gr.Textbox()
    change_btn = gr.Button("change")
    ci.chatbot.change(
        fn=show_random_img, outputs=output
    )
    change_btn.click(
        fn=show_random_img, outputs = output
    )

demo = gr.TabbedInterface(
    [t1,t2]
)
demo.launch()