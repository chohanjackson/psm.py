#password strength meter with python and streamlit

import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Jackson Chohan", page_icon="🌘",layout="centered")

#custom css
st.markdown("""
<style>
     .main {text-align: center;}
     .stTextInput {width: 60% ! important; margin: auto; }
     .stButton button {width: 50%; background-color blue; color: white; font-size: 18px; }
     .stbutton button:hover {background-color: red; color: white;}      
</style>       
""" , unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

#function to check password strength
def check_password_strength(password):
     score = 0
     feedback = []

     if len(password) >= 8:
          score += 1   #increased score by 1
     else:
          feedback.append("❌ password should be **atleast 8 character long** .")

     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
          score += 1
     else:
          feedback.append("❌ password should include **both uppercase (A-Z) and lowercase (a-z)letters** .")               
     
     if re.search(r"\d" , password):
          score += 1
     else:
          feedback.append("❌ password should include **at least one number (0-9) ** .")

     #special characters 
     if re.search(r"[!@#$%^&]" , password):
          score += 1
     else:
          feedback.append("❌ Include **at least one special character (!@#$%^&) **. ") 

     #display password strength results
     if score == 4:
          st.success("✅ **strong password** - Your password is secure.") 
     elif score == 3:
          st.info("⚠️ **Moderate password** - Consider improving by adding more feature") 
     else:
          st.error("❌ **week password** - follow the suggestion below to strength it. ")     

     #feedback
     if feedback:
          with st.expander("🔍 **Improve Your password** "):
               for item in feedback:
                    st.write(item)
Password = st.text_input("Enter your password:", type="password", help="Enter your password is strong 🔐")                    

#Button working
if st.button("Check Strength"):
     if Password:
          check_password_strength(Password)
     else:
          st.warning("⚠️ Please enter a password first !")   #show warning if password empty   
