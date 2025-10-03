import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from agent import get_agent
import tempfile
import io
import contextlib
import scipy.stats
import seaborn as sns

st.title("langchain 🤝 gemini")

uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    agent = get_agent(df)

    question = st.text_area("Ask a question about your data")

    if st.button("Run") and question:
        with st.spinner("Thinking..."):

            # Capture stdout in case LLM prints something
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                try:
                    response = agent.run(question)
                    output = f.getvalue()
                except Exception as e:
                    st.error(f"Error: {e}")
                    output = None
                    response = None

            # Plot rendering if any
            fig = plt.gcf()
            if fig.get_axes():
                st.pyplot(fig)
                plt.clf()  # Clear after rendering

            # Response or stdout
            if output:
                st.code(output)
            if response:
                st.success(response)
