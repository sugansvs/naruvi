import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title='Naruvi V2', layout='wide')

sql_questions = [
    'Find second highest salary.',
    'Difference between WHERE and HAVING?',
    'Explain window functions.',
    'Write a CTE example.',
    'INNER JOIN vs LEFT JOIN?'
]
python_questions = [
    'Explain Pandas groupby().',
    'Difference between list and tuple.',
    'How do you handle missing values?',
    'Explain merge() in pandas.'
]
stats_questions = [
    'Mean vs Median?',
    'What is standard deviation?',
    'Correlation vs causation?'
]
resume_questions = [
    'Explain your YouTube ETL architecture.',
    'Why MySQL and MongoDB together?',
    'Business insights from PhonePe project?',
    'How did OCR work in BizCard project?'
]

st.title('Naruvi — AI Data Analyst Interview Coach')
st.caption('Built for Sugan | 40K Readiness Journey')

module = st.sidebar.radio('Choose Module', [
    'Dashboard',
    'SQL Practice',
    'Python Practice',
    'Statistics',
    'Resume Mock Interview',
    'HR Interview',
    'Job Tracker'
])

if module == 'Dashboard':
    st.header('Interview Readiness Dashboard')
    scores = pd.DataFrame({
        'Skill':['SQL','Python','Power BI','Statistics','Communication'],
        'Score':[72,68,75,60,65]
    })
    fig = px.bar(scores, x='Skill', y='Score')
    st.plotly_chart(fig, use_container_width=True)
    st.metric('40K Readiness Score', '68%')

elif module == 'SQL Practice':
    st.header('SQL Interview Practice')
    difficulty = st.selectbox('Difficulty',['Easy','Medium','Hard'])
    st.success(random.choice(sql_questions))

elif module == 'Python Practice':
    st.header('Python Interview Practice')
    st.info(random.choice(python_questions))

elif module == 'Statistics':
    st.header('Statistics Practice')
    st.warning(random.choice(stats_questions))

elif module == 'Resume Mock Interview':
    st.header('Resume Personalized Mock Interview')
    st.error(random.choice(resume_questions))
    answer = st.text_area('Your Answer')
    if st.button('Evaluate'):
        st.success('Good structure. Add more business impact and metrics.')

elif module == 'HR Interview':
    st.header('HR Practice')
    st.write('Tell me about yourself.')
    st.write('Why should we hire you?')
    st.write('Why remote data analyst role?')

elif module == 'Job Tracker':
    st.header('Job Application Tracker')
    company = st.text_input('Company')
    role = st.text_input('Role')
    status = st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
    if st.button('Save Entry'):
        st.success(f'Saved: {company} - {role} - {status}')
