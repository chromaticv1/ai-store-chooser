import gradio as gr
import vision_agent

def read_from_image(img_path):
    return vision_agent.img_extractor(img_path)

with gr.Blocks() as demo:
    gr.Markdown("extract region, vp and price")
    with gr.Row():
        inp = gr.UploadButton()
        out = gr.Markdown()
    btn = gr.Button("Run")
    btn.click(fn=read_from_image, inputs=inp, outputs=out)

demo.launch()
