# TASK:7 Streamlit + OpenAI Data Analysis

## Overview

This project integrates Streamlit with OpenAI's language model to perform data analysis based on user questions. The app allows users to upload structured data files (CSV or Excel), input natural language questions about the data, and receive Python code that performs the desired analysis. This code is then executed in a secure environment, and the results are displayed within the Streamlit app.

## Features

* **File Upload:** Supports CSV and Excel file uploads.
* **Data Preview:** Displays a preview of the uploaded data.
* **Natural Language Query:** Accepts user queries in plain English.
* **Code Generation:** Generates Python code using OpenAI based on the user's query.
* **Secure Code Execution:** Executes the generated code in a controlled environment to ensure safety.
* **Result Display:** Shows the output of the executed code.

## Prerequisites

* Python 3.7 or higher
* OpenAI API key
* Required Python packages (streamlit, pandas, openai)

## Installation



1. **Clone the repository:**

   ```sh
   git clone https://github.com/codeBunny2022/7_CHIRAG_CHAUHAN.git
   cd 7_CHIRAG_CHAUHAN
   ```



2\. Create a virtual environment:


```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```



3\. Install the dependencies:

```bash
pip install -r requirements.txt
```



4\. Add your OpenAI API key:

Replace 'openai-api-key' with your actual OpenAI API key in the [app.py](http://app.py) file:

```bash
openai.api_key = 'openai-api-key'
```


Running the Application



1. Start the Streamlit app:


```bash
streamlit run app.py
```



2. Upload Data:
   * Click on "Choose a file" to upload a CSV or Excel file.
   * Supported formats: .csv, .xlsx
3. Preview Data:
   * After uploading, the app will display a preview of the data.
4. Ask a Question:
   * Enter your question in the text input box.
   * For example: "Calculate the average value of a column named 'age'."
5. Generate and Execute Code:
   * The app will generate corresponding Python code using OpenAI and display it.
   * The generated code will then be executed, and the result will be shown below the code.


Security Considerations

* The execution of generated Python code is handled in a restricted environment to avoid unsafe operations such as file I/O, subprocesses, or access to system modules.
* This project uses basic security practices to minimize risks, but it's recommended to review and validate generated code before execution, especially in a production environment.



# CustomLangChainAgent: Secure Code Generation and Execution

## Overview

`custom_agent.py` is a Python script that leverages OpenAI's GPT-3 to generate and execute Python code based on user input securely. The script is designed to generate Python code that performs specific data analysis tasks and execute this code within a controlled environment to ensure security.

## Features

* **Code Generation:** Uses OpenAI's API to generate Python code based on a natural language prompt.
* **Secure Execution:** Executes the generated code in a restricted environment to avoid unsafe operations.
* **Error Handling:** Captures and displays any errors that occur during code execution.
* **Context Awareness:** Allows passing of data context such as DataFrames for analysis.

## Prerequisites

* Python 3.7 or higher
* OpenAI API key
* Required Python packages (pandas, openai)

## Installation


1. **Clone the repository:**

   ```sh
   
   git clone https://github.com/codeBunny2022/7_CHIRAG_CHAUHAN.git
   cd 7_CHIRAG_CHAUHAN
   ```



2. Execute the script:

   Run the script to see the generated code and its execution result:

```bash
python custom_agent.py
```



3. View Output:

   The script will output the generated code and its execution result. For example:

```bash
Generated Code:
data['sales'].sum()

Execution Result:
1150
```


