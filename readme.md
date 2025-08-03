# Instructions

1. `python -m venv .venv`
2. `source .venv/bin/activate.sh` for linux, WSL or `./.venv/scripts/activate` on windows
3. put `GOOGLE_API_KEY=#######...` in `.env` such as the structure below. find your key from here: https://aistudio.google.com/apikey
4. `pip install -r requirements.txt`
5. `python app.py`

```
ai-market-analysis
├── app.py
├── .env
├── readme.md
├── requirements.txt
├── test
│   └── ssb.jpg
└── vision_agent.py
```
useful things for me so i can look up later:
https://python.langchain.com/docs/how_to/multimodal_inputs/
