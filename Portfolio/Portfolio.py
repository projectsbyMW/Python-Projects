import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

emptycol, col1, col2 = sl.columns([0.1,0.9,1.6])

with col1:
    sl.image("Portfolio/portimage.jpg")

with col2:
    sl.title("Matheshwaran S")
    content = """
    Hi, I am Matheshwaran, an aspring python programmer and a AWS cloud engineer.
    This is my portfolio where you can view my Python Projects.
    """
    sl.info(content)
    sl.write("[Github Link] (https://github.com/projectsbyMW)" )
    sl.write("[Blog Link] (https://dev.to/madhesh_waran_63)" )
    sl.write("[Site Link] (https://madheshwaran.site)" )
    sl.write("[LinkedIn Link] (https://www.linkedin.com/in/mathesh-waran-957729213)" )
    sl.write("Personal Mobile Number: (+91)-7339590394" )


#sl.title("My Portfolio")
cole1,cole2,cole3 = sl.columns([1.1,0.8,0.8])
with cole1:
    sl.write(" ")
with cole2:
    sl.subheader("My Portfolio")
with cole3:
    sl.write(" ")

col3, col4 = sl.columns(2)

df = pandas.read_csv("Portfolio/data.csv",sep=";")
print(df)

with col3:
    for n,i in df[:10].iterrows():
        sl.header(i["title"])
        sl.write(i["description"])
        sl.image("Portfolio/images/" + i["image"], width= 300)
        sl.write(f"[Source Code] ({i['url']})" )

with col4:
    for n,i in df[10:].iterrows():
        sl.header(i["title"])
        sl.write(i["description"])
        sl.image("Portfolio/images/" + i["image"], width= 300)
        sl.write(f"[Source Code] ({i['url']})" )
