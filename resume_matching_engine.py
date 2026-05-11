# import re
# import math
# from collections import defaultdict

# # Define the SKILL_ALIASES dictionary
# SKILL_ALIASES = {
#     # Languages
#     "python": "python",
#     "pyhton": "python",
#     "java": "java",
#     "javascript": "javascript",
#     "javascrpit": "javascript",
#     "js": "javascript",
#     "typescript": "typescript",
#     "typescrpit": "typescript",
#     "c++": "cpp",
#     "cpp": "cpp",
#     "r": "r",
#     "kotlin": "kotlin",
#     # ML / Data
#     "machinelearning": "machine_learning",
#     "machine learning": "machine_learning",
#     "ml": "machine_learning",
#     "sklearn": "machine_learning",
#     "deeplearning": "deep_learning",
#     "deep learning": "deep_learning",
#     "deep-learning": "deep_learning",
#     "tensorflow": "tensorflow",
#     "pytorch": "pytorch",
#     "keras": "keras",
#     "nlp": "nlp",
#     "bert": "bert",
#     "xgboost": "xgboost",
#     "feature engineering": "feature_engineering",
#     "statistics": "statistics",
#     "stats": "statistics",
#     "regression": "regression",
#     "clustering": "clustering",
#     "data-viz": "data_visualization",
#     "data visualization": "data_visualization",
#     "data viz": "data_visualization",
#     "matplotlib": "data_visualization",
#     "tableau": "data_visualization",
#     "power-bi": "data_visualization",
#     "power bi": "data_visualization",
#     "powerbi": "data_visualization",
#     "pandas": "pandas",
#     "numpy": "numpy",
#     # Web — Frontend
#     "react": "react",
#     "reacts": "react",
#     "reactjs": "react",
#     "vue": "vue",
#     "vue.js": "vue",
#     "vuejs": "vue",
#     "redux": "redux",
#     "tailwind": "tailwind",
#     "html/css": "html_css",
#     "html css": "html_css",
#     "html": "html_css",
#     "css": "html_css",
#     "jest": "jest",
#     "graphql": "graphql",
#     # Web — Backend
#     "node.js": "nodejs",
#     "nodejs": "nodejs",
#     "node js": "nodejs",
#     "flask": "flask",
#     "spring boot": "spring_boot",
#     "springboot": "spring_boot",
#     "rest api": "rest_api",
#     "rest": "rest_api",
#     "restapi": "rest_api",
#     "microservices": "microservices",
#     # Databases
#     "sql": "sql",
#     "mysql": "mysql",
#     "mysq": "mysql",
#     "postgresql": "postgresql",
#     "postgres": "postgresql",
#     "mongodb": "mongodb",
#     "redis": "redis",
#     # DevOps / Cloud
#     "docker": "docker",
#     "kubernetes": "kubernetes",
#     "kubernates": "kubernetes",
#     "k8s": "kubernetes",
#     "ci/cd": "ci_cd",
#     "cicd": "ci_cd",
#     "ci cd": "ci_cd",
#     "aws": "aws",
#     # Mobile
#     "android": "android",
#     "firebase": "firebase",
#     # CS Fundamentals
#     "algorithms": "algorithms",
#     "algoritms": "algorithms",
#     "data structure": "data_structures",
#     "data structures": "data_structures",
#     "competitive programming": "competitive_programming",
#     # Design
#     "ui/ux": "ui_ux",
#     "ui ux": "ui_ux",
#     "figma": "figma",
# }

# # Resume dataset
# resumes = [
#     {"id": "01", "name": "Arjun Sharma", "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
#     {"id": "02", "name": "Priya Nair", "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
#     {"id": "03", "name": "Rahul Gupta", "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
#     {"id": "04", "name": "Sneha Patel", "skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"},
#     {"id": "05", "name": "Vikram Singh", "skills": "C++, Algoritms, Data Structure, competitive programming, python"},
#     {"id": "06", "name": "Ananya Krishnan", "skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
#     {"id": "07", "name": "Karan Mehta", "skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"},
#     {"id": "08", "name": "Deepika Rao", "skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
#     {"id": "09", "name": "Aditya Kumar", "skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
#     {"id": "10", "name": "Meera Iyer", "skills": "python, R, statistics, ML, regression, clustering, Power-BI"},
# ]

# # Job description dataset
# job_descriptions = [
#     {"id": "JD-1", "company": "Kakao", "role": "ML Engineer", "requiredskills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "SQL", "Data Visualization"], "preferredskills": ["NLP", "BERT", "Feature Engineering", "Statistics"]},
#     {"id": "JD-2", "company": "Naver", "role": "Backend Engineer", "requiredskills": ["Java", "Spring Boot", "MySQL", "PostgreSQL", "Microservices", "Docker", "Kubernetes"], "preferredskills": ["REST API", "CI/CD", "Redis"]},
#     {"id": "JD-3", "company": "Line", "role": "Frontend Engineer", "requiredskills": ["JavaScript", "React", "Vue", "TypeScript", "REST API", "HTML/CSS"], "preferredskills": ["Node.js", "GraphQL", "Redux", "Jest", "AWS"]},
# ]

# def normalize_skills(skills):
#     skills = skills.lower()
#     skills = re.split(r',\s*', skills)
#     normalized_skills = []
#     for skill in skills:
#         if skill in SKILL_ALIASES:
#             normalizedskills.append(SKILLALIASES[skill])
#         else:
#             for key in SKILL_ALIASES:
#                 if key in skill:
#                     normalizedskills.append(SKILLALIASES[key])
#                     break
#     return list(set(normalized_skills))

# def computetfidf(resumes):
#     vocabulary = set()
#     for resume in resumes:
#         vocabulary.update(resume["normalized_skills"])
#     vocabulary = sorted(list(vocabulary))
#     tfidfvectors = []
#     for resume in resumes:
#         tfidfvector = [0] * len(vocabulary)
#         for skill in resume["normalized_skills"]:
#             tf = 1 / len(resume["normalized_skills"])
#             df = sum(1 for r in resumes if skill in r["normalized_skills"])
#             idf = math.log(10 / df)
#             tf_idf = tf * idf
#             tfidfvector[vocabulary.index(skill)] = tf_idf
#         tfidfvectors.append(tfidfvector)
#     return vocabulary, tfidfvectors

# def computejdvectors(job_descriptions, vocabulary):
#     jd_vectors = []
#     for jobdescription in jobdescriptions:
#         jd_vector = [0] * len(vocabulary)
#         for skill in jobdescription["requiredskills"]:
#             skill = skill.lower()
#             if skill in SKILL_ALIASES:
#                 skill = SKILL_ALIASES[skill]
#             if skill in vocabulary:
#                 jd_vector[vocabulary.index(skill)] = 1
#         for skill in jobdescription["preferredskills"]:
#             skill = skill.lower()
#             if skill in SKILL_ALIASES:
#                 skill = SKILL_ALIASES[skill]
#             if skill in vocabulary:
#                 jd_vector[vocabulary.index(skill)] = 1
#         jdvectors.append(jdvector)
#     return jd_vectors

# def computecosinesimilarity(tfidfvectors, jd_vectors):
#     similarities = []
#     for tfidfvector in tfidfvectors:
#         similarity = []
#         for jdvector in jdvectors:
#             dotproduct = sum(x * y for x, y in zip(tfidfvector, jdvector))
#             magnitudetfidf = math.sqrt(sum(x  2 for x in tfidfvector))
#             magnitudejd = math.sqrt(sum(x  2 for x in jdvector))
#             similarity.append(dotproduct / (magnitudetfidf * magnitudejd))
#         similarities.append(similarity)
#     return similarities

# def rankcandidates(similarities, resumes, jobdescriptions):
#     rankings = []
#     for i, jobdescription in enumerate(jobdescriptions):
#         ranking = []
#         for j, resume in enumerate(resumes):
#             ranking.append((resume["name"], similarities[j][i]))
#         ranking.sort(key=lambda x: (-x[1], x[0]))
#         rankings.append(ranking[:3])
#     return rankings

# def main():
#     for resume in resumes:
#         resume["normalizedskills"] = normalizeskills(resume["skills"])
#     vocabulary, tfidfvectors = computetfidf(resumes)
#     jdvectors = computejdvectors(jobdescriptions, vocabulary)
#     similarities = computecosinesimilarity(tfidfvectors, jd_vectors)
#     rankings = rankcandidates(similarities, resumes, jobdescriptions)
#     for i, jobdescription in enumerate(jobdescriptions):
#         print(f"{jobdescription['id']} — {jobdescription['company']} ({job_description['role']})")
#         for name, score in rankings[i]:
#             print(f"{name}({score:.2f})")
#         print()

# if name == "main":
#     main()

import re
import math

# =========================
# Skill Alias Dictionary
# =========================

SKILL_ALIASES = {

    # Languages
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",

    # ML / Data
    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "stats": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",

    # Frontend
    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",
    "jest": "jest",
    "graphql": "graphql",

    # Backend
    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "springboot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",
    "microservices": "microservices",

    # Databases
    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",

    # DevOps / Cloud
    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",
    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",
    "aws": "aws",

    # Mobile
    "android": "android",
    "firebase": "firebase",

    # CS Fundamentals
    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "data structures": "data_structures",
    "competitive programming": "competitive_programming",

    # Design
    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma",
}

# =========================
# Resume Dataset
# =========================

resumes = [

    {
        "id": "01",
        "name": "Arjun Sharma",
        "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"
    },

    {
        "id": "02",
        "name": "Priya Nair",
        "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"
    },

    {
        "id": "03",
        "name": "Rahul Gupta",
        "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"
    },

    {
        "id": "04",
        "name": "Sneha Patel",
        "skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"
    },

    {
        "id": "05",
        "name": "Vikram Singh",
        "skills": "C++, Algoritms, Data Structure, competitive programming, python"
    },

    {
        "id": "06",
        "name": "Ananya Krishnan",
        "skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"
    },

    {
        "id": "07",
        "name": "Karan Mehta",
        "skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"
    },

    {
        "id": "08",
        "name": "Deepika Rao",
        "skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"
    },

    {
        "id": "09",
        "name": "Aditya Kumar",
        "skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"
    },

    {
        "id": "10",
        "name": "Meera Iyer",
        "skills": "python, R, statistics, ML, regression, clustering, Power-BI"
    }

]

# =========================
# Job Description Dataset
# =========================

job_descriptions = [

    {
        "id": "JD-1",
        "company": "Kakao",
        "role": "ML Engineer",

        "requiredskills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "SQL",
            "Data Visualization"
        ],

        "preferredskills": [
            "NLP",
            "BERT",
            "Feature Engineering",
            "Statistics"
        ]
    },

    {
        "id": "JD-2",
        "company": "Naver",
        "role": "Backend Engineer",

        "requiredskills": [
            "Java",
            "Spring Boot",
            "MySQL",
            "PostgreSQL",
            "Microservices",
            "Docker",
            "Kubernetes"
        ],

        "preferredskills": [
            "REST API",
            "CI/CD",
            "Redis"
        ]
    },

    {
        "id": "JD-3",
        "company": "Line",
        "role": "Frontend Engineer",

        "requiredskills": [
            "JavaScript",
            "React",
            "Vue",
            "TypeScript",
            "REST API",
            "HTML/CSS"
        ],

        "preferredskills": [
            "Node.js",
            "GraphQL",
            "Redux",
            "Jest",
            "AWS"
        ]
    }

]

# =========================
# Normalize Skills
# =========================

def normalize_skills(skills):

    skills = skills.lower()

    skills = re.split(r',\s*', skills)

    normalized_skills = []

    for skill in skills:

        skill = skill.strip()

        if skill in SKILL_ALIASES:

            normalized_skills.append(SKILL_ALIASES[skill])

        else:

            for key in SKILL_ALIASES:

                if key in skill:

                    normalized_skills.append(SKILL_ALIASES[key])

                    break

    return list(set(normalized_skills))

# =========================
# Compute TF-IDF Vectors
# =========================

def compute_tfidf(resumes):

    vocabulary = set()

    for resume in resumes:

        vocabulary.update(resume["normalized_skills"])

    vocabulary = sorted(list(vocabulary))

    tfidf_vectors = []

    for resume in resumes:

        tfidf_vector = [0] * len(vocabulary)

        for skill in resume["normalized_skills"]:

            tf = 1 / len(resume["normalized_skills"])

            df = sum(
                1 for r in resumes
                if skill in r["normalized_skills"]
            )

            idf = math.log(len(resumes) / df)

            tf_idf = tf * idf

            tfidf_vector[vocabulary.index(skill)] = tf_idf

        tfidf_vectors.append(tfidf_vector)

    return vocabulary, tfidf_vectors

# =========================
# Compute JD Vectors
# =========================

def compute_jd_vectors(job_descriptions, vocabulary):

    jd_vectors = []

    for job_description in job_descriptions:

        jd_vector = [0] * len(vocabulary)

        all_skills = (
            job_description["requiredskills"]
            + job_description["preferredskills"]
        )

        for skill in all_skills:

            skill = skill.lower()

            if skill in SKILL_ALIASES:

                skill = SKILL_ALIASES[skill]

            if skill in vocabulary:

                jd_vector[vocabulary.index(skill)] = 1

        jd_vectors.append(jd_vector)

    return jd_vectors

# =========================
# Cosine Similarity
# =========================

def compute_cosine_similarity(tfidf_vectors, jd_vectors):

    similarities = []

    for tfidf_vector in tfidf_vectors:

        similarity = []

        for jd_vector in jd_vectors:

            dot_product = sum(
                x * y for x, y in zip(tfidf_vector, jd_vector)
            )

            magnitude_tfidf = math.sqrt(
                sum(x ** 2 for x in tfidf_vector)
            )

            magnitude_jd = math.sqrt(
                sum(x ** 2 for x in jd_vector)
            )

            if magnitude_tfidf == 0 or magnitude_jd == 0:

                similarity.append(0)

            else:

                similarity.append(
                    dot_product / (magnitude_tfidf * magnitude_jd)
                )

        similarities.append(similarity)

    return similarities

# =========================
# Rank Candidates
# =========================

def rank_candidates(similarities, resumes, job_descriptions):

    rankings = []

    for i, job_description in enumerate(job_descriptions):

        ranking = []

        for j, resume in enumerate(resumes):

            ranking.append(
                (resume["name"], similarities[j][i])
            )

        ranking.sort(
            key=lambda x: (-x[1], x[0])
        )

        rankings.append(ranking[:3])

    return rankings

# =========================
# Main Function
# =========================

def main():

    # Normalize Resume Skills

    for resume in resumes:

        resume["normalized_skills"] = normalize_skills(
            resume["skills"]
        )

    # TF-IDF

    vocabulary, tfidf_vectors = compute_tfidf(resumes)

    # Job Description Vectors

    jd_vectors = compute_jd_vectors(
        job_descriptions,
        vocabulary
    )

    # Similarity

    similarities = compute_cosine_similarity(
        tfidf_vectors,
        jd_vectors
    )

    # Ranking

    rankings = rank_candidates(
        similarities,
        resumes,
        job_descriptions
    )

    # Output

    print("\n=========== Resume Matching Results ===========\n")

    for i, job_description in enumerate(job_descriptions):

        print(
            f"{job_description['id']} | "
            f"{job_description['company']} | "
            f"{job_description['role']}"
        )

        print("-" * 50)

        for name, score in rankings[i]:

            print(f"{name:<20} Score: {score:.4f}")

        print()

# =========================
# Run Program
# =========================

if __name__ == "__main__":
    main()