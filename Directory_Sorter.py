import os, shutil
import streamlit as st

# Use Streamlit's text_input widget to get the directory from the user
path = st.text_input("Paste Directory:")

if path:  # Only proceed if the user has entered a path
    file_name = os.listdir(path)

    folder_names = ["csv files", "Images", "pdfs", "apps", "Word docs", "Excel docs", "emails", "text files", "powerpoint docs"]

    for file in  file_name:
        if ".csv" in file:
            if not os.path.exists(path + "/" + folder_names[0]):
                os.makedirs(path + "/" + folder_names[0])
                shutil.move(path + "/" + file, path + "/" + folder_names[0] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[0] + "/" + file)
        elif ".png" in file:
            if not os.path.exists(path + "/" + folder_names[1]):
                os.makedirs(path + "/" + folder_names[1])
                shutil.move(path + "/" + file, path + "/" + folder_names[1] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[1] + "/" + file)

        elif ".pdf" in file:
            if not os.path.exists(path + "/" + folder_names[2]):
                os.makedirs(path + "/" + folder_names[2])
                shutil.move(path + "/" + file, path + "/" + folder_names[2] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[2] + "/" + file)
        elif ".exe" in file:
            if not os.path.exists(path + "/" + folder_names[5]):
                os.makedirs(path + "/" + folder_names[3])
                shutil.move(path + "/" + file, path + "/" + folder_names[3] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[3] + "/" + file)

        elif ".docx" in file:
            if not os.path.exists(path + "/" + folder_names[4]):
                os.makedirs(path + "/" + folder_names[4])
                shutil.move(path + "/" + file, path + "/" + folder_names[4] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[4] + "/" + file)
        elif ".xlsx" in file:
            if not os.path.exists(path + "/" + folder_names[5]):
                os.makedirs(path + "/" + folder_names[5])
                shutil.move(path + "/" + file, path + "/" + folder_names[5] + "/" + file)
            else:
                shutil.move(path + "/" + file, path + "/" + folder_names[5] + "/" + file)
            # Add similar conditions for other file types
        else:
            # Use Streamlit's error message to display files that were not moved
            st.error(file + " were not moved")

# Run this with 'streamlit run your_script.py' in your terminal
