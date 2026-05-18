import streamlit as st
import pandas as pd

st.set_page_config(page_title='Naruvi', layout='wide')

st.title('Naruvi - AI Data Analyst Interview Coach')
st.subheader('Built for Sugan')

module = st.sidebar.selectbox('Choose Module', ['SQL Practice','Python Interview','Power BI','HR Interview','Job Tracker'])

if module == 'SQL Practice':
    st.header('SQL Practice')
    questions = [
        'Find the second highest salary.',
        'Difference between WHERE and HAVING?',
        'Explain INNER JOIN vs LEFT JOIN.'
    ]
    for q in questions:
        st.write('- ' + q)

elif module == 'Python Interview':
    st.header('Python Interview')
    st.write('- Explain Pandas groupby().')
    st.write('- How did you use Python in your PhonePe project?')

elif module == 'Power BI':
    st.header('Power BI')
    st.write('- Difference between measure and calculated column?')
    st.write('- Explain star schema.')

elif module == 'HR Interview':
    st.header('Resume-Based Questions')
    st.write('- Explain your YouTube ETL project.')
    st.write('- Why should we hire you for a data analyst role?')

elif module == 'Job Tracker':
    st.header('Job Tracker')
    df = pd.DataFrame(columns=['Company','Role','Status'])
    st.dataframe(df)
