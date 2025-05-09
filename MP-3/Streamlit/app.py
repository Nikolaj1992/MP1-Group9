import streamlit as st
import read_image
import read_api
import problem_formulation as pf
import classification as cf
import clustering 
import linear_regression

from PIL import Image
logo = Image.open('./media/esc.jpg')

# Function to display the homepage content
def show_homepage():
    st.image(logo)
    st.title('MP3')
    st.write('This Project is an analysis of European Song contest.')
    st.write("Made by: Jenny, David, Nikolaj and Patrick")
    st.write("Sem 4, BI, 2025")

# Main function that runs the app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "MP3 questions reformulated","Regression","Classification","Clustering", "Picture Analyzer", "ApiReader"])

    if page == "Homepage":
        show_homepage()
    elif page == "MP3 questions reformulated":
        pf.show_problem_formulation()  
    elif page == "Regression":
        linear_regression.show_linear_regression()
    elif page == "Classification":
        cf.show_classification()
    elif page == "Clustering":
        clustering.show_clustering()
    elif page == "Picture Analyzer":
        read_image.participant_analyzer()
    elif page == "ApiReader":
        read_api.fetch_eurovision_data()

if __name__ == "__main__":
    main()
