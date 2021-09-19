# Project Peacock: Streamlit Resume hosted on github


import streamlit as st


st.set_page_config(page_title='Resume', page_icon=None, layout='centered', initial_sidebar_state='collapsed')

st.title('Loy Tze Hao, Glen')
c1,c2,c3,c4 = st.columns(4)
c1.text('Contact me')
c2.text('Github')
c3.text('Linkedin')
c4.text('Singapore')

st.header('Education and Qualifications')

st.subheader('Bachelor of Science (Honours), Major in Applied Mathematics')
st.write('National University of Singapore')
exp1 = st.expander('Coursework')
with exp1:
	st.write("Calculus, Linear Algebra, Combinatorics, Probability, Numerical Analysis, Real Analysis, Complex Analysis, Multivariate Calculus, Nonlinear Programming, Computer-Aided Data Analysis (R, SAS and SPSS), Financial Mathematics, Matrix Computation, Game Theory, Mathematical Logic, Stochastic Operations Research")

st.subheader('Master of Science, Professional Accountancy')
st.write('University of London')
exp2 = st.expander('Coursework')
with exp2:
	st.write("_In Progress_")

	
st.header('Membership to Professional Bodies')
st.subheader('Association of Chartered Certified Accountants (ACCA) - Affiliate') 



	
	

st.header('Professional Experience')





st.header('Skills')

with st.sidebar:
    st.write("Education")




