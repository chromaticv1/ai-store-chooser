import gradio as gr
import pandas as pd
import time
import random
import seaborn as sns
import matplotlib.pyplot as plt
from data_extractor import img_extr_2
from agent import get_agent

df = 'awoo'
agent = 'awooga'

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
#     )
# agent = get_agent(df)

def take_images(files):
    df = img_extr_2(files)
    global agent
    agent = get_agent(df)
    return df

def talk_with_agent(message, history):
    fig = plt.gcf()
    plt.clf()
    response = agent.invoke([message])
    fig = plt.gcf()
    if fig.get_axes():
        return response['output'], fig
    else: return response['output'], gr.skip()

imgbox = gr.Interface(
    fn=take_images,
    inputs=["files"],
    outputs=["dataframe"],
)

with gr.Blocks() as analysisbox:
    with gr.Row():
        plotbox = gr.Plot(render=False)
        chatbox = gr.ChatInterface(
            fn=talk_with_agent,
            examples=['hello', 'hola', 'merhaba'],
            #title= 'yes bot',
            type='messages',
            additional_outputs=[plotbox]
            )
        plotbox.render()
        #img = gr.Image()
            


demo = gr.TabbedInterface(
    [imgbox, analysisbox], tab_names= ['upload', 'analysis']
)

demo.launch()
