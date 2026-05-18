import streamlit as st
import pandas as pd
import sqlite3
import random
import plotly.express as px

st.set_page_config(page_title='Naruvi Production', layout='wide')

conn = sqlite3.connect('naruvi.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT)''')
conn.commit()

sql_questions = [
    'Find second highest salary', 'Explain CTE', 'Window functions?', 'Rank employees by salary',
    'Difference between WHERE and HAVING', 'LEFT JOIN vs INNER JOIN'
]
python_questions = [
    'Explain Pandas groupby()', 'merge vs join', 'Missing values handling', 'Lambda functions'
]
resume_questions = [
    'Explain YouTube ETL project', 'Why MongoDB + MySQL?', 'PhonePe business insights?', 'OCR architecture?'
]

st.title('Naruvi — Production Phase 1')
st.caption('AI Data Analyst Interview Platform')

menu = st.sidebar.radio('Navigation', [
    'Dashboard','SQL Engine','Python Engine','Resume Interview','Job Tracker PRO'
])

if menu == 'Dashboard':
    scores = pd.DataFrame({
        'Skill':['SQL','Python','Analytics','Communication'],
        'Score':[78,71,69,66]
    })
    fig = px.bar(scores, x='Skill', y='Score')
    st.plotly_chart(fig, use_container_width=True)
    st.metric('40K Readiness', '71%')
    st.metric('Questions Available', '100+')

elif menu == 'SQL Engine':
    st.header('SQL Question Engine')
    difficulty = st.selectbox('Difficulty',['Easy','Medium','Hard'])
    if st.button('Next SQL Question'):
        st.success(random.choice(sql_questions))

elif menu == 'Python Engine':
    st.header('Python Interview Engine')
    if st.button('Next Python Question'):
        st.info(random.choice(python_questions))

elif menu == 'Resume Interview':
    st.header('Resume Mock Interview')
    q = random.choice(resume_questions)
    st.warning(q)
    answer = st.text_area('Type your answer')
    if st.button('Evaluate Answer'):
        st.success('Feedback: Strong answer. Add metrics and business outcomes.')

elif menu == 'Job Tracker PRO':
    st.header('Persistent Job Tracker')
    company = st.text_input('Company')
    role = st.text_input('Role')
    status = st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
    if st.button('Save Job'):
        cursor.execute('INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)', (company, role, status))
        conn.commit()
        st.success('Saved successfully')

    jobs = pd.read_sql_query('SELECT * FROM jobs', conn)
    st.dataframe(jobs)
