import streamlit as st
st.write("Point Of View")
def main():
  form=st.form(key='my_form')
  username=st.text_input(label='Username')
  submit=form.form_submit_button(label='Go')
  
  if (submit):
    f=pd.DataFrame(username,index=[0])
    return username
  else:
    st.write("Error")
if __name__=='__main__':
	main()
