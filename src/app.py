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

# Theme & UI Configuration
# --- Kiosk Mode Setup ---
# 1. Load Demo Data by Default
# Theme & UI Configuration
# --- Kiosk Mode Setup ---
# Theme & UI Configuration
# --- Kiosk Mode Setup ---
def get_default_df():
    try:
        return pd.read_csv("src/demo_data.csv")
    except Exception as e:
        print(f"Warning: Could not load demo data: {e}")
        return pd.DataFrame({"Message": ["No demo data found"]})

def get_default_agent():
    df = get_default_df()
    return get_agent(df)

def take_images(files, agent_state):
    """
    Process uploaded files.
    - Extract data
    - Return dataframe and new agent state
    """
    if not files:
        return gr.skip(), gr.skip()
    
    # Process images
    df = img_extr_2(files)
    new_agent = get_agent(df) # Update agent to use new data
    return df, new_agent

def talk_with_agent(message, history, agent_state):
    fig = plt.gcf()
    plt.clf()
    # agent_state is the agent object
    if agent_state is None:
        return "Agent not initialized.", gr.skip()

    response = agent_state.invoke([message])
    fig = plt.gcf()
    if fig.get_axes():
        return response['output'], fig
    else: return response['output'], gr.skip()

# --- Custom Poster Theme ---
# ... (theme code omitted for brevity as it is unchanged) ...
theme = gr.themes.Soft(
    primary_hue="pink",
    secondary_hue="slate",
    neutral_hue="slate",
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui", "sans-serif"]
).set(
    body_background_fill="*neutral_900",
    block_background_fill="*neutral_800",
    block_border_color="*neutral_700",
    input_background_fill="*neutral_800",
    button_primary_background_fill="#E1306C", # Hot Pink / Magenta
    button_primary_background_fill_hover="#C13584",
    button_primary_text_color="white", 
    slider_color="#E1306C"
)

# --- UI Layout ---
with gr.Blocks(theme=theme, title="AI Store Chooser - Kiosk Demo") as demo:
    # State components
    # Using callables ensures a fresh copy is created for each user session.
    df_state = gr.State(value=get_default_df)
    agent_state = gr.State(value=get_default_agent)

    gr.Markdown(
        """
        # <span style="color: #E1306C;">We are making</span> Informal Markets <span style="color: #E1306C;">BETTER</span>
        ### 🛍️ Visual Market Analytics for Video Game Currency Resellers
        """
    )
    
    # --- TOP SECTION: UPLOAD & DATA ---
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 1. Upload or Select Data")
            file_input = gr.File(
                file_count="multiple", 
                label="Drop Images Here",
                file_types=["image"]
            )
            
            # Example Images for easy Kiosk usage
            gr.Examples(
                examples=[
                    [["example_images/arekta_coin_store.jpg"]],
                    [["example_images/infinity_gamestop.jpg"]],
                    [["example_images/murubbi_game_store.jpg"]]
                ],
                inputs=file_input,
                label="Try these Examples:"
            )
            
            upload_btn = gr.Button("🚀 Analyze Images", variant="primary")
        
        with gr.Column(scale=1):
            gr.Markdown("### Data Preview")
            df_output = gr.Dataframe(
                value=get_default_df, # Initial view (accepts callable too)
                label="Current Active Data",
                interactive=False
            )

    # Action binding
    upload_btn.click(
        fn=take_images,
        inputs=[file_input, agent_state],
        outputs=[df_output, agent_state]
    )

    gr.HTML("<hr style='border-color: #444; margin: 20px 0;'>")

    # --- BOTTOM SECTION: ANALYSIS ---
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 2. Analysis & Visualization")
            gr.Markdown("*Ask the AI about the data. The Demo Data is pre-loaded!*")
            
            plotbox = gr.Plot(label="Live Visualizations")
            
        with gr.Column(scale=1):
            chatbox = gr.ChatInterface(
                fn=talk_with_agent,
                examples=[
                    ['Show me the price distribution'], 
                    ['Compare store prices for 475 VP'], 
                    ['Which store offers the best value?']
                ],
                additional_outputs=[plotbox],
                additional_inputs=[agent_state]
                # type="messages" # Omitted for safety
            )

    gr.HTML("<hr style='border-color: #444; margin: 40px 0;'>")

    # --- INFO SECTION (POSTER CONTENT) ---
    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                ### 🎮 Our Problem
                In popular games like **Valorant**, rapid price changes force sellers to constantly update advertisements and monitor competitors manually.
                
                Pricing data is locked in **unstructured formats** (e.g. screenshots, posters, image-based text), making it hard to track.
                """
            )
            gr.Markdown(
                """
                ### 💡 Our Solution
                Our app turns "price listing" photos from the internet into clear, readable tables on your phone or computer.
                
                **Core Mechanism**:
                1. Users input raw screenshots or promotional posters.
                2. An AI model identifies and extracts key entities like **Seller Name**, **Bundle Size (VP)**, and **Price (BDT)**.
                """
            )
        
        with gr.Column():
            gr.Markdown(
                """
                ### 🚀 Motivation
                Buying international goods is restricted in Bangladesh due to limited access to payment gateways. Resellers face a hard time making decisions based on:
                * Supplier availability
                * Market demand driven by events
                * Competition from other resellers
                """
            )
            gr.Markdown(
                """
                ### 🌟 Direct Outcomes & Impact
                * **Efficiency**: Automates what was once a manual, error-prone process.
                * **Equity**: Empowers both consumers and small business owners with data-driven insights.
                * **Visual Market Analytics**: providing a competitive edge in the informal market.
                """
            )

demo.launch()
