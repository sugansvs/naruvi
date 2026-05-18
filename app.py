import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from modules.question_engine import load_questions, get_random_question
from modules.scoring import evaluate_answer
from modules.resume_coach import get_resume_questions
from modules.company_tracks import get_company_tracks

st.set_page_config(page_title='Naruvi V5', layout='wide')
conn = sqlite3.connect('naruvi.db', check_same_thread=False)
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

st.title('Naruvi — V5 Real Product')
menu = st.sidebar.selectbox('Modules',['Dashboard','Mock Interview','Resume Coach','Company Prep'])

if menu == 'Dashboard':
    df = pd.DataFrame({'Skill':['SQL','Python','Power BI','Excel'],'Score':[85,80,76,73]})
    st.plotly_chart(px.bar(df,x='Skill',y='Score'), use_container_width=True)
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
    questions = get_resume_questions()
    st.error(get_random_question(questions))
elif menu == 'Company Prep':
    tracks = get_company_tracks()
    company = st.selectbox('Target Company', list(tracks.keys()))
    for topic in tracks[company]:
        st.write('- ' + topic)
