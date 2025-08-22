import gradio as gr
from vision_agent import img_extr_2
import seaborn as sns

def sns_plt(df):
    sns.set_theme(style='white')
    return sns.relplot(x = 'vp_price', y='vp_amount', hue ='country', data=df)

def read_from_image(img_path_list):
    df = (img_extr_2(img_path_list))
    return (df)
    

with gr.Blocks() as demo:
    gr.Markdown("# extract region, vp, price")
    
    inp = gr.Files()
    btn = gr.Button("Run")
    # out_plot = gr.Plot()
    out_plot = gr.LinePlot(x='vp_amount', y='vp_price', color='country')
    btn.click(fn=read_from_image, inputs=inp, outputs= out_plot)

demo.launch()
