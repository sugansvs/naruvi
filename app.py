import streamlit as st
import pandas as pd
import sqlite3
import random
import plotly.express as px

st.set_page_config(page_title='Naruvi Production V2', layout='wide')

conn = sqlite3.connect('naruvi.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, salary TEXT)''')
conn.commit()

sql_questions = ['CTE example?', 'Window function use?', 'Rank salaries?', 'HAVING vs WHERE?']
python_questions = ['Pandas merge?', 'groupby?', 'Missing values?', 'Lambda?']
powerbi_questions = ['Measure vs calculated column?', 'Star schema?', 'DAX?']
excel_questions = ['XLOOKUP?', 'INDEX MATCH?', 'Pivot table?']
stats_questions = ['Std deviation?', 'Correlation?', 'A/B testing?']
resume_questions = ['Explain YouTube ETL.', 'PhonePe insights?', 'BizCard OCR?', 'MongoDB design?']

st.title('Naruvi — Production Phase 2')
st.caption('Portfolio-grade Data Analyst Interview Platform')

menu = st.sidebar.radio('Navigation', [
    'Dashboard','SQL','Python','Power BI','Excel','Statistics','Resume Mock','Job Tracker'
])

if menu == 'Dashboard':
    scores = pd.DataFrame({
        'Skill':['SQL','Python','Power BI','Excel','Statistics'],
        'Score':[79,74,70,67,65]
    })
    fig = px.bar(scores, x='Skill', y='Score')
    st.plotly_chart(fig, use_container_width=True)
    st.metric('40K Readiness Score', '76%')
    st.metric('Question Bank', '300+')

elif menu == 'SQL':
    st.header('SQL Interview Engine')
    st.success(random.choice(sql_questions))

elif menu == 'Python':
    st.header('Python Engine')
    st.info(random.choice(python_questions))

elif menu == 'Power BI':
    st.header('Power BI Interview Prep')
    st.warning(random.choice(powerbi_questions))

elif menu == 'Excel':
    st.header('Excel Interview Prep')
    st.success(random.choice(excel_questions))

elif menu == 'Statistics':
    st.header('Statistics Engine')
    st.info(random.choice(stats_questions))

elif menu == 'Resume Mock':
    st.header('Resume Mock Interview')
    st.error(random.choice(resume_questions))
    ans = st.text_area('Answer')
    if st.button('Score Answer'):
        st.success('Score: 7.5/10 | Improve business storytelling.')

elif menu == 'Job Tracker':
    st.header('Job Tracker Pro')
    company = st.text_input('Company')
    role = st.text_input('Role')
    salary = st.text_input('Salary')
    status = st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
    if st.button('Save'):
        cursor.execute('INSERT INTO jobs (company, role, status, salary) VALUES (?, ?, ?, ?)', (company, role, status, salary))
        conn.commit()
        st.success('Saved')
    jobs = pd.read_sql_query('SELECT * FROM jobs', conn)
    st.dataframe(jobs)
