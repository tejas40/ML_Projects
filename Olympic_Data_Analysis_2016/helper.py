import pandas as pd

def medal_tally(df):
   #drop multiple medal for team errors 
   medal_tally=df.drop_duplicates(subset=['Team',"NOC","Games","Year","City","Sport","Event","Medal"])
   #group by on bais of region
   medal_tally = medal_tally.groupby('region').sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index()
   #Add new total column
   medal_tally["total"]=medal_tally["Gold"] + medal_tally["Silver"] +medal_tally["Bronze"]

   return medal_tally

def country_year_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country= df['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0,"Overall")

    return years , country 

def fetch_medal_tally(medal_df , years , country ):
    medal_df=medal_df.drop_duplicates(subset=['Team',"NOC","Games","Year","City","Sport","Event","Medal"])
    flag=0
    if years=="Overall" and country =="Overall":
        temp_df= medal_df
    if years=="Overall" and country!= "Overall":
        flag=1
        temp_df = medal_df[medal_df["region"]==country]
    if years!="Overall" and country=="Overall":
        temp_df=medal_df[medal_df["Year"]==int(years)]
    if years!="Overall" and country!="Overall":
        temp_df= medal_df[(medal_df["region"]==country) & (medal_df["Year"]==int(years))]
    
    if flag==1:
        x= temp_df.groupby('Year').sum()[["Gold","Silver","Bronze"]].sort_values("Year").reset_index()
        x["Year"]= x["Year"].astype("str")
    else:
        x= temp_df.groupby('region').sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index()
        
    x["total"]=x["Gold"] + x["Silver"] + x["Bronze"]

    x["Gold"] = x["Gold"].astype("int")
    x["Silver"] = x["Silver"].astype("int")
    x["Bronze"] = x["Bronze"].astype("int")
    x["total"] = x["total"].astype("int")

    return x


def data_over_time(df,col):
   nations_over_time = df.drop_duplicates(["Year",col])["Year"].value_counts().reset_index().sort_values('Year')
   nations_over_time.rename(columns={'Year':'Edition','count':col},inplace=True)
   return nations_over_time



def most_sucessful(df,sport):
    temp_df= df.dropna(subset="Medal")
    
    if sport !="Overall":
        temp_df= temp_df[temp_df["Sport"]==sport]
        
    x= temp_df["Name"].value_counts().reset_index().head(16).merge(df,left_on="Name",right_on="Name",how="left")[["Name",'count',"Sport",'region']].drop_duplicates('Name')
    x.rename(columns={"count":"Medals"},inplace=True)
    return x.reset_index().drop("index",axis=1)

def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset="Medal")
    temp_df.drop_duplicates(subset=['Team',"NOC","Games","Year","City","Sport","Event","Medal","ID"],inplace=True)
    new_df = temp_df[temp_df["region"]==country]
    final_df = new_df.groupby('Year').count()["Medal"].reset_index()
    return final_df 
    
def country_event_heatmap(df,country):
    temp_df = df.dropna(subset="Medal")
    temp_df.drop_duplicates(subset=['Team',"NOC","Games","Year","City","Sport","Event","Medal"],inplace=True)
    new_df = temp_df[temp_df["region"]==country]
    pt = new_df.pivot_table(index='Sport', columns="Year", values="Medal", aggfunc='count').fillna(0).astype('int')
    return pt


def most_sucessful_country_wise(df,country):
    temp_df= df.dropna(subset="Medal")
    temp_df= temp_df[temp_df["region"]==country]
        
    x= temp_df["Name"].value_counts().reset_index().head(11).merge(df,left_on="Name",right_on="Name",how="left")[["Name",'count',"Sport"]].drop_duplicates('Name')
    x.rename(columns={"count":"Medals"},inplace=True)
    return x.reset_index().drop("index",axis=1)


def men_vs_women(df):
    athletes_df = df.drop_duplicates(subset=["Name","region"])

    men= athletes_df[athletes_df["Sex"]=='M'].groupby("Year").count()["Name"].reset_index()
    women= athletes_df[athletes_df["Sex"]=='F'].groupby("Year").count()["Name"].reset_index()

    final = men.merge(women, on='Year')
    final.rename(columns={"Name_x":'Male',"Name_y":"Female"},inplace=True)

    final.fillna(0,inplace=True)

    return final