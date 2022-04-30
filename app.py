# https://stackoverflow.com/jobs?r=true&q=python -> 작동 안됨
# https://weworkremotely.com/remote-jobs/search?term=python
# https://remoteok.io/remote-dev+python-jobs

from flask import Flask, render_template, request, redirect, send_file
import module.remoteok as remoteok
import module.weworkremotely as weworkremotely
import module.export as exportCSV

app = Flask("SuperScrapper")
db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    data = []
    search = request.args.get('search')
    if search in db:
        data = db[search]
    else:
        remoteok.extract_job(search, data)
        weworkremotely.extract_job(search, data)
        db[search] = data

    return render_template("search.html", data=data, count=len(data), search=search)


@app.route("/export/<name>")
def export(name):
    exportCSV.save_to_file(name, db[name])
    return send_file(f"{name}.csv")


app.run(host="0.0.0.0", port="5500", debug=True)
