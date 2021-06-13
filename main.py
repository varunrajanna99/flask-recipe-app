from flask import request, Flask, render_template
from decouple import config
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_recipe():
    
    query_param = request.query_string.decode("ascii")
    
    api_id = config("APP_ID")
    api_key = config("APP_KEY")
    
    url = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={api_id}&app_key={api_key}&{query_param}&imageSize=REGULAR"

    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        data["status"] = "success"
        return render_template("main.html", data=data)
        
    return {"status": "failed", "recipes": json.loads(response.content)}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)