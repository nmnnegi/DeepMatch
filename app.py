import streamlit as st
from datetime import datetime
from modules.pdf_utils import extract_pdf_image_and_text
from modules.gemini_api import get_gemini_response
from modules.prompts import resume_analysis_prompt, skill_recommendation_prompt, ats_match_prompt
from modules.ui_utils import download_text_file, draw_pie_chart, extract_match_percentage
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="DeepMatch: AI Resume Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar navigation menu ---
with st.sidebar:
    selected_page = option_menu(
        menu_title="Navigation",
        options=[
            "🏠 Home",
            "📝 Resume Analysis",
            "📈 ATS Match & Score",
            "📚 Skill Recommendations",
            "📂 Resume Preview",
            "🕒 Session History",
            "❓ Help / FAQ"
        ],
        icons=[
            "house", "file-earmark-person", "diagram-3", "lightbulb",
            "file-earmark", "clock-history", "question-circle"
        ],
        menu_icon="cast",
        default_index=0,
    )

if 'history' not in st.session_state:
    st.session_state['history'] = []

def upload_section():
    col_a, col_b = st.columns([2,3])
    with col_a:
        input_text = st.text_area("Paste the Job Description Here", key="input", height=180)
    with col_b:
        uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
    return input_text, uploaded_file

# --- Main page logic ---
if selected_page == "🏠 Home":
    st.title("DeepMatch: AI Resume Analysis Suite")
    st.header("Empowering Your Career Journey with Intelligent, Personalized Insights")
    st.subheader("What can DeepMatch do?")
    st.markdown("""
- **Advanced Resume Evaluation**: Comprehensive AI-powered assessment tailored to any job description.
- **Precise ATS Compatibility Scoring**: Know exactly how applicant tracking systems will rate your resume.
- **Personalized Skill Recommendations**: Targeted learning paths to close skill gaps and elevate your profile.
- **Secure and Private**: Your data stays confidential and processed only during your session.
- **Session History**: Download all previous analyses for your records.
    """)
    st.subheader("How It Works")
    st.markdown("""
1. Upload your PDF resume and paste a job description.
2. DeepMatch highlights strengths and identifies skill gaps.
3. Get ATS matching, improvement paths, and personalized reports.
4. Download every analysis for future job searches.
    """)
    st.info("Use the sidebar to navigate between analysis tools.")

elif selected_page == "📝 Resume Analysis":
    st.header("Deep Resume Review")
    input_text, uploaded_file = upload_section()
    if st.button("Run Analysis"):
        if uploaded_file:
            pdf_image, pdf_base64, resume_txt = extract_pdf_image_and_text(uploaded_file)
            response = get_gemini_response(
                input_text,
                [{"mime_type": "image/jpeg", "data": pdf_base64}],
                resume_analysis_prompt
            )
            st.subheader("HR Feedback")
            st.write(response)
            download_text_file(response, "Download this Analysis")
            st.session_state['history'].append({
                "type": "Resume Analysis",
                "at": str(datetime.now()),
                "out": response
            })
        else:
            st.warning("Please upload your resume.")

elif selected_page == "📈 ATS Match & Score":
    st.header("ATS Match Score and Keywords")
    input_text, uploaded_file = upload_section()
    if st.button("Run ATS Analysis"):
        if uploaded_file:
            pdf_image, pdf_base64, resume_txt = extract_pdf_image_and_text(uploaded_file)
            response = get_gemini_response(
                input_text,
                [{"mime_type": "image/jpeg", "data": pdf_base64}],
                ats_match_prompt
            )
            match_pct = extract_match_percentage(response)
            col1, col2 = st.columns([3,2])
            with col1:
                st.image(pdf_image, caption="Resume First Page", use_container_width=True)
            with col2:
                st.subheader("ATS Match Rate")
                st.pyplot(draw_pie_chart(match_pct))
            st.subheader("ATS Report")
            st.write(response)
            download_text_file(response, "Download ATS Report")
            st.session_state['history'].append({
                "type": "ATS Match",
                "at": str(datetime.now()),
                "out": response
            })
        else:
            st.warning("Please upload your resume.")

elif selected_page == "📚 Skill Recommendations":
    st.header("Skill and Career Growth Actions")
    input_text, uploaded_file = upload_section()
    if st.button("Show Recommendations"):
        if uploaded_file:
            pdf_image, pdf_base64, resume_txt = extract_pdf_image_and_text(uploaded_file)
            response = get_gemini_response(
                input_text,
                [{"mime_type": "image/jpeg", "data": pdf_base64}],
                skill_recommendation_prompt
            )
            st.subheader("Improvement Steps")
            st.write(response)
            download_text_file(response, "Download Suggestions")
            st.session_state['history'].append({
                "type": "Skill Reco",
                "at": str(datetime.now()),
                "out": response
            })
        else:
            st.warning("Please upload your resume.")

elif selected_page == "📂 Resume Preview":
    st.header("Your Uploaded Resume")
    _, uploaded_file = upload_section()
    if uploaded_file:
        pdf_image, _, resume_txt = extract_pdf_image_and_text(uploaded_file)
        st.image(pdf_image, caption="First Page Snapshot", use_container_width=True)
        with st.expander("Extracted Resume Text"):
            st.write(resume_txt)
    else:
        st.info("Upload a resume to preview.")

elif selected_page == "🕒 Session History":
    st.header("Your Reports This Session")
    if st.session_state['history']:
        for item in reversed(st.session_state['history']):
            with st.expander(f"{item['type']} at {item['at'][:19]}"):
                st.write(item['out'])
                download_text_file(item['out'], "Download This Report")
    else:
        st.info("No analyses yet in this session.")

elif selected_page == "❓ Help / FAQ":
    st.header("Help and FAQs")
    st.markdown("""
**PDF only. Data is not stored.  
ATS = resume screener used by employers.  
Session history is temporary—reports disappear when you reload the app.**
""")



