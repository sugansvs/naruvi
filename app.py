import streamlit as st
import pandas as pd
import sqlite3
import random
import plotly.express as px

st.set_page_config(page_title='Naruvi Enterprise', layout='wide')
conn = sqlite3.connect('naruvi.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT, salary TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS mock_scores (id INTEGER PRIMARY KEY, module TEXT, score INTEGER)')
conn.commit()

question_bank = {
 'SQL':['Second highest salary?','CTE example?','Window function?'],
 'Python':['groupby?','merge()?','lambda?'],
 'Power BI':['DAX?','Star schema?'],
 'Excel':['XLOOKUP?','Pivot table?'],
 'Statistics':['A/B testing?','Correlation?']
}
resume_questions = ['Explain YouTube ETL','PhonePe insights?','Airbnb analysis?','BizCard OCR?']

st.title('Naruvi — Enterprise Phase 3')
menu = st.sidebar.selectbox('Modules',['Dashboard','Interview Engine','Resume AI Mock','Job Tracker Enterprise','Performance Analytics'])

if menu=='Dashboard':
 df=pd.DataFrame({'Skill':['SQL','Python','Power BI','Excel','Statistics'],'Score':[82,78,74,70,69]})
 st.plotly_chart(px.bar(df,x='Skill',y='Score'),use_container_width=True)
 st.metric('40K Readiness Score','82%')
elif menu=='Interview Engine':
 domain=st.selectbox('Domain',list(question_bank.keys()))
 st.warning(random.choice(question_bank[domain]))
 if st.button('Submit'):
  score=random.randint(6,10)
  cursor.execute('INSERT INTO mock_scores (module, score) VALUES (?,?)',(domain,score))
  conn.commit()
  st.success(f'Score: {score}/10')
elif menu=='Resume AI Mock':
 st.error(random.choice(resume_questions))
 st.text_area('Your Answer')
 if st.button('Evaluate'):
  st.success('Add business impact metrics.')
elif menu=='Job Tracker Enterprise':
 company=st.text_input('Company')
 role=st.text_input('Role')
 salary=st.text_input('Salary')
 status=st.selectbox('Status',['Applied','Interview','Rejected','Offer'])
 if st.button('Save Job'):
  cursor.execute('INSERT INTO jobs (company, role, status, salary) VALUES (?,?,?,?)',(company,role,status,salary))
  conn.commit()
 jobs=pd.read_sql_query('SELECT * FROM jobs',conn)
 st.dataframe(jobs)
elif menu=='Performance Analytics':
 scores=pd.read_sql_query('SELECT * FROM mock_scores',conn)
 if len(scores)>0:
  st.plotly_chart(px.line(scores,x='id',y='score',color='module'),use_container_width=True)
 else:
  st.info('No mock interview data yet.')
