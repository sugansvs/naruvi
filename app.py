import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from modules.question_engine import load_questions, get_random_question
from modules.scoring import evaluate_answer
from modules.resume_coach import get_resume_questions
from modules.company_tracks import get_company_tracks
from modules.job_tracker import init_db

st.set_page_config(page_title='Naruvi V5 Phase C', layout='wide')
conn = init_db()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS mock_scores (id INTEGER PRIMARY KEY, module TEXT, score INTEGER)')
conn.commit()

question_files = {
    'SQL':'data/sql_questions.json',
    'Python':'data/python_questions.json',
    'Power BI':'data/powerbi_questions.json',
    'Excel':'data/excel_questions.json',
    'Statistics':'data/stats_questions.json',
    'HR':'data/hr_questions.json'
}

st.title('Naruvi — V5 Hiring Product')
menu = st.sidebar.selectbox('Modules',['Dashboard','Mock Interview','Resume Coach','Company Prep','Job Tracker','Analytics'])

if menu == 'Dashboard':
    df = pd.DataFrame({'Skill':['SQL','Python','Power BI','Excel','Statistics','Communication'],'Score':[86,82,78,75,72,70]})
    st.plotly_chart(px.bar(df,x='Skill',y='Score'), use_container_width=True)
    st.metric('Hiring Readiness','89%')
    st.metric('Target Salary','₹40K+')

elif menu == 'Mock Interview':
    domain = st.selectbox('Domain', list(question_files.keys()))
    questions = load_questions(question_files[domain])
    st.warning(get_random_question(questions))
    ans = st.text_area('Your Answer')
    if st.button('Evaluate'):
        score, feedback = evaluate_answer(ans)
        cursor.execute('INSERT INTO mock_scores (module, score) VALUES (?, ?)', (domain, score))
        conn.commit()
        st.success(f'Score: {score}/10')
        st.info(feedback)

elif menu == 'Resume Coach':
    st.error(get_random_question(get_resume_questions()))

elif menu == 'Company Prep':
    tracks = get_company_tracks()
    company = st.selectbox('Target Company', list(tracks.keys()))
    for topic in tracks[company]:
        st.write('- ' + topic)

elif menu == 'Job Tracker':
    company = st.text_input('Company')
    role = st.text_input('Role')
    salary = st.text_input('Salary')
    status = st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
    if st.button('Save Job'):
        cursor.execute('INSERT INTO jobs (company, role, status, salary) VALUES (?, ?, ?, ?)', (company, role, status, salary))
        conn.commit()
    jobs = pd.read_sql_query('SELECT * FROM jobs', conn)
    st.dataframe(jobs)

elif menu == 'Analytics':
    scores = pd.read_sql_query('SELECT * FROM mock_scores', conn)
    if len(scores):
        st.plotly_chart(px.line(scores, x='id', y='score', color='module'), use_container_width=True)
        st.dataframe(scores)
    else:
        st.info('No analytics yet.')
