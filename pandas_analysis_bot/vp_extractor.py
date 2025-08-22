from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
import base64
from pathlib import Path
import os
from typing import List
from pydantic import BaseModel, Field
import instructor
import pandas as pd

os.environ["GOOGLE_API_KEY"]= "AIzaSyAW7k0L9H_xxbRMsHFzHev7Dg1iI4t7MK4"
model_name = "gemini-2.5-flash-lite-preview-06-17"
def extract_prices_from_image(image_path: str) -> str:
    # Initialize the model
    model = init_chat_model(
        model_name,
        model_provider="google_genai",
    )
    
    # Read and encode the image in base64
    image_path_obj = Path(image_path)
    with open(image_path_obj, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    
    # Prepare message for Gemini
    message = HumanMessage(content=[
        {"type": "text", "text": "write down the prices of VP listed in the image"},
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
        }
    ])
    
    # Invoke the model with the message
    response = model.invoke([message])
    
    # Return the response content
    return response.content




class pricing(BaseModel):
    VP: str = Field(..., description="amount of VP")
    Price: int = Field(..., description="price for the amount of VP")

class price_listing(BaseModel):
    price_listing: List[pricing] = Field(..., description="List of pricing mentioned in the text")

def extract_structured_prices(text: str, model_name: str ) -> price_listing:
    client = instructor.from_provider("google/"+model_name)
    response = client.messages.create(
        messages=[{
            "role": "user",
            "content": f"Extract {text}"
        }],
        response_model=price_listing,
    )
    return response

def extract_prices_from_image_to_structured_data(image_path: str) -> price_listing:
    # Step 1: Extract raw text from image
    raw_text = extract_prices_from_image(image_path)
    
    # Step 2: Parse raw text into structured format
    structured_prices = extract_structured_prices(raw_text)
    
    return structured_prices


result = (extract_prices_from_image_to_structured_data("images/infinity_gamestop.jpg")).dict()

print(result)