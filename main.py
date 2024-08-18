from convert import convert_plsql_to_python
from save_code import save_code_to_file
from run_tests import run_python_tests

# Example PL/SQL code and test case
plsql_code = """
CREATE OR REPLACE FUNCTION calc_factorial(n IN NUMBER) RETURN NUMBER IS
    result NUMBER := 1;
BEGIN
    FOR i IN 1..n LOOP
        result := result * i;
    END LOOP;
    RETURN result;
END calc_factorial;
"""

plsql_test_case = """
DECLARE
    v_result NUMBER;
BEGIN
    v_result := calc_factorial(5);
    DBMS_OUTPUT.PUT_LINE('Factorial of 5 is ' || v_result);
    IF v_result = 120 THEN
        DBMS_OUTPUT.PUT_LINE('Test Passed');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Test Failed');
    END IF;
END;
"""

# Convert PL/SQL to Python
python_code, python_test_case = convert_plsql_to_python(plsql_code, plsql_test_case)

# Print the converted code
print("Converted Python Code:\n", python_code)
print("Converted Python Test Case:\n", python_test_case)

# Save the converted code and test case to files
save_code_to_file(python_code, python_test_case)

# Run the test case and display the results
test_results = run_python_tests()
print("Test Results:\n", test_results)
