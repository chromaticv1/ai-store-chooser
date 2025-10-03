# Build
This project was done on windows, python 3.13.5
## Setup environment:
1. clone the project:
    ```sh
    git clone https://github.com/chromaticv1/ai-store-chooser --depth=1
    cd ai-store-chooser
    ```
2. setup python environment
    ```sh
    python -m venv .venv
    ```
3. Activate the environment:
    ```sh
    source .venv/bin/activate
    ```
    for Linux, WSL, Mac or anything unix;
    ```ps1
    ./.venv/scripts/activate
    ```
    on Windows.
4. put `GOOGLE_API_KEY=#######...` in `.env` such as the structure below. [find your key here](https://aistudio.google.com/apikey)
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

5. Install the required libraries and modules.
    ```
    pip install -r requirements.txt
    ```

# Run
1. `python src/app.py`
2. Drag and drop price listing images into upload section and upload. Uploading something is required for the analysis bot to work.
3. chat with the dataframe generated in the analysis section.
