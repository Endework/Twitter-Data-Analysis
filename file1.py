import pandas as pd
import mydatabase as dbu

database = 'project.db'


def load_info_table():
# create the products table
    #query = 'CREATE TABLE info ([created_at  CHAR, source CHAR ,text  CHAR,lang CHAR, favorite_count FLOAT)'
    query='CREATE TABLE info ([created_at DATE, source CHAR,text CHAR,	polarity FLOAT,	subjectivity FLOAT,	lang CHAR,	favorite_count INTIGER,	retweet_count INTEGER,	original_author CHAR ,	followers_count INTEGER,	friends_count	INTEGER , sensitivity	BOOL, hashtags CAHR,	mentions CAHR,	place CHAR,	cleaned_text CHAR,	flattened_hashtags	CAHR, sentiment	label, CAHR])'
    dbu.execute_sql(database=database, sql=query)


    # insert all rows into the products table
    info = pd.read_excel(r'C:\Users\ende\Desktop\Twitter-Data-Analysis-main (1)\Twitter-Data-Analysis-main\final_data.xlsx')
    dbu.insert_data(database='project.db', table='info', data=info)



   

if __name__=='__main__':
    load_info_table()
    