def save_code_to_file(python_code, python_test_case):
    # Save the converted Python code to factorial.py
    with open('factorial.py', 'w') as f:
        f.write(python_code)

    # Save the converted Python test case to test_factorial.py
    with open('test_factorial.py', 'w') as f:
        f.write(python_test_case)
