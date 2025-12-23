from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

def get_agent(df):
    return create_pandas_dataframe_agent(
        init_chat_model("gemma-3-4b-it", model_provider = "google_genai"),
        df,
        verbose=True,
        allow_dangerous_code = True
    )

