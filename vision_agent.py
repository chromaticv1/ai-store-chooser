from typing import Iterable
from dotenv import load_dotenv
import base64
from langchain.chat_models import init_chat_model

load_dotenv()

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

model_name = "gemini-2.5-flash-lite"
model_provider = "google_genai"
llm = init_chat_model(model = model_name, model_provider =model_provider)
prompt = "country: (country where the vp bought in bdt is valid, ie global, philipines, etc) \nlisting:\n  300 VP:\n    499 BDT\n  400 VP:\n    699 BDT"
def img_extractor(img_path:str, alt_prompt='')->str:
    message = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "give me the information in yaml like the example:\n" + (alt_prompt if len(alt_prompt)>0 else prompt),
            },
            {
                "type": "image",
                "source_type": "base64",
                "data": image_to_base64(img_path),
                "mime_type": "image/jpeg",
            },
        ],
    }

    response = (llm.invoke([message]))
    return response.text()

def img_extr_2(l:Iterable, alt_prompt:str='')->list:
    outputs = []
    for img_path in l:
        outputs.append(img_extractor(img_path, alt_prompt))
    
    return outputs
# test, python vision_agent.py
if __name__ == "__main__":
    print(
        img_extractor('./test/ssb.jpg')
    )
