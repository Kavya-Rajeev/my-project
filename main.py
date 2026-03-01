"""
Simple Python Program
Author: Kavya Rajeev
Description: Demonstrates basic GitHub workflow
"""

def greet(name):
    """
    Returns a greeting message.
    """
    return f"Hello, {name}! Welcome to GitHub."

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()