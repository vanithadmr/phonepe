# imporing Important libaries :
import numpy as np 
import seaborn as sns 
import pandas as pd
import mysql.connector
from mysql.connector import Error
import plotly.express as px 
import matplotlib.pyplot as plt 
import streamlit as st 
import plotly.graph_objects as go
from plotly.subplots import make_subplots 
import os 
import json 
import warnings 
warnings.filterwarnings('ignore') 




# Database connection:
try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456789",
        database = "phonepe"

    ) 
    if connection.is_connected():
        print("mysql coonection is SUCESSFUL!!!") 
    cursor = connection.cursor()
    print("Cursor Activated")
except Error as e:
    print("While connecting mysql ERROR!!!") 
    #why we need to close the connection because,if you maintain the connection live ,there is a cyber security we maintaion the records securely 


# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# agg_transaction:

# initially we set sql_safe_updates = 0 why because by default its 1:
# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# agg_transaction:

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE agg_transaction 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE agg_transaction 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE agg_transaction 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = """UPDATE agg_transaction 
           SET States = REPLACE(States, '-', ' ')"""
cursor.execute(query)

# take the percentage two decimal point using ROUND() function:
query = """UPDATE agg_transaction 
           SET Transaction_amount = ROUND(Transaction_amount, 2)"""
cursor.execute(query)

# loading entire fron the table :
query = "SELECT * FROM agg_transaction"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
agg_transaction = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Transaction_type', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)


connection.commit() 
#agg_transaction   

# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# agg_user 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE agg_user 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE agg_user 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE agg_user 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = """UPDATE agg_user 
           SET States = REPLACE(States, '-', ' ')""" 
cursor.execute(query)

# take the percentage two decimal point using ROUND() function:
query = """UPDATE agg_user 
           SET Percentage = ROUND(Percentage,2)""" 
cursor.execute(query) 

# loading entire fron the table :
query = "SELECT * FROM agg_user"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
agg_user = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Brands', 'Transaction_count', 'Percentage']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)


connection.commit() 
#agg_user


# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# agg_insurance 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE agg_insurance 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE agg_insurance 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE agg_insurance 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = """UPDATE agg_insurance 
           SET States = REPLACE(States, '-', ' ')""" 
cursor.execute(query)

# take the percentage two decimal point using ROUND() function:
query = "UPDATE agg_insurance " \
"        SET Transaction_amount = ROUND(Transaction_amount,2)" 
cursor.execute(query) 

# loading entire fron the table :
query = "SELECT * FROM agg_insurance"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
agg_insurance = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Transaction_type', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)
connection.commit()
#agg_insurance 


# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# map_transaction:

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE map_transaction 
           SET States = 'Andaman & Nicobar Islands' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE map_transaction 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalize format:
query = """UPDATE map_transaction 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# convert all Districts names into capitalize format:
query = """UPDATE map_transaction 
           SET Districts = CONCAT(UPPER(SUBSTRING(Districts,1,1)),LOWER(SUBSTRING(Districts,2,LENGTH(Districts))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = "UPDATE map_transaction SET States = REPLACE(States, '-', ' ')" 
cursor.execute(query)

# take the Transaction_amount two decimal point using ROUND() function:
query = """UPDATE map_transaction 
           SET Transaction_amount = ROUND(Transaction_amount, 2)"""
cursor.execute(query)

# loading entire fron the table :
query = "SELECT * FROM map_transaction"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
map_transaction = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Districts', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)
connection.commit() 
#map_transaction


# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# map_user 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE map_user 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE map_user 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE map_user 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# convert all Districts names into capitalize format:
query = """UPDATE map_user 
           SET Districts = CONCAT(UPPER(SUBSTRING(Districts,1,1)),LOWER(SUBSTRING(Districts,2,LENGTH(Districts))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = "UPDATE map_user SET States = REPLACE(States, '-', ' ')" 
cursor.execute(query)


# loading entire fron the table :
query = "SELECT * FROM map_user"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
map_user = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Districts', 'Register_users', 'App_opens_users']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)


connection.commit() 
#map_user



# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# map_insurance 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE map_insurance 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE map_insurance 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE map_insurance 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# convert all Districts names into capitalize format:
query = """UPDATE map_insurance 
           SET Districts = CONCAT(UPPER(SUBSTRING(Districts,1,1)),LOWER(SUBSTRING(Districts,2,LENGTH(Districts))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = "UPDATE map_insurance SET States = REPLACE(States, '-', ' ')" 
cursor.execute(query)

# Transaction amount converted to 2 decimal places:
query = """UPDATE map_insurance 
           SET Transaction_amount = ROUND(Transaction_amount, 2)"""
cursor.execute(query) 


# loading entire fron the table :
query = "SELECT * FROM map_insurance"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
map_insurance = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Districts', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)
connection.commit() 
#map_insurance

# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# top_transaction 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE top_transaction 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE top_transaction 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE top_transaction 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = "UPDATE top_transaction SET States = REPLACE(States, '-', ' ')" 
cursor.execute(query) 

# take the Transaction_amount two decimal point using ROUND() function:
query = """UPDATE top_transaction 
           SET Transaction_amount = ROUND(Transaction_amount,2)""" 
cursor.execute(query) 

# take the Pincodes without decimal point using ROUND() function:
query = """UPDATE top_transaction 
           SET Pincodes = FLOOR(Pincodes)""" 
cursor.execute(query)

# loading entire fron the table :
query = "SELECT * FROM top_transaction"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
top_transaction = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Pincodes', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)


connection.commit() 
#top_transaction



# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# top_user 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE top_user 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE top_user 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE top_user 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = """UPDATE top_user 
           SET States = REPLACE(States, '-', ' ')""" 
cursor.execute(query) 

# loading entire fron the table :
query = "SELECT * FROM top_user"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
top_user = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Pincodes', 'Register_user']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)
connection.commit() 
#top_user


# modifying the columns and update the values as per our requirements and loading a data from the database again creating dataframe:
# top_insurance 

# initially we set sql_safe_updates = 0 why because by default its 1:
query = "SET SQL_SAFE_UPDATES = 0"
cursor.execute(query)

# update states names :
query = """UPDATE top_insurance 
           SET States = 'Andaman & Nicobar' 
           WHERE States = 'andaman-&-nicobar-islands'"""
cursor.execute(query)

query = """UPDATE top_insurance 
           SET States ='Dadar Nagar Haveli' 
           WHERE States = 'dadra-&-nagar-haveli-&-daman-&-diu'"""
cursor.execute(query) 

# convert all states names into capitalizr format:
query = """UPDATE top_insurance 
           SET States = CONCAT(UPPER(SUBSTRING(States,1,1)),LOWER(SUBSTRING(States,2,LENGTH(States))))"""
cursor.execute(query) 

# Removing '-' FROM the states column:
query = """UPDATE top_insurance 
           SET States = REPLACE(States, '-', ' ')""" 
cursor.execute(query) 

# loading entire fron the table :
query = "SELECT * FROM top_insurance"
cursor.execute(query)
table = cursor.fetchall()

# CREATING dataframe:
top_insurance = pd.DataFrame(table, columns = ['States', 'Years', 'Quaters', 'Districts', 'Transaction_count', 'Transaction_amount']) 

# again we set sql_safe_updats is 0:
query = "SET SQL_SAFE_UPDATES = 1"
cursor.execute(query)
connection.commit() 
#top_insurance





st.set_page_config(layout="wide")

# Create two columns, right one smaller for the logo
col1, col2 = st.columns([8, 2])

with col2:
    # Set width in pixels to increase size (e.g., 200px)
    st.image("C:/Users/Dhatch/Desktop/phonepe logo.png", width=200)

with col1:
    
    st.markdown("""
        <style>
        [data-testid=stAppViewContainer] {
        background-color: #CFC8DD
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("PHONEPE DATA EXTRACTION AND DATA VISUALIZATION") 
    st.markdown(
        '<p style="font-size:30px; color:red;">Phonepe is a Easy TransactionApp, You can transfer any Bank to any Bank Securly !</p>',
        unsafe_allow_html=True
    ) 


# creating sidebar:
with st.sidebar:

    st.markdown("""
        <style>
        [data-testid=stSidebar] {
        background-color: #8265BD
        }
        </style>
        """, unsafe_allow_html=True)

    st.header("Main Menu")
    
    # Add widgets and other elements within this block
    option = st.radio(
        "PAGES",["Home", "All_Datas", "Data_Visualization", "TOP_charts"]
    ) 

if option == 'Home':
    main_col, side_col = st.columns([3, 1])

    with main_col:
    
    
        query = "SELECT States,SUM(Register_users) AS Register_users FROM top_user GROUP BY States ORDER BY Register_users"
        cursor.execute(query) 
        table = cursor.fetchall()
        df = pd.DataFrame(table,columns = ['States', 'Register_users']) 
        df['States'] = df['States'].str.strip().str.title()
        df['Register_users'] = pd.to_numeric(df['Register_users'])

        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Register_users',
            color_continuous_scale='Reds',
            height=500, width=500
        )

        fig.update_geos(fitbounds="locations", visible=False)
    
        fig.update_layout(plot_bgcolor="#CFC8DD", title_text='Register Users Across States')
        st.plotly_chart(fig,use_container_width=True) 


        #SIDE BUTTONS HOME PAGE:

    with side_col:
        # Wrap the button in a container with the custom class 

        st.sidebar.header("Filters")
        year = st.sidebar.selectbox("Select Year", [2020, 2021, 2022, 2023, 2024])
        quarter = st.sidebar.selectbox("Select Quarter", ["1", "2", "3", "4"])
        st.markdown('<div class="right-button">', unsafe_allow_html=True)
       
        option = st.radio(
            "PAGES",["Pincodes", "States", "Districts"], horizontal=True) 
        def year_quater(year):
            year = year
            if option == 'Pincodes':
                #st.write("Button clicked!")
                    query = f"""SELECT Pincodes,SUM(Register_users) AS Register_users 
                                FROM top_user 
                                WHERE Years = %s  AND Quaters = %s 
                                GROUP BY Pincodes 
                                ORDER BY Register_users DESC LIMIT 10"""
                    cursor.execute(query,year) 
                    table = cursor.fetchall() 
                    df = pd.DataFrame(table, columns = ['Pincodes','Register_users']) 
                    st.write(df) 
                
            elif option == 'States':
                query = f"""SELECT States,SUM(Register_users) AS Register_users 
                            FROM top_user 
                            WHERE Years = %s AND Quaters = %s 
                            GROUP BY States 
                            ORDER BY Register_users DESC LIMIT 10"""
                cursor.execute(query,year) 
                table = cursor.fetchall() 
                df = pd.DataFrame(table, columns = ['States','Register_users']) 
                df['States'] = df['States'].str.strip().str.title()
                st.write(df) 
            elif option == 'Districts':
                query = f"""SELECT Districts,SUM(Transaction_count) AS Transaction_count 
                            FROM map_insurance 
                            WHERE Years = %s AND Quaters = %s 
                            GROUP BY Districts 
                            ORDER BY Transaction_count DESC LIMIT 10"""
                cursor.execute(query,year) 
                table = cursor.fetchall() 
                df = pd.DataFrame(table, columns = ['Districts','Transaction_count'])
                #df["Transaction_count"] = df["Transaction_count"].astype('int64')
                st.write(df)
            
                st.markdown('</div>', unsafe_allow_html=True) 
        year_quater([year,1])

    





elif option == 'All_Datas': 
   
    
    # Define the options for the select box
    options = ["Agg_transaction", "Agg_user", "Agg_insurance", "Map_transaction", "Map_user", "Map_insurance", "Top_transaction", "Top_user", "Top_insurance"] 
    d = {
        'Agg_transaction': agg_transaction, 'Agg_user' : agg_user, 'Agg_insurance' : agg_insurance,
         'Map_transaction' : map_transaction, 'Map_user' : map_user, 'Map_insurance' : map_insurance,
         'Top_transaction': top_transaction, 'Top_user' : top_user, 'Top_insurance' : top_insurance 
         }
    # Create the select box
    selected_option = st.selectbox("DATAFRAMES :", options,) 
    
                      

    # Use the selected option in your app 
    st.markdown("""
## Selected dataframe is :




""")
    #st.write("Selected dataframe is :")

    st.write(d[selected_option])
    #st.write(selected_option)

elif option == 'Data_Visualization': 
    st.markdown(
        '<p style="font-size:30px; color:red;">Decoding Transaction Dynamics </p>',
        unsafe_allow_html=True
    )
    #st.write("Decoding Transaction Dynamics :") 
    col21, col22 = st.columns([1,1])
        # second pie plot:
    with col21:
        def years1(year):
            year = year
            #Agg_tansaction_type: 
            query = f"""SELECT Years,Transaction_type, SUM(Transaction_amount) AS Transaction_amount 
                        FROM agg_transaction 
                        WHERE Years = %s 
                        GROUP BY Transaction_type 
                        ORDER BY Transaction_amount""" 
            cursor.execute(query,year)
            table = cursor.fetchall()
            df = pd.DataFrame(table, columns = ['Years','Transaction_type', 'Transaction_amount'])
            fig = px.pie(df, values = 'Transaction_amount', names = 'Transaction_type', title= "Transaction_types vs Transaction_amount")
            fig.update_layout(uniformtext_minsize = 12, uniformtext_mode = 'hide') 
            st.plotly_chart(fig, use_container_width=True) 

        year_list11 = agg_transaction['Years'].unique()
        option2 = st.selectbox("Years",year_list11)
        years1([option2])
            
    with col22:
            
        def years2(year):
            data = year
            query = f"""SELECT Years,Transaction_type, SUM(Transaction_count) AS Transaction_count 
                        FROM agg_transaction 
                        WHERE Years = %s 
                        GROUP BY Transaction_type 
                        ORDER BY Transaction_count""" 
            cursor.execute(query,data)
            table = cursor.fetchall()
            df = pd.DataFrame(table, columns = ['Years','Transaction_type', 'Transaction_count'])
            fig = px.pie(df, values = 'Transaction_count', names = 'Transaction_type', title= "Transaction_types vs Transaction_count")
            fig.update_layout(uniformtext_minsize = 12, uniformtext_mode = 'hide') 
            st.plotly_chart(fig, use_container_width=True) 

        year_list21 = agg_transaction['Years'].unique()
        option3 = st.selectbox("Years1",year_list21)
        years2([option3])


    def states(state):
        state = state
        query = f"""SELECT Years, SUM(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount 
                    FROM agg_transaction 
                    WHERE States = %s 
                    GROUP BY Years 
                    ORDER BY Years""" 
        cursor.execute(query, state)
        table1 = cursor.fetchall() 
        df1 = pd.DataFrame(table1, columns = ['Years', 'Transaction_count', 'Transaction_amount'])
        fig1 = px.line(df1, x = 'Years', y = 'Transaction_count',markers=True) 
        fig2 = px.line(df1, x = 'Years', y = 'Transaction_amount',markers=True) 
        col11,col21 = st.columns([1,1])
        with col11: 
             fig1 = px.line(df1, x = 'Years', y = 'Transaction_count') 
             fig1.update_traces(mode='lines+markers')
             st.plotly_chart(fig1, use_container_width=True) 

        with col21: 
             fig2 = px.line(df1, x = 'Years', y = 'Transaction_amount')
             fig2.update_traces(mode='lines+markers')
             st.plotly_chart(fig2, use_container_width=True)  
             
    states_list = agg_transaction['States'].unique()
    option1 = st.selectbox("states",states_list)
    states([option1])


    # Define the options for the select box
    options = ["Agg_transaction", "Agg_insurance", "Map_transaction", "Map_insurance", "Top_transaction", "Top_insurance"] 
    d_dataframes = {
        'Agg_transaction': agg_transaction, 'Agg_insurance' : agg_insurance,
         'Map_transaction' : map_transaction, 'Map_insurance' : map_insurance,
         'Top_transaction': top_transaction, 'Top_insurance' : top_insurance 
         } 
    # Create the select box
    selected_option = st.selectbox("Data_exploration for :", options) 
    
                      

    # Use the selected option in your app 
    st.markdown("""
## Selected data exploration is :
""")
    #st.write("Selected dataframe is :")
    #st.write(selected_option) 
    #st.write(d_dataframes[selected_option]) 

    def year_s(year,table_name):
        data = year
        query = f"""SELECT States,Years,SUM(Transaction_count) AS Transaction_count 
        FROM {table_name} 
        WHERE Years = %s GROUP BY States  
        ORDER BY Transaction_count""" 
        cursor.execute(query,data)
        table1 = cursor.fetchall()
        df1 = pd.DataFrame(table1, columns = ['States','Years', 'Transaction_count'])
        fig_bar1 = px.bar(df1, x = 'States', y = 'Transaction_count' ,
                          title = f" Transaction_count  For  States  Wise : {table_name} In Year of {data[0]} ")
       
                                                        
        
        query = f"""SELECT States,SUM(Transaction_amount) AS Transaction_amount 
                    FROM {table_name} 
                    WHERE Years = %s 
                    GROUP BY States 
                    ORDER BY Transaction_amount""" 
        cursor.execute(query,data)
        table2 = cursor.fetchall()
        df2 = pd.DataFrame(table2, columns = ['States', 'Transaction_amount'])
        fig_bar2 = px.bar(df2,x='States',y='Transaction_amount',
                          title = f" Transaction_amount  For  States  Wise : {table_name} In Year of {data[0]} ") 
        
         


        # second bar plot: 
        query = f"""SELECT States, SUM(Transaction_amount) AS Transaction_amount 
                    FROM {table_name} 
                    GROUP BY States 
                    ORDER BY Transaction_amount 
                    DESC LIMIT 10 """
        cursor.execute(query) 

        table4 = cursor.fetchall()
        df4 = pd.DataFrame(table4, columns = ['States', 'Transaction_amount']) 
        fig_bar4 = px.bar(df4,x='States',y='Transaction_amount',
                          title = "Years Wise Transaction_Amount",
                          color_discrete_sequence = px.colors.sequential.Aggrnyl)

    

        # states wise transaction_count:
        query = f"""SELECT States,SUM(Transaction_count) AS Transaction_count 
                    FROM {table_name} 
                    GROUP BY States 
                    ORDER BY Transaction_count""" 
        cursor.execute(query)


        table5 = cursor.fetchall()
        df5 = pd.DataFrame(table5, columns = ['States', 'Transaction_count'])
        fig_bar5 = px.bar(df5, x = 'States', y = 'Transaction_count', 
                          title = "States wise Transaction_Count",
                          color_discrete_sequence = px.colors.sequential.Blackbody )
        


        #  states lowest transaction_count:
        query = f"""SELECT States,SUM(Transaction_count) AS Transaction_count 
                    FROM {table_name} 
                    GROUP BY States 
                    ORDER BY Transaction_count LIMIT 15""" 
        cursor.execute(query)


        table6 = cursor.fetchall()
        df6 = pd.DataFrame(table6, columns = ['States', 'Transaction_count'])
        #df6

        fig_bar6 = px.bar(df6, x = 'States', y = 'Transaction_count', 
                          title = "TOP 15 States LOWEST Transaction_Count ", 
                          color_discrete_sequence = px.colors.sequential.Agsunset )
       

        # top 10 states highest transaction_count:

        query = f"""SELECT States,SUM(Transaction_count) AS Transaction_count 
                    FROM {table_name} 
                    GROUP BY States 
                    ORDER BY Transaction_count DESC LIMIT 10""" 
        cursor.execute(query)


        table7 = cursor.fetchall()
        df7 = pd.DataFrame(table7, columns = ['States', 'Transaction_count'])
          

        fig_bar7 = px.bar(df7, x = 'States', y = 'Transaction_count', 
                          title = "TOP 10 States wise Transaction_Count ", 
                          color_discrete_sequence = px.colors.sequential.Aggrnyl)
       
        fig_combined = make_subplots(rows = 2, cols = 3, subplot_titles =(f" Transaction_amount  For  States  Wise : {table_name} In Year of {data[0]}",
                                                                f" Transaction_count  For  States  Wise : {table_name} In Year of {data[0]}",
                                                                "Top 10 states Transaction_Amount","States wise Transaction_Count",
                                                                "TOP 15 States LOWEST Transaction_Count ","TOP 10 States wise Transaction_Count "))
        
        for trace in fig_bar1.data: 
            fig_combined.add_trace(trace, row = 1, col = 1) 
        for trace in fig_bar2.data:
            fig_combined.add_trace(trace, row = 1, col = 2) 
        for trace in fig_bar4.data:
            fig_combined.add_trace(trace, row = 1, col = 3) 
        for trace in fig_bar5.data:
            fig_combined.add_trace(trace, row = 2, col = 1) 
        for trace in fig_bar6.data:
            fig_combined.add_trace(trace, row = 2, col = 2) 
        for trace in fig_bar7.data:
            fig_combined.add_trace(trace, row = 2, col = 3) 


        fig_combined.update_layout(height = 1000) 
        st.plotly_chart(fig_combined, use_container_width=True)  




       
        

        #return df9 
    d = d_dataframes[str(selected_option)]    
    years = d['Years'].unique()
    option = st.radio('years_option',years, horizontal= True)
    year_s([option],str(selected_option))  


    st.markdown(
        '<p style="font-size:30px; color:red;">Device Dominance And User Engagement Analysis </p>',
        unsafe_allow_html=True
    ) 
    # device dominance and user engagement analysis:
    # Years and Quater Wise App_opens :
    query = """SELECT Years,Quaters,SUM(App_opens_users) AS App_opens_users 
               FROM map_user 
               GROUP BY Years,Quaters 
               ORDER BY Years,Quaters,App_opens_users"""
    cursor.execute(query) 
    table21 = cursor.fetchall()
    df21 = pd.DataFrame(table21, columns = ['Years','Quaters','App_opens_users'])
    fig_line = px.line(df21, x = 'Years', y = 'App_opens_users', color = 'Quaters', 
                       title = "Years and Quater Wise App_opens",width=10, height=10)
    
    # Apps_Not_opens districts  :

    query = """SELECT States,COUNT(States) AS App_notopens_count 
               FROM map_user 
               WHERE App_opens_users = 0 
               GROUP BY States"""
    cursor.execute(query)
    table22 = cursor.fetchall()
    df22 = pd.DataFrame(table22, columns = ['States','App_notopens_count'])
    fig_bar = px.bar(df22, x = 'States', y = 'App_notopens_count',title = "Apps_Not_opens districts") 

    # States Wise Register_Users And App_opens_count :
    query = """SELECT States,SUM(Register_users) AS Register_user,SUM(App_opens_users) AS App_opens_users 
               FROM map_user 
               GROUP BY States"""
    cursor.execute(query)
    table23 = cursor.fetchall()
    df23 = pd.DataFrame(table23, columns = ['States', 'Register_users', 'App_opens_users'])
    fig_scatter = px.scatter(df23, x = 'Register_users', y = 'App_opens_users', 
                             color = 'States', 
                             title = "States Wise Register_Users And App_opens_coun" ) 

    # Top 10 districts hightest register uesr: 

    query = """SELECT Districts,SUM(Register_users) AS Register_users 
               FROM map_user 
               GROUP BY Districts 
               ORDER BY Register_users DESC LIMIT 10"""

    cursor.execute(query) 
    table24 = cursor.fetchall()
    df24 = pd.DataFrame(table24, columns = ['Districts','Register_users'])
    fig_bar2 = px.bar(df24, x = 'Districts', y = 'Register_users', title = 'States wise Register_users' )
    
    # States wise Register_users
    query = """SELECT States,SUM(Register_users) AS Register_users 
               FROM map_user 
               GROUP BY States 
               ORDER BY Register_users""" 
    cursor.execute(query) 
    table25 = cursor.fetchall()
    df25 = pd.DataFrame(table25, columns = ['States','Register_users'])
    fig_bar3 = px.bar(df25, x = 'States', y = 'Register_users', title = 'States wise Register_users') 

    # Apps_opens districts :

    query = """SELECT States,COUNT(States) AS App_opens_count 
               FROM map_user 
               WHERE App_opens_users != 0 
               GROUP BY States"""
    cursor.execute(query)
    table26 = cursor.fetchall()
    df26 = pd.DataFrame(table26, columns = ['States','App_opens_count'])
    fig_bar4 = px.bar(df26, x = 'States', y = 'App_opens_count')
   
        
        
    

    fig_combined = make_subplots(rows = 2, cols = 3, subplot_titles =(" Years and Quater Wise App_opens ",
                                                                "Apps_Not_opens districts",
                                                                "States Wise Register_Users And App_opens_count",
                                                                "Top 10 districts hightest register uesr ",
                                                                "States wise Register_users",
                                                                "Apps_opens_districts"))
        
    for trace in fig_line.data: 
        fig_combined.add_trace(trace, row = 1, col = 1) 
    for trace in fig_bar.data:
            fig_combined.add_trace(trace, row = 1, col = 2) 
    for trace in fig_scatter.data:
            fig_combined.add_trace(trace, row = 1, col = 3) 
    for trace in fig_bar2.data:
            fig_combined.add_trace(trace, row = 2, col = 1) 
    for trace in fig_bar3.data:
            fig_combined.add_trace(trace, row = 2, col = 2) 
    for trace in fig_bar4.data:
            fig_combined.add_trace(trace, row = 2, col = 3) 


    fig_combined.update_layout(width = 1000,height = 1000) 
    st.plotly_chart(fig_combined, use_container_width=True)  


    st.markdown(
        '<p style="font-size:30px; color:red;">Insurance Transaction Analysis </p>',
        unsafe_allow_html=True
        )  
    
    def districts(districts):
        district = districts
        query = f"""SELECT Years, SUM(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount 
                    FROM map_insurance 
                    WHERE Districts = %s 
                    GROUP BY Years 
                    ORDER BY Years""" 
        cursor.execute(query, district)
        table1 = cursor.fetchall() 
        df1 = pd.DataFrame(table1, columns = ['Years', 'Transaction_count', 'Transaction_amount'])
        fig1 = px.line(df1, x = 'Years', y = 'Transaction_count',markers=True) 
        fig2 = px.line(df1, x = 'Years', y = 'Transaction_amount',markers=True) 
        col11,col21 = st.columns([1,1])
        with col11: 
             fig1 = px.line(df1, x = 'Years', y = 'Transaction_count') 
             fig1.update_traces(mode='lines+markers')
             st.plotly_chart(fig1, use_container_width=True) 

        with col21: 
             fig2 = px.line(df1, x = 'Years', y = 'Transaction_amount')
             fig2.update_traces(mode='lines+markers')
             st.plotly_chart(fig2, use_container_width=True)  
             
    districts_list = map_insurance['Districts'].unique()
    option1 = st.selectbox("Districts_wise",districts_list)
    districts([option1])

    # Transaction_count Across States
    query = """SELECT States, COUNT(Transaction_count) AS Transaction_count 
               FROM map_insurance 
               GROUP BY States 
               ORDER BY Transaction_count DESC LIMIT 10""" 
    cursor.execute(query)
    table1 = cursor.fetchall()
    df1 = pd.DataFrame(table1, columns = ['States', 'Total_Transaction_count']) 
    fig1 = px.bar(df1, x = 'States', y = 'Total_Transaction_count', 
                  title = " Transaction_count Across States", 
                  color_discrete_sequence = px.colors.sequential.Agsunset)
   

    # Transaction_count Across Districts:
    query = """SELECT Districts, COUNT(Transaction_count) AS Transaction_count 
               FROM map_insurance 
               GROUP BY Districts 
               ORDER BY Transaction_count DESC LIMIT 10""" 
    cursor.execute(query)
    table2 = cursor.fetchall()
    df2 = pd.DataFrame(table2, columns = ['Districts', 'Total_Transaction_count']) 
    fig2 = px.bar(df2, x = 'Districts', y = 'Total_Transaction_count', 
                  title = " Transaction_count Across Districts", 
                  color_discrete_sequence = px.colors.sequential.Aggrnyl)
    
    
    # Transaction_count Across Pincodes:
    query = """SELECT States,Pincodes, COUNT(Transaction_count) AS Transaction_count 
               FROM top_insurance 
               GROUP BY States,Pincodes 
               ORDER BY Transaction_count DESC LIMIT 10""" 
    cursor.execute(query)
    table3 = cursor.fetchall()
    df3 = pd.DataFrame(table3, columns = ['States','Pincodes', 'Total_Transaction_count']) 
    df3['Pincodes'] = df3['Pincodes'].astype('string')
    fig3 = px.bar(df3, x = 'States', y = 'Total_Transaction_count',
                  color = 'Total_Transaction_count', 
                  title = " Transaction_count Across Pincodes",
                  hover_name = 'Pincodes',
                  color_discrete_sequence = px.colors.sequential.Blackbody_r)
    
    #stacked bar plot year and quater combinations
    query = """SELECT Years,Quaters,SUM(Transaction_amount) AS Transaction_amount 
               FROM agg_insurance 
               GROUP BY Years, Quaters 
               ORDER BY Transaction_amount LIMIT 10"""
    cursor.execute(query) 
    table4 = cursor.fetchall()
    df4 = pd.DataFrame(table4, columns = ['Years','Quaters','Transaction_amount'])
    fig4 = px.bar(df4, x = 'Years', y = 'Transaction_amount', color = 'Quaters' , 
                  title ="stacked bar plot year and quater combinations")



    fig_combined = make_subplots(rows = 1, cols = 2, subplot_titles = (" Transaction_count Across States ",
                                                                "stacked bar plot year and quater combinations"
                                                                ))
        
    for trace in fig1.data: 
        fig_combined.add_trace(trace, row = 1, col = 1) 
    for trace in fig4.data:
            fig_combined.add_trace(trace, row = 1, col = 2) 
    
    
    fig_combined.update_layout(width = 500,height = 500) 
    st.plotly_chart(fig_combined, use_container_width=True) 

    col51, col52 = st.columns([1,1]) 
    with col51: 
        # Transaction_count Across Districts:
        query = """SELECT Districts, COUNT(Transaction_count) AS Transaction_count 
                   FROM map_insurance 
                   GROUP BY Districts 
                   ORDER BY Transaction_count DESC LIMIT 10""" 
        
        cursor.execute(query)
        table2 = cursor.fetchall()
        df2 = pd.DataFrame(table2, columns = ['Districts', 'Total_Transaction_count']) 
        fig2 = px.bar(df2, x = 'Districts', y = 'Total_Transaction_count', 
                      title = " Transaction_count Across Districts", 
                      color_discrete_sequence = px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig2, use_container_width=True) 

    with col52: 
        # Transaction_count Across Pincodes:
        query = """SELECT States,Pincodes, COUNT(Transaction_count) AS Transaction_count 
        FROM top_insurance 
        GROUP BY States,Pincodes 
        ORDER BY Transaction_count DESC LIMIT 10""" 

        cursor.execute(query)
        table3 = cursor.fetchall()
        df3 = pd.DataFrame(table3, columns = ['States','Pincodes', 'Total_Transaction_count']) 
        df3['Pincodes'] = df3['Pincodes'].astype('string')
        fig3 = px.bar(df3, x = 'States', y = 'Total_Transaction_count',color = 'Total_Transaction_count', title = " Transaction_count Across Pincodes",hover_name = 'Pincodes', color_discrete_sequence = px.colors.sequential.Blackbody_r)
        st.plotly_chart(fig3, use_container_width=True)        


    st.markdown(
        '<p style="font-size:30px; color:red;">' \
        'Quarters And Year Wise Tansaction_Amount Transaction_Count '
        '</p>',
        unsafe_allow_html=True 
    ) 

    # Most insurance Transaction combinations specific Quater and Years:
    def year_quaters(quater):
        data1 = quater
        query = f"""SELECT Years, Quaters, SUM(Transaction_count) AS Transaction_count,SUM(Transaction_amount) AS Transaction_amount  
                    FROM agg_insurance 
                    WHERE Quaters = %s 
                    GROUP BY Years 
                    ORDER BY Years,Transaction_count,Transaction_amount """ 
        cursor.execute(query,data1)
        table5 = cursor.fetchall()
        df5 = pd.DataFrame(table5, columns = ['Years', 'Quaters', 'Total_Transaction_count','Total_Transaction_amount']) 
        col41,col42 = st.columns([1,1])
        with col41:

            fig5 = px.line(df5, x = 'Years', y = 'Total_Transaction_amount',
                        title = " Transaction_amount Across specific Quater and Years", 
                        hover_name = 'Quaters',color = 'Quaters',
                        color_discrete_sequence = px.colors.sequential.Rainbow)
            
            fig5.update_traces(mode='lines+markers')
            st.plotly_chart(fig5, use_container_width=True) 

        with col42:
            fig6 = px.line(df5, x = 'Years', y = 'Total_Transaction_count',
                        title = "Transaction_count Across specific Quater and Years", hover_name = 'Quaters',color = 'Quaters',
                        color_discrete_sequence = px.colors.sequential.Magenta)
            fig6.update_traces(mode='lines+markers')
            st.plotly_chart(fig6, use_container_width=True) 
             

    
    agg_insurance_Quater = agg_insurance['Quaters'].unique()
    quarter = st.selectbox("SELECT_Quater", agg_insurance_Quater)
    year_quaters([quarter])

    st.markdown(
        '<p style="font-size:30px; color:red;">User Registration Analysis </p>',
        unsafe_allow_html=True 
    )  

    # Top Registration_users Across States
    query = """SELECT States, COUNT(Register_users) AS Register_users 
               FROM map_user 
               GROUP BY States 
               ORDER BY Register_users DESC LIMIT 10""" 
    
    cursor.execute(query)
    table1 = cursor.fetchall()
    df1 = pd.DataFrame(table1, columns = ['States', 'Total_Register_users']) 
    fig1 = px.bar(df1, x = 'States', y = 'Total_Register_users', title = " Top Registration_users Across States", 
                  color_discrete_sequence = px.colors.sequential.Agsunset) 
    
    # Register_users Across Districts:
    query = """SELECT Districts, SUM(Register_users) AS Register_users 
               FROM map_user 
               GROUP BY Districts 
               ORDER BY Register_users DESC LIMIT 10""" 
    cursor.execute(query)
    table2 = cursor.fetchall()
    df2 = pd.DataFrame(table2, columns = ['Districts', 'Registeration_users']) 
    fig2 = px.bar(df2, x = 'Districts', y = 'Registeration_users', 
                  title = " Register_users Across Districts", 
                  color_discrete_sequence = px.colors.sequential.Aggrnyl)
    
    
    # Transaction_count Across Pincodes:
    query = """SELECT States,Pincodes, COUNT(Register_users) AS Register_users 
               FROM top_user 
               GROUP BY States,Pincodes 
               ORDER BY Register_users DESC LIMIT 10""" 
    cursor.execute(query)
    table3 = cursor.fetchall()
    df3 = pd.DataFrame(table3, columns = ['States','Pincodes', 'Total_Register_users']) 
    fig3 = px.histogram(df3, x = 'States', y = 'Total_Register_users',color = 'Pincodes',  
                        title = " Top 10 Pincodes", 
                        color_discrete_sequence = px.colors.sequential.Magenta, hover_name = 'Pincodes')
    
    

    query = """SELECT Years, Quaters, COUNT(Register_users) AS Register_users 
               FROM map_user WHERE Quaters = 1 
               GROUP BY Years 
               ORDER BY Years,Register_users DESC LIMIT 10"""
     
    cursor.execute(query)
    table5 = cursor.fetchall()
    df5 = pd.DataFrame(table5, columns = ['Years', 'Quaters', 'Total_Register_users']) 
    fig5 = px.bar(df5, x = 'Years', y = 'Total_Register_users', color = 'Quaters', 
                  title = " Transaction_count Across specific Quater and Years", 
                  color_discrete_sequence = px.colors.sequential.Rainbow)
    

    fig_combined = make_subplots(rows = 2, cols = 2, subplot_titles =(" Top Registration_users Across States ",
                                                                "Register_users Across Districts",
                                                                "Top 10 Pincodes",
                                                                "Transaction_count Across specific Quater and Years ",
                                                                
                                                                ))
        
    for trace in fig1.data: 
        fig_combined.add_trace(trace, row = 1, col = 1) 
    for trace in fig2.data:
            fig_combined.add_trace(trace, row = 1, col = 2) 
    for trace in fig3.data:
            fig_combined.add_trace(trace, row = 2, col = 1) 
    for trace in fig5.data:
            fig_combined.add_trace(trace, row = 2, col = 2) 

 
    fig_combined.update_layout(width = 2000,height = 800) 
    st.plotly_chart(fig_combined, use_container_width=True) 
    
    st.markdown(
        '<p style="font-size:30px; color:red;">Transaction Analysis Across States and Districts </p>',
        unsafe_allow_html=True
    ) 

    # Top Districts value and volume: 
    query = """SELECT Districts,COUNT(Transaction_count) AS Transaction_count,SUM(Transaction_amount) AS Transaction_amount 
               FROM map_transaction 
               GROUP BY Districts 
               ORDER BY Transaction_count,Transaction_amount DESC LIMIT 10"""
    cursor.execute(query)
    table1 = cursor.fetchall()
    df1 = pd.DataFrame(table1, columns = ['Districts', 'Transaction_count', 'Transaction_amount'])
    fig1 = px.scatter(df1, x = 'Transaction_amount' , y = 'Transaction_count', color = 'Districts')


    # Top States value and volume: 
    query = """SELECT States,COUNT(Transaction_count) AS Transaction_count,SUM(Transaction_amount) AS Transaction_amount 
               FROM map_transaction 
               GROUP BY States 
               ORDER BY Transaction_count,Transaction_amount DESC LIMIT 10"""
    cursor.execute(query)
    table2 = cursor.fetchall()
    df2 = pd.DataFrame(table2, columns = ['States', 'Transaction_count', 'Transaction_amount'])
    fig2 = px.scatter(df2, x = 'Transaction_amount' , y = 'Transaction_count', color = 'States')
     

    # Top Pincodes Transaction value and volume: 
    query = """SELECT Pincodes,COUNT(Transaction_count) AS Transaction_count,SUM(Transaction_amount) AS Transaction_amount 
               FROM top_transaction 
               GROUP BY Pincodes 
               ORDER BY Transaction_count,Transaction_amount,Pincodes DESC LIMIT 10"""
    cursor.execute(query)
    table3 = cursor.fetchall()
    df3 = pd.DataFrame(table3, columns = ['Pincodes', 'Transaction_count', 'Transaction_amount'])
    fig3 = px.scatter(df3, x = 'Transaction_amount' , y = 'Transaction_count', hover_name='Pincodes',title = " Top Pincodes Transaction value and volume")

    # specific year TRansaction_count and transaction amount:
    query = """SELECT Years,Quaters, COUNT(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount FROM 
               map_transaction WHERE Years = 2021 
               GROUP BY Quaters 
               ORDER BY Quaters,Transaction_count,Transaction_amount DESC LIMIT 10"""
    cursor.execute(query)
    table4 = cursor.fetchall()
    df4 = pd.DataFrame(table4, columns = ['Years',"Quaters", 'Transaction_count', 'Transaction_amount'])
    fig4 = px.bar(df4,x = 'Quaters', y = 'Transaction_count', color = 'Transaction_count',title = 'Transaction_Count of year of 2020',hover_name='Years',color_discrete_sequence = px.colors.sequential.Aggrnyl)
    

    # specific year TRansaction_count and transaction amount:
    query = """SELECT Years,Quaters, COUNT(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount 
               FROM map_transaction 
               WHERE Years = 2021 GROUP BY Quaters 
               ORDER BY Quaters,Transaction_count,Transaction_amount DESC LIMIT 10"""
    cursor.execute(query)
    table5 = cursor.fetchall()
    df5 = pd.DataFrame(table5, columns = ['Years',"Quaters", 'Transaction_count', 'Transaction_amount'])
    fig5 = px.bar(df5,x = 'Years', y = 'Transaction_amount',title = 'Transaction_amount of year of 2020', hover_name='Quaters',color = 'Transaction_amount') 

    fig_combined = make_subplots(rows = 2, cols = 2, subplot_titles =(" Top States Transaction value and volume ",
                                                                " Top Districts Transaction value and volume ",
                                                                "Top Pincodes Transaction value and volume"))
                                                                
                                                                
    for trace in fig1.data: 
        fig_combined.add_trace(trace, row = 1, col = 1) 
    for trace in fig2.data:
            fig_combined.add_trace(trace, row = 1, col = 2) 
    for trace in fig3.data:
            fig_combined.add_trace(trace, row = 2, col = 1) 
    


 
    fig_combined.update_layout(width = 1000,height = 500) 
    st.plotly_chart(fig_combined, use_container_width=True) 

    col31,col32 = st.columns([1,1])
    with col31: 
         # specific year TRansaction_count and transaction amount:
        def yearmap(year):
            year31 = year
            query = f"""SELECT Years,Quaters, COUNT(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount 
                        FROM map_transaction 
                        WHERE Years = %s GROUP BY Quaters 
                        ORDER BY Quaters,Transaction_count,Transaction_amount DESC LIMIT 10"""
            cursor.execute(query,year31)
            table4 = cursor.fetchall()
            df4 = pd.DataFrame(table4, columns = ['Years',"Quaters", 'Transaction_count', 'Transaction_amount'])
            fig4 = px.bar(df4,x = 'Quaters', y = 'Transaction_count', color = 'Transaction_count',title = 'Transaction_Count of year of 2020',hover_name='Years',color_discrete_sequence = px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig4, use_container_width=True) 
        year_list31 = map_transaction['Years'].unique()
        option31 = st.selectbox("Years_map1",year_list31)
        yearmap([option31])
            

    with col32: 
        def yearmap(year):
            year32 = year
            query = f"""SELECT Years,Quaters, COUNT(Transaction_count) AS Transaction_count, SUM(Transaction_amount) AS Transaction_amount 
                        FROM map_transaction 
                        WHERE Years = %s 
                        GROUP BY Quaters 
                        ORDER BY Quaters,Transaction_count,Transaction_amount DESC LIMIT 10"""
            cursor.execute(query,year32)
            table5 = cursor.fetchall()
            df5 = pd.DataFrame(table5, columns = ['Years',"Quaters", 'Transaction_count', 'Transaction_amount'])
            fig5 = px.bar(df5,x = 'Years', y = 'Transaction_amount',title = 'Map_transaction Transaction_amount of year of 2020', hover_name='Quaters',color = 'Transaction_amount') 
            st.plotly_chart(fig5, use_container_width=True) 
        year_list33 = map_transaction['Years'].unique()
        option32 = st.selectbox("Years_map",year_list33)
        yearmap([option32])
            
    

    
elif option == 'TOP_charts':
    st.set_page_config(layout ='wide')
    st.title("TOP CHARTS") 

    options = [ "Agg_insurance", "Map_insurance", "Top_insurance"] 
     
    # Create the select box
    selected_option = st.selectbox("Insurance Analysis Of :", options)

    def year_quater_combinations(year,table_name):
        data = year
        query = f"""SELECT States,Quaters,SUM(Transaction_amount) AS Transaction_amount 
                    FROM {table_name} 
                    WHERE Years = %s 
                    GROUP BY States,Quaters 
                    HAVING Quaters = %s 
                    ORDER BY  Transaction_amount DESC LIMIT 10"""
        cursor.execute(query,data)
        table = cursor.fetchall()
        df1= pd.DataFrame(table, columns = ['States','Quaters','Transaction_amount'])
        fig1 = px.bar(df1, x = 'States', y = 'Transaction_amount',color = "Transaction_amount", hover_name = 'Quaters' ,title =f"year and quater combinations for top 10 states : {table_name}")
        st.plotly_chart(fig1, use_container_width=True)

    

        # top 10 pincodes tranaction_ampunt: 
        year = [year[0]]
        query = f"""SELECT Quaters,Pincodes,SUM(Transaction_amount) AS Transaction_amount 
                    FROM top_insurance 
                    WHERE Years = %s 
                    GROUP BY Quaters,Pincodes 
                    ORDER BY Transaction_amount,Quaters DESC LIMIT 10"""
        cursor.execute(query,year)
        table = cursor.fetchall()
        df2 = pd.DataFrame(table, columns = ['Quaters','Pincodes', 'Transaction_amount']) 
        df2['Pincodes'] = df2['Pincodes'].astype('string')
        fig2 = px.bar(df2, x = 'Quaters', y = 'Transaction_amount', title = f"Top 10 pincodes {year}",hover_name = 'Pincodes')
        #st.plotly_chart(fig2, use_container_width=True)
  

        query = f"""SELECT States,SUM(Register_users) AS Register_users 
                    FROM top_user 
                    WHERE Years = %s AND Quaters = %s 
                    GROUP BY States 
                    ORDER BY Register_users DESC LIMIT 10"""
        cursor.execute(query,data) 
        table = cursor.fetchall() 
        df3 = pd.DataFrame(table, columns = ['States','Register_users']) 
        df3['States'] = df3['States'].str.strip().str.title()
        fig3 = px.bar(df3, x = 'States', y = "Register_users", title="Top 10 States")
        #st.plotly_chart(fig3, use_container_width=True)
  

        query = f"""SELECT Pincodes,SUM(Register_users) AS Register_users 
                    FROM top_user 
                    WHERE Years = %s  AND Quaters = %s 
                    GROUP BY Pincodes 
                    ORDER BY Register_users DESC LIMIT 10"""

        cursor.execute(query,data) 
        table = cursor.fetchall() 
        df4 = pd.DataFrame(table, columns = ['Pincodes','Register_users']) 
        fig4 = px.bar(df4, x = 'Register_users', hover_name = "Pincodes", title="Top 10 Pincodes",color = "Pincodes")
        #st.plotly_chart(fig4, use_container_width=True)
  

        query = f"""SELECT Districts,SUM(Transaction_count) AS Transaction_count 
                    FROM map_insurance 
                    WHERE Years = %s AND Quaters = %s 
                    GROUP BY Districts 
                    ORDER BY Transaction_count DESC LIMIT 10"""

        cursor.execute(query,data) 
        table = cursor.fetchall() 
        df5 = pd.DataFrame(table, columns = ['Districts','Transaction_count'])
        #df["Transaction_count"] = df5["Transaction_count"].astype('int64')
        fig5 = px.bar(df5, x = 'Districts', y = "Transaction_count", title="Top 10 Districts") 
        #st.plotly_chart(fig5, use_container_width=True) 

        fig_combined = make_subplots(rows = 2, cols = 2, subplot_titles =(" Top pincodes across Quaters ",
                                                                    "Top 10 States",
                                                                    "Top 10 Pincodes",
                                                                    "Top 10 Districts ",
                                                                    
                                                                    ))
            
        for trace in fig2.data: 
            fig_combined.add_trace(trace, row = 1, col = 1) 
        for trace in fig3.data:
                fig_combined.add_trace(trace, row = 1, col = 2) 
        for trace in fig4.data:
                fig_combined.add_trace(trace, row = 2, col = 1) 
        for trace in fig5.data:
                fig_combined.add_trace(trace, row = 2, col = 2) 

    
        fig_combined.update_layout(width = 1000,height = 600) 
        st.plotly_chart(fig_combined, use_container_width=True) 


        col1, col2 = st.columns([1, 1])
        with col1:

        #Agg_tansaction_type:
            query = """SELECT Transaction_type, SUM(Transaction_amount) AS Transaction_amount 
                       FROM agg_transaction 
                       GROUP BY Transaction_type 
                       ORDER BY Transaction_amount"""

            cursor.execute(query)
            table6 = cursor.fetchall()
            df6 = pd.DataFrame(table6, columns = ['Transaction_type', 'Transaction_amount'])
            fig6 = px.pie(df6, values = 'Transaction_amount', names = 'Transaction_type', title= "Transaction_types vs Transaction_amount")
            fig6.update_layout(uniformtext_minsize = 12, uniformtext_mode = 'hide') 
            st.plotly_chart(fig6, use_container_width=True) 

        with col2:
        #Agg_tansaction_type:
            query = """SELECT Transaction_type, SUM(Transaction_count) AS Transaction_count 
                       FROM agg_transaction 
                       GROUP BY Transaction_type 
                       ORDER BY Transaction_count""" 
            cursor.execute(query)
            table7 = cursor.fetchall()
            df7 = pd.DataFrame(table7, columns = ['Transaction_type', 'Transaction_count'])
            fig7 = px.pie(df7, values = 'Transaction_count', names = 'Transaction_type', title= "Transaction_types vs Transaction_count")
            fig7.update_layout(uniformtext_minsize = 12, uniformtext_mode = 'hide') 
            st.plotly_chart(fig7, use_container_width=True) 
    

    years_list = top_insurance['Years'].unique()
    quaters_list = top_insurance['Quaters'].unique()
    option1 = st.selectbox('years_option',years_list)
    option2 = st.selectbox('Quaters',quaters_list)

    year_quater_combinations([option1,option2],str(selected_option)) 

    
    

 
                                                                                                                                                                                                                                                                                                                                                