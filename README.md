# AI Resume Analyzer

AI Resume Analyzer is an intelligent tool that leverages artificial intelligence and natural language processing (NLP) to automate, enhance, and streamline the resume screening and evaluation process. It extracts key information, analyzes content, and provides actionable insights to help both job seekers and recruiters make smarter decisions.

---

## Features

- **Resume Parsing & Data Extraction**
  - Extracts contact details, skills, education, work history, and certifications from resumes in PDF, DOCX, and TXT formats.
  - Handles multiple languages and various resume layouts.

- **Keyword & Skill Matching**
  - Uses NLP to match relevant skills and qualifications from resumes to job descriptions or recruiter-defined criteria.
  - Highlights gaps and suggests missing skills.

- **Automated Scoring & Ranking**
  - Assigns scores to candidates based on customizable parameters like experience, education, and skill relevance.
  - Ranks candidates to help recruiters quickly identify top talent.

- **Personalized Feedback & Recommendations**
  - Generates tailored feedback for candidates, suggesting improvements for better alignment with job requirements.
  - Offers actionable tips to enhance resume quality and ATS compatibility.

- **Analytics & Insights**
  - Provides data-driven insights into the candidate pool, such as skills distribution and experience levels.
  - Identifies skill gaps and offers recommendations for both recruiters and candidates.

- **Integration & Scalability**
  - Integrates with Applicant Tracking Systems (ATS) and HR platforms via REST APIs or SDKs.
  - Scalable to handle high volumes of resumes.

- **Data Security & Privacy**
  - Implements robust security measures to protect sensitive user information and ensure compliance with data protection regulations.

---

## How It Works

1. **Upload Resume:** Upload resumes in supported formats or create one using the built-in AI-powered builder.
2. **AI Analysis:** The system parses the resume, extracting and structuring key information using NLP and machine learning models.
3. **Keyword & Skill Matching:** Extracted data is compared against job requirements to assess fit and highlight missing skills.
4. **Scoring & Ranking:** Each resume is scored and ranked based on predefined criteria.
5. **Feedback & Recommendations:** Personalized feedback is generated for candidates, including suggestions for improvement and ATS optimization.
6. **Download & Integration:** Candidates can download optimized resumes, and recruiters can integrate structured data into their ATS or HRIS.

---

## Benefits

- **Saves Time:** Automates screening and reduces manual effort for recruiters.
- **Improves Efficiency:** Provides consistent, unbiased evaluations and handles large resume volumes.
- **Enhances Candidate Experience:** Delivers fast feedback and actionable recommendations.
- **Drives Data-Driven Decisions:** Offers analytics and insights for better recruitment strategies.
- **Ensures Security:** Protects user data with industry-standard practices.

---

## Installation & Setup

1. **Clone the Repository**

2. **Create a Virtual Environment (Recommended)**

3. **Install Dependencies**

4. **Download NLP Models**
  
5. **Configure Environment Variables**
- Create a `.env` file in the `utils/` directory and add your API keys (e.g., for Google Gemini API):
  ```
  GOOGLE_API_KEY=your_google_gemini_api_key
  ```

6. **Run the Application**

