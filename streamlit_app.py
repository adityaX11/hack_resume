import streamlit as st

from resume_matching_engine import (
    resumes,
    job_descriptions,
    normalize_skills,
    compute_tfidf,
    compute_jd_vectors,
    compute_cosine_similarity,
    rank_candidates
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📜",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: linear-gradient(
        to right,
        #141e30,
        #243b55
    );
}

/* Title */

.title {
    text-align: center;
    color: white;
    font-size: 55px;
    font-weight: bold;
    margin-bottom: 40px;
}

/* Job Card */

.job-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 35px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

/* Result Card */

.result-card {
    background: rgba(0,0,0,0.35);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    border-left: 6px solid #00ff99;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.25);
    transition: 0.3s;
}

.result-card:hover {
    transform: scale(1.02);
}

/* Company */

.company {
    color: #00ffcc;
    font-size: 34px;
    font-weight: bold;
}

/* Role */

.role {
    color: white;
    font-size: 24px;
    margin-top: 10px;
    margin-bottom: 20px;
}

/* Headings */

.heading {
    color: #ffd166;
    font-size: 21px;
    font-weight: bold;
    margin-top: 18px;
}

/* Skills */

.skills {
    color: #f1f1f1;
    font-size: 17px;
    line-height: 1.8;
}

/* Rank */

.rank {
    color: #00ff99;
    font-size: 20px;
    font-weight: bold;
}

/* Candidate Name */

.name {
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 8px;
}

/* Score */

.score {
    color: #dddddd;
    font-size: 18px;
    margin-top: 8px;
}

/* Section Heading */

.section-title {
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 25px;
}

/* Select Box */

div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.markdown(
    """
    <div class="title">
        📜 AI Resume Matching Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# PROCESS DATA
# =========================================

for resume in resumes:

    resume["normalized_skills"] = normalize_skills(
        resume["skills"]
    )

vocabulary, tfidf_vectors = compute_tfidf(
    resumes
)

jd_vectors = compute_jd_vectors(
    job_descriptions,
    vocabulary
)

similarities = compute_cosine_similarity(
    tfidf_vectors,
    jd_vectors
)

rankings = rank_candidates(
    similarities,
    resumes,
    job_descriptions
)

# =========================================
# JOB SELECTOR
# =========================================

selected_job = st.selectbox(
    "🎯 Select Job Role",
    [
        f"{job['id']} - {job['role']}"
        for job in job_descriptions
    ]
)

# =========================================
# DISPLAY
# =========================================

for i, job in enumerate(job_descriptions):

    current_job = f"{job['id']} - {job['role']}"

    if current_job == selected_job:

        # =================================
        # JOB DETAILS CARD
        # =================================

        st.markdown(
            f"""
<div class="job-card">

<div class="company">
🏢 {job['company']}
</div>

<div class="role">
💼 {job['role']}
</div>

<div class="heading">
✅ Required Skills
</div>

<div class="skills">
{", ".join(job['requiredskills'])}
</div>

<div class="heading">
⭐ Preferred Skills
</div>

<div class="skills">
{", ".join(job['preferredskills'])}
</div>

</div>
            """,
            unsafe_allow_html=True
        )

        # =================================
        # RESULT TITLE
        # =================================

        st.markdown(
            """
            <div class="section-title">
                🎯 Top Matching Candidates
            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================
        # RESULT CARDS
        # =================================

        for rank, (name, score) in enumerate(
            rankings[i],
            start=1
        ):

            st.markdown(
                f"""
<div class="result-card">

<div class="rank">
🏆 Rank #{rank}
</div>

<div class="name">
{name}
</div>

<div class="score">
📊 Match Score : {score:.4f}
</div>

</div>
                """,
                unsafe_allow_html=True
            )