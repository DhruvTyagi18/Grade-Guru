
# import streamlit as st
# import streamlit.components.v1 as components
# from PIL import Image
# import pytesseract
# from LLM import infer  # Assuming this is a custom module you have
# from util import write_answer  # Assuming this is a custom module you have
# from trans import speak  # Assuming this is a custom module you have

# max_line_length = 80

# def extract_text_from_image(image):
#     """Extract text from the given image using OCR."""
#     pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
#     text = pytesseract.image_to_string(image)
#     return text

# def main():
#     st.set_page_config(
#         page_title="Grade Guru AI Examiner",
#         page_icon="./grade-guru.png",
#     )

#     # Inject custom CSS
#     st.markdown(
#         """
#         <style>
#         .css-18e3th9, .css-1d391kg, .css-1cpxqw2 {
#             background-color: #FFA500;
#         }
#         .logo-container {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }
#         .logo {
#             max-width: 150px;
#             margin-bottom: 20px;
#         }
#         .stTitle, .stMarkdown h4 {
#             color: #4B0082;
#             text-align: center;
#         }
#         div.stButton > button {
#             background-color: #4B0082;
#             color: white;
#             border: none;
#             padding: 10px 20px;
#             text-align: center;
#             text-decoration: none;
#             display: inline-block;
#             font-size: 16px;
#             margin: 4px 2px;
#             cursor: pointer;
#             border-radius: 8px;
#         }
#         textarea {
#             background-color: #e0e0e0;
#             color: #4B0082;
#             border: 1px solid #4B0082;
#             border-radius: 8px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()



# # Create two columns
# col1, col2 = st.columns([1, 5])

# # Display the logo in the first column
# with col1:
#     st.image("./grade-guru.png", width=100)  # Adjust the width as needed

# # Display the title in the second column
# with col2:
#     st.title("Grade Guru - The AI Examiner")
#     st.write("Where AI meets A+!")


# st.markdown("#### Step 1 : Upload Student Answer Photo")
# student_image = st.file_uploader("Upload Student Answer Photo", type=["png", "jpg", "jpeg"])

# if student_image is not None:
#     image = Image.open(student_image)
#     student_answer_text = extract_text_from_image(image)
#     st.success("Student answer text extracted successfully!")
# else:
#     student_answer_text = ""

# st.markdown("#### Step 2 : Enter Student Answer text extracted from Step 1")
# student_answer = st.text_area("Enter student answer extracted text here", value=student_answer_text)

# st.markdown("#### Step 3 : Upload Teacher's Answer Photo")
# teacher_image = st.file_uploader("Upload Teacher's Answer Photo", type=["png", "jpg", "jpeg"], key="teacher")

# if teacher_image is not None:
#     image = Image.open(teacher_image)
#     teacher_answer_text = extract_text_from_image(image)
#     st.success("Teacher's answer text extracted successfully!")
# else:
#     teacher_answer_text = ""

# st.markdown("#### Step 4 : Enter Teacher's Answer")
# teacher_answer = st.text_area("Enter teacher's answer here", value=teacher_answer_text)

# st.markdown("#### Step 5 : Total Marks of question")
# total_marks = st.text_area("Enter total marks of question")

# if st.button('Examine Result', key='submit_button', help='Click to submit your input.'):
#     placeholder = st.empty()
#     placeholder.image("testing.gif")
#     Evaluation = infer(student_answer, teacher_answer, total_marks)
#     placeholder.empty()

#     write_answer(Evaluation, max_line_length)

#     speak(Evaluation)

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
