import streamlit as st
import re

def is_valid_password(password):
    # Check minimum length
    if len(password) < 8:
        return "❌ Password must be at least 8 characters long, 1 upper case, 1 lower case, 1 number and a special character"

    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return "❌ Password must be at least 8 characters long, 1 upper case, 1 lower case, 1 number and a special character"

    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return "❌ Password must be at least 8 characters long, 1 upper case, 1 lower case, 1 number and a special character"

    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\\/]", password):
        return "❌ Password must be at least 8 characters long, 1 upper case, 1 lower case, 1 number and a special character"

    # Check for digit
    if not re.search(r"[0-9]", password):
        return "❌ Password must be at least 8 characters long, 1 upper case, 1 lower case , 1 number and a special character."

    return "✅ Password is valid."

# Streamlit UI
st.title("🔐 Create Your Account")

username = st.text_input("Enter your username")
password = st.text_input("Create a password", type="password")

if st.button("Sign Up"):
    if not username:
        st.warning("Please enter a username.")
    else:
        result = is_valid_password(password)
        if "✅" in result:
            st.success("Account created successfully!")
        else:
            st.error(result)
