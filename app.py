import streamlit as st
import streamlit.components.v1 as components
from LLM import infer
from util import write_answer
from trans import speak

max_line_length = 80

def main():
    st.set_page_config(
        page_title="Grade Guru AI Examiner",
        page_icon="./grade-guru.png",
    )

    # Inject custom CSS
    st.markdown(
        """
        <style>
        .css-18e3th9, .css-1d391kg, .css-1cpxqw2 {
            background-color: #FFA500;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .logo {
            max-width: 150px;
            margin-bottom: 20px;
        }
        .stTitle, .stMarkdown h4 {
            color: #4B0082;
            text-align: center;
        }
        div.stButton > button {
            background-color: #4B0082;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        textarea {
            background-color: #e0e0e0;
            color: #4B0082;
            border: 1px solid #4B0082;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()



# Create two columns
col1, col2 = st.columns([1, 5])

# Display the logo in the first column
with col1:
    st.image("./grade-guru.png", width=100)  # Adjust the width as needed

# Display the title in the second column
with col2:
    st.title("Grade Guru - The AI Examiner")
    st.write("Where AI meets A+!")

st.markdown("#### Step 1 : Upload Student Anwer Photo")
components.html(
    """
    <iframe
        src="https://merve-llava-next.hf.space"
        frameborder="0"
        width="100%"
        height="70%"
    ></iframe>
    """
)
st.markdown("#### Step 2 : Enter Student Answer text extracted from Step 1")
student_answer = st.text_area("Enter student answer extracted text here")

st.markdown("#### Step 3 : Enter Teacher's Answer")
teacher_answer = st.text_area("Enter teacher's answer here")

st.markdown("#### Step 4 : Total Marks of question")
total_marks = st.text_area("Enter total marks of question")


if st.button('Examine Result', key='submit_button', help='Click to submit your input.'):
    placeholder = st.empty()
    placeholder.image("testing.gif")
    Evaluation=infer(student_answer,teacher_answer,total_marks)
    placeholder.empty()

    write_answer(Evaluation,max_line_length)

    speak(Evaluation)