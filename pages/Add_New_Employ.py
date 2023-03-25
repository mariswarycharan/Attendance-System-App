import streamlit as st
from PIL import Image
import pickle 
import os

st.title("Add_New_Employ!!!")

employ_name = st.text_input("Enter the name of employ")
employ_role = st.text_input("Enter the role of employ")
employ_photo = st.file_uploader("upload the photo")

names_list = pickle.load(open("employ_name_list.pickle","rb"))


submit = st.button("SUBMIT")


if submit:
    image = Image.open(employ_photo)
    if employ_name.lower() not in names_list:
        names_list.append(employ_name.lower())
        names_list.sort()
        pickle.dump(names_list,open("employ_name_list.pickle","wb"))
        
        image.save(r"employ_images/"+employ_name.lower()+".png")
        
        st.success("successfully uploaded!!!")
    else:
        st.info("employ name already exist")
        
# --------------------------------------------------------------------------------------------------------------------------#
        
st.title("Delete any employ")

search_employ = st.text_input("search employ")
not_found_list = []
for i  in [".png",".jpg",".jfif",".jpeg"]:
    try:
        
        find_image = Image.open("employ_images/"+search_employ+i)
        path_of_find_employ = "employ_images/"+search_employ+i
        
        st.image(find_image)
    
    except:
        if search_employ == "":
            pass
        else:
            not_found = "Employ not found "+ search_employ
            not_found_list.append(not_found)
        pass
    
if len(not_found_list) == 4:
    st.warning(not_found)
    
delete_employ_button = st.button("Delete")

if delete_employ_button:
    
    if search_employ.lower() in names_list:
        os.remove(path_of_find_employ)
        
        names_list.remove(search_employ.lower())
        names_list.sort()
        pickle.dump(names_list,open("employ_name_list.pickle","wb"))
        
        st.success("successfully deleteed!!!")
    else:
        st.warning("employ does not exist")


