# Instructions
## Setup python environment:
1. `python -m venv .venv`
2. `source .venv/bin/activate.sh` for linux, WSL or `./.venv/scripts/activate` on windows
3. put `GOOGLE_API_KEY=#######...` in `.env` such as the structure below. find your key from here: https://aistudio.google.com/apikey
4. `pip install -r requirements.txt`

## VP Extractor: (Computer Vision)
VP or "Valorant Points" is a currency in the game Valorant by Riot Games. Our goal is to extract the pricing of the posters provided by various stores.
1. `python vp_extractor/app.py`
2. drag and drop images from tests
3. Outputs are stored in `outputs/test.csv`

## Pandas Analysis bot: (NLP/?)
1. `streamlit run pandas_analysis_bot/app.py`
2. input any `.csv` file, ask any questions! if you see any PARSE errors, rerun, it's the LLM being silly.
```
ai-store-chooser
|-- .env
|-- outputs
|   `-- test.csv
|-- pandas_analysis_bot
|   |-- agent.py
|   |-- app.py
|   `-- vp_extractor.py
|-- readme.md
|-- requirements.txt
|-- test
|   |-- arekta_coin_store.jpg
|   |-- infinity_gamestop.jpg
|   |-- murubbi_game_store.jpg
|   |-- steam_store_bd.jpg
|   `-- vai_amra_trusted.jpg
`-- vp_extractor
    |-- app.py
    `-- vision_agent.py
```
useful things for me so i can look up later:
https://python.langchain.com/docs/how_to/multimodal_inputs/
