#........................Project Title Airbnb Data Analysis********.................................
#import Useful libraries
import git
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import streamlit as st
from PIL import Image
import requests
import plotly.graph_objects as go



#streamlit configaration

st.set_page_config(page_title= "AIRBNB ANALYSIS",layout= "wide")
st.title(":rainbow[AIRBNB ANALYSIS]")
df= pd.read_csv("C:/Users/admin pc/OneDrive/Desktop/Airbnb_project/Airbnb.csv")
tab1, tab2 = st.tabs(["HOME", "EXPLORE"])

with tab1:
    image=Image.open("airbnbimage.png")
    st.image(image,width=400)

    st.sidebar.header(":red[Airbnb Analysis]")
    st.sidebar.caption(":green[Data Extraction]")
    st.sidebar.caption(":green[Data Cleaning and Preparation]")
    st.sidebar.caption(":green[Visualization using streamlit]")
    st.sidebar.caption(":green[Availability Analysis by Season]")
    st.sidebar.caption(":green[Location-Based Insights]")
    st.sidebar.caption(":green[Interactive Visualizations]")
    st.sidebar.caption(":green[Dashboard Creation]")
    

    st.text_area(":red[ABOUT PROJECT]:",
                  "This project aims to analyze Airbnb data (Exctracted from github Respiratory), perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends")
    
    st.text_area(":red[ABOUT AIRBNB]",
                 "Airbnb is an American company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking.")
    
    st.text_area(":red[WHAT IS STREAMLIT USED FOR]",
                 "Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time. Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application")
    st.text_area(":red[ABOUT TABLEAU]",
                 "Tableau is most known for its wide range of data visualization capabilities, and is often used interchangeably with other traditional BI tools.")
    st.text_area(":red[ADVANTAGES OF TABLEAU]","Bussiness intelligence,Data visualization,Data colllaboration,Real-time data analysis,Can import lagre size of data")
    st.text_area(":red[Tools Used For this Project]","Python,VSCODE,Github,Streamlit,Tableau")






with tab2:
    #To upload file
    uploaded_file=st.file_uploader("Upload your file here",type=["CSV","XLS","XLXL","TXT"])
    if uploaded_file is not None:
    
         df= pd.read_csv("C:/Users/admin pc/OneDrive/Desktop/Airbnb_project/Airbnb.csv")
         button=st.button("Click here to view dataframe")
         if button: 
              st.write(df.head(5))

    plot_select=st.selectbox("Select",("TOP 10 PROPERTY TYPES IN AIRBNB BAR CHART","TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART","TOP 10 HOSTS "))
     #visualization of Available property type in Airbnb
    if plot_select=="TOP 10 PROPERTY TYPES IN AIRBNB BAR CHART":
                    df_coun=df["property_type"].value_counts()[:10]
                    df22=pd.DataFrame(df_coun).reset_index()
                    fig_1= px.bar(df22,x="property_type",y="count",title = "TOP 10 PROPERTY TYPES IN AIRBNB BAR CHART", height = 700,)
                    fig_1.update_layout(title_font=dict(size=23),title_font_color='#6739b7',xaxis_tickangle=-45,xaxis_title="Property_type")
                    st.plotly_chart(fig_1)

    if plot_select=="TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART":    
                    #visualization of Types of Rooms provided by Airbnb
                    df_room=df["room_type"].value_counts()
                    df_room=pd.DataFrame(df_room).reset_index()
                    fig_2= px.pie(df_room,names="room_type",values="count",title = "TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART")
                    fig_2.update_layout(title_font=dict(size=23),title_font_color='#6739b7')
                    st.plotly_chart(fig_2)


    if plot_select=="TOP 10 HOSTS ":
                    host=df["host_name"].value_counts()[:10]
                    pd_host=pd.DataFrame(host).reset_index()
                    fig_3= px.line(pd_host,x="host_name",y="count",title = "TOP 10 HOSTS ", height = 700)
                    fig_3.update_layout(title_font=dict(size=23),title_font_color='#6739b7',xaxis_tickangle=-45,xaxis_title="HOSTS_NAME")
                    st.plotly_chart(fig_3)





   

#To alloow th user to filter by country,proprty type, room type and view related plots
    col1,col2,col3=st.columns(3)
    with col1:
       country =st.selectbox('Select a Country',sorted(df.country.unique()))
    with col2:  
       prop = st.selectbox('Select Property_type',sorted(df.property_type.unique()))
    with col3:    
       room = st.selectbox('Select Room_type',sorted(df.room_type.unique()))                      
            
    #To view avarage listing of  top 10 hosts
    df_1=df[(df['country']==country)&(df["property_type"]==prop) &  (df["room_type"]==room)]
    df_1=df_1.groupby("host_name")["price"].mean()
    df_1=pd.DataFrame(df_1).sort_values(by='price',ascending=False)[:10]
    df_1.rename(columns={"price":"average_price"},inplace=True)
    df_1.reset_index(inplace=True)

    fig_avg = px.scatter(df_1,x='host_name',y='average_price',color="average_price",title='Average Price for top 10 host',color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig_avg)
    #Average Price for each Room type
    df_bed_avai=df[(df['country']==country)&(df["property_type"]==prop) &  (df["room_type"]==room)]
    df_bed_avai=df_bed_avai.groupby("bedrooms")["availability"].sum()
    df_bed_avai=pd.DataFrame(df_bed_avai)
    df_bed_avai.rename(columns={"availability":"Total_Availability"},inplace=True)
    df_bed_avai.reset_index(inplace=True)
    fig_31 = px.bar(df_bed_avai,x="bedrooms",y="Total_Availability",title='Average Price for each Room type')
    st.plotly_chart(fig_31)
 
    










    select = st.radio('Select One',[":red[Price Analysis]",":red[Availability Analysis]",":red[Location-Based Analysis]"])
    

    if select==":red[Price Analysis]":
                    #Average Price for each Room type
                    pr_df = df.groupby('room_type',as_index=False)['price'].mean().sort_values(by='price')
                    pr_df=pd.DataFrame(pr_df).rename(columns={'price':'Average_price'})
                    fig_3 = px.bar(data_frame=pr_df,x='room_type',y='Average_price',color='Average_price',title='Average Price for each Room type')
                    st.plotly_chart(fig_3,use_container_width=True)

                    #PRICE FOR PROPERTY_TYPES
                    df_price_prop=df.groupby("property_type")[["price","review_scores","number_of_reviews"]].mean()
                    df_price_prop=pd.DataFrame(df_price_prop).rename(columns={"price":"Average_price","review_scores":"Average_review_scores","number_of_reviews":"Average_number_of_reviews"}).reset_index()
                    fig_bar= px.bar(df_price_prop, x='property_type', y="Average_price", title= "AVERAGE PRICE FOR PROPERTY_TYPES",hover_data=["Average_review_scores","Average_number_of_reviews",],color_discrete_sequence=px.colors.sequential.Redor_r, width=800, height=600)
                    fig_bar.update_layout(xaxis_tickangle=-45)
                    st.plotly_chart(fig_bar)


                     #AVERAGE MONTHLY PRICE FOR PROPERTY_TYPES
                    pr_df = df.groupby('property_type',as_index=False)['monthly_price'].mean().sort_values(by='monthly_price',ascending=False)
                    pr_df=pr_df.rename(columns={'monthly_price':'Average_monthly_price'})
                    fig_sctt= px.scatter(pr_df[:10], x='property_type', y= "Average_monthly_price", title= "AVERAGE MONTHLY PRICE FOR PROPERTY_TYPES",color_discrete_sequence=px.colors.sequential.Redor_r, width=800, height=600)
                    st.plotly_chart(fig_sctt)



                    #SECURITY DEPOSIT BASED ON HOST

                    df_sec = df.groupby('name',as_index=False)['security_deposit'].mean().sort_values(by="security_deposit",ascending=False)[:10]
                    df_sec=pd.DataFrame(df_sec).rename(columns={"security_deposit":"Avarage_security_deposit"})
                    fig_sec= px.bar(df_sec, x='name', y="Avarage_security_deposit", title= "TOP 10 LISTING BY  SECURITY DEPOSIT")
                    st.plotly_chart(fig_sec)



                    #MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES
                    df2=df.price.sort_values(ascending=False)
                    df3=df.copy()
                    df3.drop("price",axis=1,inplace=True)
                    df3["Price"]=df2
                    
                    fig_1= px.bar(df3.head(20), x= "name",  y= "Price" ,color= "Price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3.head(20)["Price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
                    st.plotly_chart(fig_1)



                   
                 

  

    if select == ":red[Availability Analysis]":
                    
                    #Availability by Room_type
                    datafrm_room=df.groupby("room_type")["availability"].sum()
                    datafrm_room=pd.DataFrame(datafrm_room).reset_index() 
                    st.write(datafrm_room)
                    fig_avial = px.box(datafrm_room,x='room_type',y='availability',color='room_type',title='Availability by Room_type')
                    st.plotly_chart(fig_avial,use_container_width=True) 
                      

                    #Availability by Room_type
                    df_prprty=df.groupby("property_type")["availability"].sum()
                    df_prprty=pd.DataFrame(df_prprty).reset_index()
                    fig_avial = px.bar(df,x='property_type',y='availability',color='property_type',title='Availability by property_type')
                    fig_avial.update_layout(xaxis_tickangle=-45) 

                    st.plotly_chart(fig_avial,use_container_width=True)
  
                    #Availability cleaning_fee
                    df_sunb= px.sunburst(df, path=["room_type","bed_type","host_identity_verified"], values="availability",width=600,height=500,title="Availability of property with host_identity_verification",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
                    st.plotly_chart(df_sunb)


                    #Availability of listing in countries

                    df_county_=df.groupby("country")["availability"].sum()
                    df_county_=pd.DataFrame(df_county_).reset_index().rename(columns={"availability":"Total_Availability"})
                    fig_user=px.scatter(df_county_, x="country", y="Total_Availability", color="country",title="Availability of listing in countries")
                    st.plotly_chart(fig_user)




    
    if select == ":red[Location-Based Analysis]":
                  
                    
                    #Geospatial Distribution of Listings
                    fig_scttatr= px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', 
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
                    fig_scttatr.update_layout(width=800,height=600,title='Geospatial Distribution of Listings')
                    st.plotly_chart(fig_scttatr) 
                   
                    #LISTINGS BY COUNTRY CHOROPLETH MAP
                    url= "https://raw.githubusercontent.com/openlayers/ol3/6838fdd4c94fe80f1a3c98ca92f84cf1454e232a/examples/data/geojson/countries.geojson"
                    response = requests.get(url)
                    data1= json.loads(response.content)
                    Geo_country=[feature["properties"]["name"] for feature in data1["features"]]
                    Geo_country.sort()
                    Geo_country_df=pd.DataFrame({"country":Geo_country})
                    Geo_country_df["property_type"]=df["property_type"]
                    Geo_country_df["price"]=df["price"]
                    fig = px.choropleth( Geo_country_df, geojson=url, featureidkey='properties.name',locations='country',color='property_type',hover_name="country",hover_data="price",color_continuous_scale='thermal',title = 'Geo map for Airbnb  Analysis')
                    fig.update_geos(fitbounds="locations", visible=False)
                    fig.update_layout(title_font=dict(size=33),title_font_color='#6739b7',width=800, height=800)
                    fig['layout']['xaxis']['fixedrange'] = False 
                    fig['layout']['yaxis']['fixedrange'] = False
                    st.plotly_chart(fig,use_container_width=True)


#Here completed the project Airbnb Analysis