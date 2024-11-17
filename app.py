import streamlit as st
import pandas as pd
import openai
import builtins
import io

# Function to load data
def load_data(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        data = pd.read_excel(uploaded_file)
    else:
        st.error("File format not supported.")
        return None
    return data

# Set up OpenAI API
openai.api_key = 'openai-api-key'

# Function to generate code using OpenAI
def generate_code(data_head, question):
    prompt = f"""
    I have the following data:
    {data_head}

    User question:
    {question}

    Generate a Python script to perform this analysis. Ensure the code is properly formatted, sanitized, and free of unsafe operations such as file I/O, subprocesses, or access to sys/os modules.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Function to execute code securely
def execute_code(code, context):
    safe_builtins = {k: getattr(builtins, k) for k in dir(builtins) if not k.startswith('__')}
    exec_context = {
        **safe_builtins,
        **context
    }
    stdout = io.StringIO()
    exec(code, exec_context)
    return stdout.getvalue()

st.title("Streamlit + LLM Data Analysis")

st.header("Upload your structured data")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load and display the data
    data = load_data(uploaded_file)
    if data is not None:
        st.write("Data preview:")
        st.dataframe(data)

        # User input for question
        question = st.text_input("Ask a question about your data", "")

        if question:
            with st.spinner('Generating code and analyzing data...'):
                data_head = data.head().to_string()
                generated_code = generate_code(data_head, question)

                st.code(generated_code, language='python')

                context = {'data': data}
                try:
                    result = execute_code(generated_code, context)
                    st.write("Result:")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred during code execution: {e}")