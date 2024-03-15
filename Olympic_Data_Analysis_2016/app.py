import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("athlete_events.csv")
region_df=pd.read_csv("noc_regions.csv")

df=preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image("pngegg.png")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu=="Medal Tally":
    st.sidebar.header("Medal Tally")
    years , country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select years: ",years)
    selected_country =st.sidebar.selectbox("Select Country: ",country)

    medal_tallly = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=="Overall" and  selected_country=="Overall":
        st.title("Overall  Tally")
    if selected_year != "Overall" and selected_country=="Overall":
        st.title("Medle Tally in  "+ str(selected_year) + " Olympics")
    if selected_year=="Overall" and selected_country!="Overall":
        st.title(selected_country + " Overall  performance")
    if selected_year!="Overall" and selected_country!="Overall":
        st.title(selected_country + "  performace in " +str(selected_year) +" Olympics")
    st.table(medal_tallly)

if user_menu=="Overall Analysis":
    editions=df["Year"].unique().shape[0] -1
    cities=df["City"].unique().shape[0] 
    sports=df["Sport"].unique().shape[0] 
    events=df["Event"].unique().shape[0] 
    athletes=df["Name"].unique().shape[0] 
    nations=df["region"].unique().shape[0] 


    st.title("Top Statistics")
    col1 , col2, col3 =st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1 , col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

#GRAPH 1 : OVERALL ANALYSIS 
    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time,x="Edition", y="region")
    st.title("Participating Nations Over the years")
    st.plotly_chart(fig)
#GRAPH 2
    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time,x="Edition", y="Event")
    st.title("Events Over the years")
    st.plotly_chart(fig)
#GRAPH 3
    atheletes_over_time = helper.data_over_time(df,'Name')
    fig = px.line(atheletes_over_time,x="Edition", y="Name")
    st.title("Atheletes Over the years")
    st.plotly_chart(fig)

#GRAPH 4 : HEATMAP 

    st.title("No of Events over time(Every Sports)")
    fig ,ax= plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(["Year","Sport","Event"])
    x=x.pivot_table(index="Sport",columns="Year",values="Event",aggfunc="count").fillna(0).astype('int')
    ax = sns.heatmap(x,annot=True)
    st.pyplot(fig)

#TAbel most sucessful athletes:
    st.title("Most sucessful Atheletes")
    sport_list=df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,"Overall")

    selected_sport = st.selectbox("Select a Sprot",sport_list)
    x=helper.most_sucessful(df,selected_sport)
    st.table(x)

    
if user_menu=="Country-wise Analysis":
#Country wise medal tally graph 
    st.title("Country wise Medal Tally Graph")
    country=df["region"].dropna().unique().tolist()
    country.sort()
 
    st.sidebar.title("Country-wise analysis")
    selected_country_list =st.sidebar.selectbox("Select country: ",country)
    country_df = helper.yearwise_medal_tally(df , selected_country_list)
    st.title(selected_country_list + " Medal Tally over the years")
    fig = px.line(country_df , x="Year", y= "Medal")
    st.plotly_chart(fig)

    st.title(selected_country_list + " Excels in the following Sports")
    pt = helper.country_event_heatmap(df, selected_country_list)
    fig ,ax= plt.subplots(figsize=(20,20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)


    st.title("Top 10 Atheltes of "+ selected_country_list)
    top_10_df = helper.most_sucessful_country_wise(df,selected_country_list)
    st.table(top_10_df)

if user_menu=="Athlete wise Analysis":
    athletes_df = df.drop_duplicates(subset=["Name","region"])
    x1= athletes_df["Age"].dropna()
    x2= athletes_df[athletes_df["Medal"]=="Gold"]["Age"].dropna()
    x3= athletes_df[athletes_df["Medal"]=="Silver"]["Age"].dropna()
    x4= athletes_df[athletes_df["Medal"]=="Bronze"]["Age"].dropna()

    fig = ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalist','Silver Medalist','Bronze Medalist'], show_hist=False , show_rug=False)
    # fig.update_layout(autosize=False , width=800 , height=600)
    st.title("Distribution of Age ")
    st.plotly_chart(fig)
    
    x= []
    name=[]
    famous_sports=['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming', 'Badminton',
                    'Sailing', 'Gymnastics', 'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling', 
                    'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Shooting', 'Boxing', 
                    'Taekwondo', 'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Golf', 'Softball', 'Archery', 
                    'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball', 
                    'Rhythmic Gymnastics', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon',
                    'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df=athletes_df[athletes_df["Sport"]==sport]
        x.append(temp_df[temp_df["Medal"]=='Gold']["Age"].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False , width=800 , height=600)
    st.title("Distribution of Age with respect to Sports (Gold Medals )")
    st.plotly_chart(fig)


    st.title("Men VS Women participation over the years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=['Male','Female'])
    st.plotly_chart(fig)