import os
import json
import pandas as pd
import psycopg2
import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go

#aggre_transaction


path1="C:/Users/ELCOT/New folder/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_tran_list= os.listdir(path1)

columns1={"States":[], "Years":[], "Quarter":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}

for state in agg_tran_list:
    current_states=path1+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            A=json.load(Data)

            for i in A["data"]["transactionData"]:
                    name=i["name"]
                    trans_count=i["paymentInstruments"][0]["count"]
                    amount=i["paymentInstruments"][0]["amount"]
                    columns1["Transaction_type"].append(name)
                    columns1["Transaction_count"].append(trans_count)
                    columns1["Transaction_amount"].append(amount)
                    columns1["States"].append(state)
                    columns1["Years"].append(year)
                    columns1["Quarter"].append(int(file.strip(".json")))

aggre_transaction=pd.DataFrame(columns1)

#aggre_user
path2="C:/Users/ELCOT/New folder/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_list= os.listdir(path2)

columns2={"States":[], "Years":[], "Quarter":[], "Brands":[], "Transaction_count":[], "Percentage":[]}

for state in agg_user_list:
    current_states=path2+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            B=json.load(Data)

            try:
                for i in B["data"]["usersByDevice"]:
                    brand=i["brand"]
                    trans_count=i["count"]
                    percentage=i["percentage"]
                    columns2["Brands"].append(brand)
                    columns2["Transaction_count"].append(trans_count)
                    columns2["Percentage"].append(percentage)
                    columns2["States"].append(state)
                    columns2["Years"].append(year)
                    columns2["Quarter"].append(int(file.strip(".json")))

            except:
                pass        
            
aggre_user=pd.DataFrame(columns2)

#map transaction
path3="C:/Users/ELCOT/New folder/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_tran_list= os.listdir(path3)

columns3={"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[], "Transaction_amount":[]}

for state in map_tran_list:
    current_states=path3+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            C=json.load(Data)

            for i in C["data"]["hoverDataList"]:
                            name=i["name"]
                            trans_count=i["metric"][0]["count"]
                            amount=i["metric"][0]["amount"]
                            columns3["Districts"].append(name)
                            columns3["Transaction_count"].append(trans_count)
                            columns3["Transaction_amount"].append(amount)
                            columns3["States"].append(state)
                            columns3["Years"].append(year)
                            columns3["Quarter"].append(int(file.strip(".json")))


            
map_trans=pd.DataFrame(columns3)

#map_user
path4="C:/Users/ELCOT/New folder/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list= os.listdir(path4)

columns4={"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUsers":[], "AppOpens":[]}

for state in map_user_list:
    current_states=path4+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            D=json.load(Data)

            for i in D["data"]["hoverData"].items():
                        district=i[0]
                        resisteredusers=i[1]["registeredUsers"]
                        appopens=i[1]["appOpens"]
                        columns4["Districts"].append(district)
                        columns4["RegisteredUsers"].append(resisteredusers)
                        columns4["AppOpens"].append(appopens)
                        columns4["States"].append(state)
                        columns4["Years"].append(year)
                        columns4["Quarter"].append(int(file.strip(".json")))

map_users=pd.DataFrame(columns4)

#top transaction


path5="C:/Users/ELCOT/New folder/phonepe/pulse/data/top/transaction/country/india/state/"
top_trans_list= os.listdir(path5)

columns5={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state in map_user_list:
    current_states=path5+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            E=json.load(Data)

            for i in E["data"]["pincodes"]:
                        entityName=i["entityName"]
                        count=i["metric"]["count"]
                        amount=i["metric"]["amount"]
                        columns5["Pincodes"].append(entityName)
                        columns5["Transaction_count"].append(count)
                        columns5["Transaction_amount"].append(amount)
                        columns5["States"].append(state)
                        columns5["Years"].append(year)
                        columns5["Quarter"].append(int(file.strip(".json")))


top_trans=pd.DataFrame(columns5)

#top user


path6="C:/Users/ELCOT/New folder/phonepe/pulse/data/top/user/country/india/state/"
top_user_list= os.listdir(path6)

columns6={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUsers":[]}

for state in map_user_list:
    current_states=path6+state+"/"
    agg_year_list=os.listdir(current_states)
    
    for year in agg_year_list:
        current_year=current_states+year+"/"
        agg_file_list=os.listdir(current_year)
        
        for file in agg_file_list:
            current_file=current_year+file
            Data=open(current_file,"r")

            F=json.load(Data)

            for i in F["data"]["pincodes"]:
                        name=i["name"]
                        registeredusers=i["registeredUsers"]
                        columns6["Pincodes"].append(entityName)
                        columns6["RegisteredUsers"].append(count)
                        columns6["States"].append(state)
                        columns6["Years"].append(year)
                        columns6["Quarter"].append(int(file.strip(".json")))


top_user=pd.DataFrame(columns6)

#Table creation for channels
#import pgsql.connector


mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query1='''create table if not exists aggregated_transaction (States varchar(50),
                                                                        Years int,
                                                                        Quarter int,	
                                                                        Transaction_type varchar(50),	
                                                                        Transaction_count bigint,	
                                                                        Transaction_amount bigint
                                                                        )'''
cursor.execute(create_query1)
mydb.commit()
                      

for index,row in aggre_transaction.iterrows():
        insert_query1='''INSERT into aggregated_transaction(States,
                                                        Years,
                                                        Quarter,	
                                                        Transaction_type,	
                                                        Transaction_count,	
                                                        Transaction_amount)

                                                                values(%s,%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Transaction_type'],
                row['Transaction_count'],
                row['Transaction_amount']
                )


        cursor.execute(insert_query1,values)
        mydb.commit()

#aggre user
mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query2='''create table if not exists aggregated_user(States varchar(50),
                                                                        Years int,
                                                                        Quarter int,	
                                                                        Brands varchar(50),	
                                                                        Transaction_count bigint,	
                                                                        Percentage int
                                                                        )'''
cursor.execute(create_query2)
mydb.commit()

for index,row in aggre_user.iterrows():
        insert_query2='''INSERT into aggregated_user(States,
                                                        Years,
                                                        Quarter,	
                                                        Brands,	
                                                        Transaction_count,	
                                                        Percentage)

                                                                values(%s,%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Brands'],
                row['Transaction_count'],
                row['Percentage'],
                )


        cursor.execute(insert_query2,values)
        mydb.commit()

#map trans

mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query3='''create table if not exists map_transaction (States varchar(50),
                                                                        Years int,
                                                                        Quarter int,	
                                                                        Districts varchar(50),	
                                                                        Transaction_count bigint,	
                                                                        Transaction_amount bigint
                                                                        )'''
cursor.execute(create_query3)
mydb.commit()

for index,row in map_trans.iterrows():
        insert_query3='''INSERT into map_transaction(States,
                                                        Years,
                                                        Quarter,	
                                                        Districts,	
                                                        Transaction_count,	
                                                        Transaction_amount)

                                                                values(%s,%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Districts'],
                row['Transaction_count'],
                row['Transaction_amount']
                )


        cursor.execute(insert_query3,values)
        mydb.commit()

#mapuser

mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query4='''create table if not exists map_users(States varchar(50),
                                                                        Years int,
                                                                        Quarter int,	
                                                                        Districts varchar(50),	
                                                                        RegisteredUsers bigint,	
                                                                        AppOpens bigint
                                                                        )'''
cursor.execute(create_query4)
mydb.commit()

for index,row in map_users.iterrows():
        insert_query4='''INSERT into map_users(States,
                                                        Years,
                                                        Quarter,	
                                                        Districts,	
                                                        RegisteredUsers,	
                                                        AppOpens)

                                                                values(%s,%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Districts'],
                row['RegisteredUsers'],
                row['AppOpens']
                )


        cursor.execute(insert_query4,values)
        mydb.commit()

#top trans

mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query5='''create table if not exists top_transaction(States varchar(50),
                                                                        Years int,
                                                                        Quarter int,	
                                                                        Pincodes int,	
                                                                        Transaction_count bigint,	
                                                                        Transaction_amount bigint
                                                                        )'''
cursor.execute(create_query5)
mydb.commit()

for index,row in top_trans.iterrows():
        insert_query5='''INSERT into top_transaction(States,
                                                        Years,
                                                        Quarter,
                                                        Pincodes,		
                                                        Transaction_count,	
                                                        Transaction_amount)

                                                                values(%s,%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Pincodes'],
                row['Transaction_count'],
                row['Transaction_amount']
                )


        cursor.execute(insert_query5,values)
        mydb.commit()

#top user

mydb=psycopg2.connect(host="localhost",
                    user="postgres",
                    password="12345",
                    #database="youtube_data",
                    port="5432")
cursor=mydb.cursor()



create_query6='''create table if not exists top_user(States varchar(50),
                                                                        Years int,
                                                                        Quarter int,
                                                                        Pincodes int,	
                                                                        RegisteredUsers	bigint
                                                                        )'''
cursor.execute(create_query6)
mydb.commit()

for index,row in top_user.iterrows():
        insert_query6='''INSERT into top_user(States,
                                                        Years,
                                                        Quarter,	
                                                        Pincodes,
                                                        RegisteredUsers
                                                        )

                                                                values(%s,%s,%s,%s,%s)'''
        values=(row['States'],
                row['Years'],
                row['Quarter'],
                row['Pincodes'],
                row['RegisteredUsers']
                )


        cursor.execute(insert_query6,values)
        mydb.commit()

def animate_all_amount():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response =requests.get(url)
    data1 = json.loads(response.content)
    state_names_tra = [feature["properties"]["ST_NM"] for feature in data1["features"]]
    state_names_tra.sort()

    df_state_names_tra = pd.DataFrame({"States":state_names_tra})

    frames = []

    for year in map_users["Years"].unique():
        for quarter in aggre_transaction["Quarter"].unique():

            at1 = aggre_transaction[(aggre_transaction["Years"]==year)&(aggre_transaction["Quarter"]==quarter)]
            atf1 = at1[["States","Transaction_amount"]]
            atf1 = atf1.sort_values(by="States")
            atf1["Years"]=year
            atf1["Quarter"]=quarter
            frames.append(atf1)

    merged_df = pd.concat(frames)

    fig_tra = px.choropleth(merged_df, geojson= data1, locations= "States", featureidkey= "properties.ST_NM", color= "Transaction_amount",
                            color_continuous_scale= "Sunsetdark", range_color= (0,4000000000), hover_name= "States", title = "TRANSACTION AMOUNT",
                            animation_frame="Years", animation_group="Quarter")

    fig_tra.update_geos(fitbounds= "locations", visible =False)
    fig_tra.update_layout(width =600, height= 700)
    fig_tra.update_layout(title_font= {"size":25})
    return st.plotly_chart(fig_tra)

def payment_count():
    attype= aggre_transaction[["Transaction_type", "Transaction_count"]]
    att1= attype.groupby("Transaction_type")["Transaction_count"].sum()
    df_att1= pd.DataFrame(att1).reset_index()
    fig_pc= px.bar(df_att1,x= "Transaction_type",y= "Transaction_count",title= "TRANSACTION TYPE and TRANSACTION COUNT",
                color_discrete_sequence=px.colors.sequential.Redor_r)
    fig_pc.update_layout(width=600, height= 500)
    return st.plotly_chart(fig_pc)

# animate all count
def animate_all_count():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()

    df_state_names_tra= pd.DataFrame({"States":state_names_tra})


    frames= []

    for year in aggre_transaction["Years"].unique():
        for quarter in aggre_transaction["Quarter"].unique():

            at1= aggre_transaction[(aggre_transaction["Years"]==year)&(aggre_transaction["Quarter"]==quarter)]
            atf1= at1[["States", "Transaction_count"]]
            atf1=atf1.sort_values(by="States")
            atf1["Years"]=year
            atf1["Quarter"]=quarter
            frames.append(atf1)

    merged_df = pd.concat(frames)

    fig_tra= px.choropleth(merged_df, geojson= data1, locations= "States",featureidkey= "properties.ST_NM",
                        color= "Transaction_count", color_continuous_scale="Sunsetdark", range_color= (0,3000000),
                        title="TRANSACTION COUNT", hover_name= "States", animation_frame= "Years", animation_group= "Quarter")

    fig_tra.update_geos(fitbounds= "locations", visible= False)
    fig_tra.update_layout(width= 600, height= 700)
    fig_tra.update_layout(title_font={"size":25})
    return st.plotly_chart(fig_tra)

def payment_amount():
    attype= aggre_transaction[["Transaction_type","Transaction_amount"]]
    att1= attype.groupby("Transaction_type")["Transaction_amount"].sum()
    df_att1= pd.DataFrame(att1).reset_index()
    fig_tra_pa= px.bar(df_att1, x= "Transaction_type", y= "Transaction_amount", title= "TRANSACTION TYPE and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Blues_r)
    fig_tra_pa.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_tra_pa)


def reg_all_states(state):
    mu= map_users[["States","Districts","RegisteredUsers"]]
    mu1= mu.loc[(mu["States"]==state)]
    mu2= mu1[["Districts", "RegisteredUsers"]]
    mu3= mu2.groupby("Districts")["RegisteredUsers"].sum()
    mu4= pd.DataFrame(mu3).reset_index()
    fig_mu= px.bar(mu4, x= "Districts", y= "RegisteredUsers", title= "DISTRICTS and REGISTERED USERS",
                color_discrete_sequence=px.colors.sequential.Bluered_r)
    fig_mu.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_mu)

def transaction_amount_year(year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
    state_names_tra.sort()
    year= int(year)
    atay= aggre_transaction[["States","Years","Transaction_amount"]]
    atay1= atay.loc[(aggre_transaction["Years"]==year)]
    atay2= atay1.groupby("States")["Transaction_amount"].sum()
    atay3= pd.DataFrame(atay2).reset_index()
    fig_atay= px.choropleth(atay3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_amount", color_continuous_scale="rainbow", range_color=(0,800000000000),
                            title="TRANSACTION AMOUNT and STATES", hover_name= "States")

    fig_atay.update_geos(fitbounds= "locations", visible= False)
    fig_atay.update_layout(width=600,height=700)
    fig_atay.update_layout(title_font= {"size":25})
    return st.plotly_chart(fig_atay)

def payment_count_year(year):
    year= int(year)
    apc= aggre_transaction[["Transaction_type", "Years", "Transaction_count"]]
    apc1= apc.loc[(aggre_transaction["Years"]==year)]
    apc2= apc1.groupby("Transaction_type")["Transaction_count"].sum()
    apc3= pd.DataFrame(apc2).reset_index()

    fig_apc= px.bar(apc3,x= "Transaction_type", y= "Transaction_count", title= "PAYMENT COUNT and PAYMENT TYPE",
                    color_discrete_sequence=px.colors.sequential.Brwnyl_r)
    fig_apc.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apc)

def transaction_count_year(year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1=json.loads(response.content)
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()

    year= int(year)
    atcy= aggre_transaction[["States", "Years", "Transaction_count"]]
    atcy1= atcy.loc[(aggre_transaction["Years"]==year)]
    atcy2= atcy1.groupby("States")["Transaction_count"].sum()
    atcy3= pd.DataFrame(atcy2).reset_index()

    fig_atcy= px.choropleth(atcy3, geojson=data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_count", color_continuous_scale= "rainbow",range_color=(0,3000000000),
                            title= "TRANSACTION COUNT and STATES",hover_name= "States")
    fig_atcy.update_geos(fitbounds= "locations", visible= False)
    fig_atcy.update_layout(width=600, height= 700)
    fig_atcy.update_layout(title_font={"size":25})
    return st.plotly_chart(fig_atcy)

def payment_amount_year(year):
    year= int(year)
    apay = aggre_transaction[["Years", "Transaction_type", "Transaction_amount"]]
    apay1= apay.loc[(aggre_transaction["Years"]==year)]
    apay2= apay1.groupby("Transaction_type")["Transaction_amount"].sum()
    apay3= pd.DataFrame(apay2).reset_index()

    fig_apay= px.bar(apay3, x="Transaction_type", y= "Transaction_amount", title= "PAYMENT TYPE and PAYMENT AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Burg_r)
    fig_apay.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apay)

def reg_state_all_RU(year,state):
    year= int(year)
    mus= map_users[["States", "Years", "Districts", "RegisteredUsers"]]
    mus1= mus.loc[(map_users["States"]==state)&(map_users["Years"]==year)]
    mus2= mus1.groupby("Districts")["RegisteredUsers"].sum()
    mus3= pd.DataFrame(mus2).reset_index()

    fig_mus= px.bar(mus3, x= "Districts", y="RegisteredUsers", title="DISTRICTS and REGISTERED USERS",
                    color_discrete_sequence=px.colors.sequential.Cividis_r)
    fig_mus.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_mus)

def reg_state_all_TA(year,state):
    year= int(year)
    mts= map_trans[["States", "Years","Districts", "Transaction_amount"]]
    mts1= mts.loc[(map_trans["States"]==state)&(map_trans["Years"]==year)]
    mts2= mts1.groupby("Districts")["Transaction_amount"].sum()
    mts3= pd.DataFrame(mts2).reset_index()

    fig_mts= px.bar(mts3, x= "Districts", y= "Transaction_amount", title= "DISTRICT and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Darkmint_r)
    fig_mts.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_mts)

def ques1():
    brand=aggre_user[["Brands","Transaction_count"]]
    brand1= brand.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()

    fig_brands= px.pie(brand2, values= "Transaction_count", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                       title= "Top Mobile Brands of Transaction_count")
    return st.plotly_chart(fig_brands)

def ques2():
    lt= aggre_transaction[["States", "Transaction_amount"]]
    lt1= lt.groupby("States")["Transaction_amount"].sum().sort_values(ascending= True)
    lt2= pd.DataFrame(lt1).reset_index().head(10)

    fig_lts= px.bar(lt2, x= "States", y= "Transaction_amount",title= "LOWEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques3():
    htd= map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF HIGHEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Emrld_r)
    return st.plotly_chart(fig_htd)

def ques4():
    htd= map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF LOWEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    return st.plotly_chart(fig_htd)

def ques5():
    sa= map_users[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="Top 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.deep_r)
    return st.plotly_chart(fig_sa)

def ques6():
    sa= map_users[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="lowest 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.dense_r)
    return st.plotly_chart(fig_sa)

def ques7():
    stc= aggre_transaction[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH LOWEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Jet_r)
    return st.plotly_chart(fig_stc)

def ques8():
    stc= aggre_transaction[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH HIGHEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Magenta_r)
    return st.plotly_chart(fig_stc)

def ques9():
    ht= aggre_transaction[["States", "Transaction_amount"]]
    ht1= ht.groupby("States")["Transaction_amount"].sum().sort_values(ascending= False)
    ht2= pd.DataFrame(ht1).reset_index().head(10)

    fig_lts= px.bar(ht2, x= "States", y= "Transaction_amount",title= "HIGHEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques10():
    dt= map_trans[["Districts", "Transaction_amount"]]
    dt1= dt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    dt2= pd.DataFrame(dt1).reset_index().head(50)

    fig_dt= px.bar(dt2, x= "Districts", y= "Transaction_amount", title= "DISTRICTS WITH LOWEST TRANSACTION AMOUNT",
                color_discrete_sequence= px.colors.sequential.Mint_r)
    return st.plotly_chart(fig_dt)

#streamlit
st.set_page_config(layout= "wide")

st.title(":blue[PHONEPE DATA VISUALIZATION AND EXPLORATION]")
tab1, tab2, tab3 = st.tabs([":red[HOME]","***:blue[EXPLORE DATA]***","***:green[TOP CHARTS]***"])

with tab1:
    col1,col2= st.columns(2)

    with col1:
        st.header(":green[PHONEPE]")
        st.subheader(":blue[INDIA'S BEST TRANSACTION APP]")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("   **-> Credit & Debit card linking**")
        st.write("   **-> Bank Balance check**")
        st.write("   **->Money Storage**")
        st.write("   **->PIN Authorization**")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("c:\\Users\\ELCOT\\Desktop\\phonepe ad\\phone pe Ad\\Phone_Pe_Ad(720p).mp4")

    col3,col4= st.columns(2)
    
    with col3:
        st.video("c:\\Users\\ELCOT\\Desktop\\phonepe ad\\phone pe Ad\\PhonePe_Motion_Graphics(720p)(1).mp4")
        

    with col4:
        st.write("**-> Easy Transactions**")
        st.write("**-> One App For All Your Payments**")
        st.write("**-> Your Bank Account Is All You Need**")
        st.write("**-> Multiple Payment Modes**")
        st.write("**-> PhonePe Merchants**")
        st.write("**-> Multiple Ways To Pay**")
        st.write("**-> 1.Direct Transfer & More**")
        st.write("**-> 2.QR Code**")
        st.write("**-> Earn Great Rewards**")

    col5,col6= st.columns(2)

    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("**->No Wallet Top-Up Required**")
        st.write("**->Pay Directly From Any Bank To Any Bank A/C**")
        st.write("**->Instantly & Free**")

    with col6:
        st.video("c:\\Users\\ELCOT\\Desktop\\phonepe ad\\phone pe Ad\\PhonePe_Motion_Graphics(720p).mp4")

with tab2:
    year = st.selectbox("select the Year",("All", "2018", "2019", "2020", "2021", "2022", "2023"))
    if year == "All" :
        col1, col2 = st.columns(2)
        with col1:
            animate_all_amount()
            payment_count()
            
        with col2:
            animate_all_count()
            payment_amount()

        state=st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
        reg_all_states(state)

    else:
        col1,col2= st.columns(2)

        with col1:
            transaction_amount_year(year)
            payment_count_year(year)

        with col2:
            transaction_count_year(year)
            payment_amount_year(year)
            state= st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
            reg_state_all_RU(year,state)
            reg_state_all_TA(year,state)

with tab3:
    ques= st.selectbox("select the question",('Top Brands Of Mobiles Used','States With Lowest Trasaction Amount',
                                  'Districts With Highest Transaction Amount','Top 10 Districts With Lowest Transaction Amount',
                                  'Top 10 States With AppOpens','Least 10 States With AppOpens','States With Lowest Trasaction Count',
                                 'States With Highest Trasaction Count','States With Highest Trasaction Amount',
                                 'Top 50 Districts With Lowest Transaction Amount'))
    if ques=="Top Brands Of Mobiles Used":
        ques1()

    elif ques=="States With Lowest Trasaction Amount":
        ques2()

    elif ques=="Districts With Highest Transaction Amount":
        ques3()

    elif ques=="Top 10 Districts With Lowest Transaction Amount":
        ques4()

    elif ques=="Top 10 States With AppOpens":
        ques5()

    elif ques=="Least 10 States With AppOpens":
        ques6()

    elif ques=="States With Lowest Trasaction Count":
        ques7()

    elif ques=="States With Highest Trasaction Count":
        ques8()

    elif ques=="States With Highest Trasaction Amount":
        ques9()

    elif ques=="Top 50 Districts With Lowest Transaction Amount":
        ques10()

