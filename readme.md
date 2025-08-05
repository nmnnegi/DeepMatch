# DeepMatch: AI Resume Analysis Suite

---

## Overview

DeepMatch is an AI-powered resume analysis suite built with Streamlit. Leveraging Google’s Gemini generative AI models, DeepMatch empowers job seekers to:

- Evaluate resumes against any job description intelligently.
- Get precise ATS (Applicant Tracking System) compatibility scoring.
- Receive personalized skill and career growth recommendations.
- Preview uploaded resume content.
- Maintain session report history with easy downloads.

This interactive web app is designed to boost your career chances by providing actionable insights from advanced AI, all in a privacy-conscious environment.

---

## Features

- **Resume Analysis:** Deep AI-powered review of your resume based on input job descriptions.
- **ATS Match & Score:** Calculate how well your resume matches ATS systems and identify missing keywords.
- **Skill Recommendations:** Receive targeted suggestions to close skill gaps.
- **Resume Preview:** View uploaded PDF resumes’ first page and extracted text.
- **Session History:** Access and download all previous reports generated during your session.
- **Secure & Private:** No data is stored permanently; all processing happens during the session.
- **Beautiful and Responsive UI:** Clean, user-friendly design using Streamlit and option menu.

---

## Installation and Local Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/deepmatch.git
cd deepmatch
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in root (not committed to git) with your Google Gemini API key:

```env
GOOGLE_API_KEY=your-google-api-key
```

5. Run the app locally:

```bash
streamlit run app.py
```

---

## Usage

- Paste or input the target job description.
- Upload your professional resume in PDF format.
- Use the sidebar to navigate:
  - Analyze your resume.
  - Check your ATS match score.
  - Get skill recommendations.
  - Preview your resume.
  - View and download past session reports.
- Download reports as text files for your reference.

---

## Deployment on Streamlit Community Cloud (No `.toml` Files Needed!)

Follow these steps to deploy your app securely with environment variables managed via Streamlit Cloud UI:

1. Push your code to a GitHub repository (don’t commit your `.env` or API keys).
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click **New app** → Select your GitHub repo and branch → Specify `app.py` as the entry point.
4. Click **Advanced settings** → Under **Secrets**, enter your Google API key in TOML format:

```toml
GOOGLE_API_KEY = "your-google-api-key"
```

5. Deploy the app.
6. Your app accesses the API key in code via:

```python
import streamlit as st

api_key = st.secrets["GOOGLE_API_KEY"]
```

---

## Troubleshooting

- **App hangs or doesn't respond:**  
  Ensure API keys are correctly set in Secrets. Use `st.error` to show missing keys.

- **Dependency conflicts during deployment:**  
  Use the provided `requirements.txt` with proper protobuf version (`protobuf>=3.20.2,<6.0.0`).

- **Large resume PDFs:**  
  Keep uploads moderate in size for smooth performance.

---

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or new features.

---

## License

Distributed under the MIT License. See `LICENSE` file for details.

---

## Acknowledgments

- Google Gemini AI for powerful generative AI backends.
- Streamlit for rapid UI and deployment.
- [Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu) for enhanced sidebar navigation.

---

Please reach out if you have questions or feedback!
