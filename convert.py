from langchain_openai import OpenAI
from langchain_core.prompts.prompt import PromptTemplate

# Initialize the LLM
llm = OpenAI(temperature=0.2)

# Define the conversion prompt for the function
function_conversion_prompt = PromptTemplate(
    input_variables=["plsql_code"],
    template="""
You are an expert in both PL/SQL and Python. Convert the following PL/SQL function into Python code:

PL/SQL Code:
{plsql_code}

Python Code:
"""
)

# Define the conversion prompt for the test case
test_conversion_prompt = PromptTemplate(
    input_variables=["plsql_test_case"],
    template="""
You are an expert in both PL/SQL and Python. Convert the following PL/SQL test case into a Python test case using the unittest framework.

Make sure to include the import statement for the calc_factorial function at the top of the test case file. It will be located in factorial.py file and the function name is calc_factorial.

PL/SQL Test Case:
{plsql_test_case}

Python Test Case:
"""
)

def convert_plsql_to_python(plsql_code, plsql_test_case):
    # Manually combine prompt and LLM
    function_prompt_text = function_conversion_prompt.format(plsql_code=plsql_code)
    python_code = llm(function_prompt_text)
    
    test_prompt_text = test_conversion_prompt.format(plsql_test_case=plsql_test_case)
    python_test_case = llm(test_prompt_text)
    
    return python_code, python_test_case
