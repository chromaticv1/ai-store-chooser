import gradio as gr
from vision_agent import img_extr_2

def read_from_image(img_path_list):
    outputs = (img_extr_2(img_path_list))
    return ''.join(outputs)

with gr.Blocks() as demo:
    gr.Markdown("extract region, vp and price")
    with gr.Row():
        inp = gr.Files()
        out = gr.Markdown()
    btn = gr.Button("Run")
    btn.click(fn=read_from_image, inputs=inp, outputs=out)

demo.launch()
