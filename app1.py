import streamlit as st

st.title("🧮 Agentic Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            st.stop()
        result = num1 / num2

    st.success(f"✅ Result: {num1} {operation} {num2} = {result}")
