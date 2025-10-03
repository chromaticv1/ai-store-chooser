# Build
This project was done on windows, python 3.13.5
## Setup environment:
1. `python -m venv .venv`
2. `source .venv/bin/activate` for linux, WSL, mac or anything unix; `./.venv/scripts/activate` on windows
3. put `GOOGLE_API_KEY=#######...` in `.env` such as the structure below. [find your key here](https://aistudio.google.com/apikey)
    ```
    ai-store-chooser
    |-- .env
    |-- debug
    |-- deprecated
    .
    .
    .
    |-- requirements.txt
    |-- readme.md
    |-- .gitignore
    ```

4. `pip install -r requirements.txt` to install libraries and modules required for this.

# Run
1. `python src/app.py`
2. Drag and drop price listing images into upload section and upload. Uploading something is required for the analysis bot to work.
3. chat with the dataframe generated in the analysis secttion
