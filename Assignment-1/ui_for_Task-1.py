from sqlalchemy.orm import query_expression
import streamlit as st
from Task_1 import open_db
from Task_1 import User, Upload, ChatView

def view_user_info():
    with st.form('f1'):
        PhoneNo = st.text_input("Enter phone number")
        User_Name = st.text_input("Enter user's name")
        Age = st.text_input("Enter user's age")
        Gender = st.radio('Gender',('Male','Female','Others'))
        btn = st.form_submit_button("Submit")

    if btn and PhoneNo and User_Name and Age and Gender:
        db = open_db()
        db.add(User(User_Name = User_Name, Age = Age, PhoneNo = PhoneNo , Gender=Gender)) 
        db.commit() # save
        db.close() # close the db
        st.success("Saved details")

def contacts():
    with st.form('f2'):
        CNumb = st.text_input("Enter phone number")
        CName = st.text_input("Enter contact's name")   
        btn = st.form_submit_button("Submit")
    if btn and CNumb and CName:
        db = open_db()
        db.add(Upload(CName = CName, CNumb = CNumb)) 
        db.commit() # save
        db.close() # close the db
        st.success("Saved details")

def chats():
    with st.form('f3'):
        chat = st.text_area('Start')
        btn = st.form_submit_button("Submit")

    if btn and chat:
        db = open_db()
        db.add(ChatView(chat = chat))
        db.commit() # save
        db.close() # close the db
        st.success("Saved details")
  

# UI code
st.title("Task_1")

options = ['Add user detail','Upload Contacts','Add Chat']

choice = st.sidebar.radio("Select any option", options)

if choice == options[0]:
    view_user_info()
elif choice == options[1]:
    contacts()
elif choice == options[2]:
    chats()
