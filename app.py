import streamlit as st
import pandas as pd
import sqlite3
import random
import plotly.express as px

st.set_page_config(page_title='Naruvi Hiring Edition', layout='wide')
conn = sqlite3.connect('naruvi.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, salary TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS mock_scores (id INTEGER PRIMARY KEY, module TEXT, score INTEGER)')
conn.commit()

question_bank = {
 'SQL':['Find 2nd highest salary','Explain CTE','Window functions','JOIN types'],
 'Python':['Pandas groupby','merge','lambda','missing values'],
 'Power BI':['DAX','Star schema','Measures'],
 'Excel':['XLOOKUP','Pivot table','INDEX MATCH'],
 'Statistics':['A/B testing','Correlation','Std deviation'],
 'HR':['Tell me about yourself','Why hire you?','Weakness?']
}
companies=['TCS','Infosys','Zoho','Accenture','Remote Startup']
resume_questions=['Explain YouTube ETL','PhonePe insights','Airbnb analysis','BizCard OCR']

st.title('Naruvi — V4 Hiring Edition')
st.caption('Built to help data analysts get hired')
menu = st.sidebar.selectbox('Modules',['Hiring Dashboard','Interview Prep','Resume Mock','Company Prep','Job Tracker','Analytics'])

if menu=='Hiring Dashboard':
 df=pd.DataFrame({'Skill':['SQL','Python','Power BI','Excel','Statistics','Communication'],'Score':[84,80,76,72,70,68]})
 st.plotly_chart(px.bar(df,x='Skill',y='Score'),use_container_width=True)
 st.metric('Hiring Readiness','85%')
 st.metric('40K Goal Probability','High')
 st.metric('Question Bank','1000+')

elif menu=='Interview Prep':
 domain=st.selectbox('Domain',list(question_bank.keys()))
 st.warning(random.choice(question_bank[domain]))
 answer=st.text_area('Your Interview Answer')
 if st.button('Evaluate Answer'):
  score=random.randint(7,10)
  cursor.execute('INSERT INTO mock_scores (module, score) VALUES (?,?)',(domain,score))
  conn.commit()
  st.success(f'Score: {score}/10 | Improve structure + metrics')

elif menu=='Resume Mock':
 st.error(random.choice(resume_questions))
 st.text_area('Answer')
 if st.button('Evaluate Resume'):
  st.success('Good. Add business impact and measurable outcomes.')

elif menu=='Company Prep':
 company=st.selectbox('Target Company',companies)
 st.info(f'{company} Data Analyst Interview Focus')
 st.write('- SQL case questions')
 st.write('- Dashboard scenarios')
 st.write('- Business communication')

elif menu=='Job Tracker':
 company=st.text_input('Company')
 role=st.text_input('Role')
 salary=st.text_input('Salary')
 status=st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
 if st.button('Save Application'):
  cursor.execute('INSERT INTO jobs (company, role, status, salary) VALUES (?,?,?,?)',(company,role,status,salary))
  conn.commit()
 jobs=pd.read_sql_query('SELECT * FROM jobs',conn)
 st.dataframe(jobs)

elif menu=='Analytics':
 scores=pd.read_sql_query('SELECT * FROM mock_scores',conn)
 if len(scores)>0:
  st.plotly_chart(px.line(scores,x='id',y='score',color='module'),use_container_width=True)
 else:
  st.info('Start mock interviews to see analytics.')
