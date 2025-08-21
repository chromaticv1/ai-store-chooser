from dotenv import load_dotenv
import base64
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from typing import List, cast

from pprint import pprint
load_dotenv()

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
    message= HumanMessage(
        content=[
            {'type': 'text',
             'text': 'This is a seller poster of valorant vp. Extract the full name of the countries, how much vp you get and how much you have to pay in bdt for that much vp in JSON. PHP means Philippines, MYS means Malaysia, BD means Bangladesh. If nothing is said then its Bangladesh.' 
             },
            {"type": 'image',
             'source_type': 'base64',
             'data': image_to_base64(img_path),
             'mime_type': 'image/jpeg'
             }
        ]
    )
    response= cast( CountryPricesList, structured_llm.invoke([message]))
    return response.model_dump()['items']

def img_extr_2(l:list, alt_prompt:str='')->list:
    outputs = []
    for img_path in l:
        outputs.append(img_extractor(img_path))
    
    return outputs
# test, python vision_agent.py
if __name__ == "__main__":
    # pprint('Simple---')
    #pprint(img_extractor('./test/ssb.jpg'))
    #pprint('3 Countires---')
    #pprint(img_extractor('./test/three_countries.jpg'))
    x = img_extr_2(['./test/ssb.jpg','./test/three_countries.jpg'])
    pprint(x)
