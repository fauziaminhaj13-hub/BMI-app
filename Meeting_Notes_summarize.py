import streamlit as st
import google.generativeai as genai

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])  

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-2.5-flash-lite")

st.title("AI Meeting Notes Summarizer")

uploaded_file = st.file_uploader("📂 Upload transcript (.txt)", type=["txt"])
transcript = st.text_area("📝 Or paste transcript here")

if st.button("⚡ Generate Summary"):
    if transcript or uploaded_file:
        if uploaded_file:
            transcript = uploaded_file.read().decode("utf-8")

        prompt = f"""Summarize this meeting into:
        - Key Decisions
        - Action Items (mark as High/Medium/Low priority)
        - Important Dates
        - Risks/Concerns
        - Follow-up Questions

        Transcript: {transcript}"""

        response = model.generate_content(prompt)
        st.session_state["summary"] = response.text

        st.subheader("📌 Meeting Summary")
        st.write(st.session_state["summary"])
if "summary" in st.session_state:
    if st.button("📄 Download as PDF"):
    
        doc = SimpleDocTemplate("Meeting_Summary.pdf")
        styles = getSampleStyleSheet()
        story =[]

# Title
        story.append(Paragraph("📝 Meeting Summary", styles["Heading1"]))
     

        # Take Gemini’s output and split into sections
        for line in st.session_state["summary"].split("\n"):
            if line.strip():
                if line.startswith(("✅","📌","📅","⚠️","❓")):
                    story.append(Paragraph(f"<b>{line}</b>", styles["Heading2"]))
                else:
                    story.append(Paragraph(line, styles["Normal"]))
        

        # Build PDF
        doc.build(story)

        st.success("✅ PDF created successfully! Check your folder.")


 

       





        
