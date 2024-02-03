# Data Science

Welcome to my "Data Science Project" repository! 🚀

In this repository, I'm sharing my all project source code with some explaination , feel free to check out my code and if u have any suggestion or doubt u can connect with me on my linkdln profil www.linkedin.com/in/tejas-kharde-847347226 

### **Notion Website published: **
For more documentation and get get step by step detail explaination about this project visite my notion wesite Here :

### **A.Overview:**

- This project aims to create an end-to-end movie recommendation system using the TMDB 5000 Movie Dataset.
- The system incorporates Exploratory Data Analysis (EDA) to understand the dataset's characteristics and patterns, followed by the development of a recommendation model.
- Additionally, a user-friendly front-end interface has been implemented to enhance the user experience.
- DATASET For our project:
    
    [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
    

### **B.Model Implementation:**

1. **Content Based Recommendation System**: ( We are Going to use This approch for our model ) 
    1. Content-based filtering considers the features of movies and users to make recommendations.
    2. It uses attributes such as genre, director, description, actors, etc. for movies, to make suggestions for the users. 
    3. The intuition behind this sort of recommendation system is that if a user liked a particular movie or show, he/she might like a movie or a show similar to it.
2.  **Collaborative Based Recommendation System:** 
    1. Collaborative filtering is employed to make recommendations based on the preferences of similar users.
    2. It matches users with same interests and gives recommendations based on their likes. 
        1. Eg: There are two users Sam and Robin, Sam likes movies A,B,C,D and Robin likes movies C,D. Since movies C,D are common to both Sam and Robin, thus movies A and B would be recommended to Robin. Collaborative filtering does not make use of metadata to give recommendations.
3. **Hybrid Model:**
    1. A hybrid recommendation model is implemented, combining collaborative and content-based filtering to leverage the strengths of both approaches.

## **C.Front-end Interface:**

- The front-end interface is developed using Streamlit, a Python library known for its simplicity and ease of use.
- User preferences, such as favorite genres, are collected through an intuitive and interactive interface.
- TMDB API is integrated to dynamically fetch movie posters, providing users with a visual representation of recommended movies.

## **Instructions for Running the Project:** 

1. Clone the repository to your local machine.
2. Install the required dependencies (provide details on requirement file).
3. Run the app.py type this command in cmd (streamlit run app.py)
4. Above command Launch the front-end interface on Streamlit server.
5. Explore movie recommendations based on your preferences.

![Machine Learning](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif)


**Happy Learning!** 🐍🤖
