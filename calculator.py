Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calculator():
    """
...     A simple calculator program that performs basic arithmetic operations.
...     """
...     print("Welcome to the Python Calculator!")
...     print("Please select an operation:")
...     print("1. Addition (+)")
...     print("2. Subtraction (-)")
...     print("3. Multiplication (*)")
...     print("4. Division (/)")
...     print("5. Exit")
... 
...     while True:
...         choice = input("Enter your choice (1-5): ")
... 
...         if choice == '5':
...             print("Exiting the calculator...")
...             break
... 
...         num1 = float(input("Enter the first number: "))
...         num2 = float(input("Enter the second number: "))
... 
...         if choice == '1':
...             result = num1 + num2
...             print(f"The result is: {result}")
...         elif choice == '2':
...             result = num1 - num2
...             print(f"The result is: {result}")
...         elif choice == '3':
...             result = num1 * num2
...             print(f"The result is: {result}")
...         elif choice == '4':
...             if num2 == 0:
...                 print("Error: Division by zero is not allowed.")
...             else:
...                 result = num1 / num2
...                 print(f"The result is: {result}")
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
