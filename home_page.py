import streamlit as st
import pickle

names_list = pickle.load(open("employ_name_list.pickle","rb"))


# pickle.dump(["balaji","charan","guhan","pranav"],open("employ_name_list.pickle","wb"))

st.code(names_list)