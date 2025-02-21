from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple list to store hobbies (in memory, no database for simplicity)
hobbies = [
    {"name": "Painting", "description": "Create art with colors!", "tip": "Start with watercolors."},
    {"name": "Gardening", "description": "Grow your own plants.", "tip": "Use pots for small spaces."}
]

@app.route("/")
def home():
    return render_template("index.html", hobbies=hobbies)

@app.route("/add", methods=["GET", "POST"])
def add_hobby():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        tip = request.form["tip"]
        hobbies.append({"name": name, "description": description, "tip": tip})
        return redirect("/")
    return render_template("add_hobby.html")

if __name__ == "__main__":
    app.run(debug=True)