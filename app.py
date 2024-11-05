# app.py

import streamlit as st
import Model_Summary as mld
import Model_QA as mldq

# Set the main page layout
st.set_page_config(page_title="QA and Summarization App", layout="centered")

# Define the main interface function
def main():
    st.title("Welcome to the QA and Summarization App")
    st.write("Please select an option to proceed:")
    
    # User selection to choose between QA or Summarization
    option = st.selectbox("Choose your action", ("Select an option", "Question Answering", "Summarization"))

    if option == "Question Answering":
        qa_interface()
    elif option == "Summarization":
        summarization_interface()

# Define the QA Interface
def qa_interface():
    st.header("Question Answering Interface")
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if question:
            # Generate the answer using the mldq function from Model_QA.py
            answer = mldq.generate_answer(question)
            st.write("**Answer:**", answer)
        else:
            st.warning("Please enter a question.")

# Define the Summarization Interface
def summarization_interface():
    st.header("Summarization Interface")
    text = st.text_area("Enter text to summarize:")

    if st.button("Summarize"):
        if text:
            # Generate the summary using the mld function from Model_Summary.py
            summary = mld.summarize(text)
            st.write("**Summary:**", summary)
        else:
            st.warning("Please enter some text to summarize.")

# Run the main function
if __name__ == "__main__":
    main()
