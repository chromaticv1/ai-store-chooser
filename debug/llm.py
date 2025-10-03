from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

def get_agent(df):
    return create_pandas_dataframe_agent(
        init_chat_model("gemini-2.5-flash-lite", model_provider = "google_genai"),
        df,
        verbose=False,
        allow_dangerous_code = True
    )

if __name__=='__main__':
    df = pd.read_csv(
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
    )
    a = get_agent(df)
    while(True):
        response = a.invoke([input('\n>')])
        print("o"+response['output'])