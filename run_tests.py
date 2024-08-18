import subprocess

def run_python_tests():
    # Run the Python test case
    result = subprocess.run(['python', 'test_factorial.py'], capture_output=True, text=True)
    
    # Print the captured stdout
    print("Test Output:\n", result.stdout)
    
    # Check for test success
    if "OK" in result.stdout:
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please review the output above.")

    # If there are any errors, print them
    if result.stderr:
        print("Errors:\n", result.stderr)
    
    return result.stdout
