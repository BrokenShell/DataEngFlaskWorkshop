import os
import shutil
import uuid

import pandas as pd
from flask import Flask, render_template, request, send_file

from app.tools import data_eng

APP = Flask(__name__)

cache_path = os.path.join("app", "data")
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
os.mkdir(cache_path)


@APP.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join("data", f"{uuid.uuid4()}.csv")
        data_eng(pd.read_csv(file.stream)).to_csv(
            os.path.join("app", filepath),
            index=False,
        )
        return send_file(
            filepath,
            as_attachment=True,
            download_name=file.filename,
        )
    else:
        return render_template("home.html")
