import streamlit as st
import requests
st.set_page_config(page_title="Offline Q&A Chatbot", layout="centered")

st.title("📄ASK QUESTIONS")
st.markdown("Upload a `.csv` or `.txt` file and ask a **question relevant to the file** (e.g., device status, log error).")

uploaded_file = st.file_uploader("Choose a CSV or TXT file", type=["csv", "txt"])
question = st.text_input("Ask your question here:")

if st.button("Get Answer"):
    if not uploaded_file or not question:
        st.warning("Please upload a file and enter a question.")
    else:
        with st.spinner("Processing..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            data = {"question": question}
            try:
                response = requests.post("http://localhost:5000/ask", files=files, data=data)
                if response.status_code == 200:
                    st.success("Answer:")
                    st.write(response.json()["answer"])
                else:
                    st.error(f"Error: {response.json().get('answer', 'Something went wrong')}")
            except Exception as e:
                st.error(f"Connection error: {e}")
