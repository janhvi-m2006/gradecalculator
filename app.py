import streamlit as st

# Page Settings
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Grade Calculator")
st.write("Enter your marks and get your grade instantly!")

# Input
marks = st.number_input(
    "Enter Marks (0-100)",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

# Button
if st.button("Calculate Grade"):

    if marks >= 90:
        grade = "A+"
        emoji = "🏆"

    elif marks >= 80:
        grade = "A"
        emoji = "🎉"

    elif marks >= 70:
        grade = "B"
        emoji = "👍"

    elif marks >= 60:
        grade = "C"
        emoji = "🙂"

    elif marks >= 50:
        grade = "D"
        emoji = "😐"

    else:
        grade = "F"
        emoji = "❌"

    st.success(f"Your Grade: {grade} {emoji}")

# Progress Bar
st.progress(int(marks))

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")