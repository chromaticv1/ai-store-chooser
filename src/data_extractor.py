from dotenv import load_dotenv
import os
import base64
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from typing import List, cast
import mimetypes

import pandas as pd

from pprint import pprint
load_dotenv()

if 'GOOGLE_API_KEY' not in os.environ.keys(): 
    raise Exception('PLS PUT YE THING')

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

model_name = "gemini-2.5-flash-lite"
model_provider = "google_genai"
llm = init_chat_model(model = model_name, model_provider =model_provider)


# Schema:
class PricePerVP(BaseModel):
    vp_amount: int
    price: float

class PriceList(BaseModel):
    country: str
    prices: List[PricePerVP]

class CountryPricesList(BaseModel):
    items: List[PriceList] 

structured_llm = llm.with_structured_output(CountryPricesList)

def img_extractor(img_path:str):
   # print(f"{mimetypes.guess_type(img_path)[0]= } {type(mimetypes.guess_type(img_path)[0])}")
    message= HumanMessage(
        content=[
            {'type': 'text',
             'text': 'This is a seller poster of valorant vp. Extract the full name of the countries, how much vp you get and how much you have to pay in bdt for that much vp in JSON. PHP means Philippines, MYS means Malaysia, BD means Bangladesh. If nothing is said then its Bangladesh.' 
             },
            {"type": 'image',
             'source_type': 'base64',
             'data': image_to_base64(img_path),
             'mime_type': mimetypes.guess_type(img_path)[0]
             }
        ]
    )
    response= cast( CountryPricesList, structured_llm.invoke([message]))
    response_json = response.model_dump()
    response_json['store_name'] = img_path.split('/')[-1].split('\\')[-1].split('.')[0]
    return response_json

def img_extr_2(l:list, alt_prompt:str='')->pd.DataFrame:

    def json_to_long_df(CPS: dict) :
        found_records = []
        store_name = CPS['store_name']
        for item in CPS['items']:
            country = item['country']
            for price in item['prices']:
                vp_amount = price['vp_amount']
                vp_price = price['price']
                found_records.append({
                    'store_name': store_name,
                    'country': country,
                    'vp_amount': vp_amount,
                    'vp_price': vp_price
                })
        return found_records

    outputs = []
    for img_path in l:

        img_extractor_output = (img_extractor(img_path))
        outputs.append(img_extractor_output)

    df_records = map(json_to_long_df, outputs)
    df_records_flattened = []
    for record in df_records:
        df_records_flattened = df_records_flattened + record
    df_output = (pd.DataFrame(df_records_flattened))
    df_output.to_csv('./outputs/test.csv')
    return df_output

# test, python vision_agent.py
if __name__ == "__main__":
    x = img_extr_2(['./example_images/arekta_coin_store.jpg'])
    