from flask import Flask,render_template
import pandas

app = Flask("__name__")

st = pandas.read_csv("data_small/stations.txt", skiprows = 17)
st = st[['STAID', 
         'STANAME                                 ']]             
stationstable = st.to_html()

@app.route("/")
def home():
    return render_template("home.html",data=stationstable)

@app.route("/api/v1/<station>/<date>")
def weather(station,date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows= 20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date] ['   TG'].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}

@app.route("/api/v1/<station>")
def alldata(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows= 20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/<station>/year/<year>")
def yeardata(station,year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows= 20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df['    DATE'].str.startswith(str(year)) ]
    return result.to_dict(orient="records")

@app.route("/api/v1/<word>")
def wordapi(word):
    df = pandas.read_csv("dictionary.csv")
    defi = df.loc[df['word'] == word] ['definition'].squeeze()
    return {"definition": defi, "word": word}

if __name__ == "__main__":
    app.run(debug=True)