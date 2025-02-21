from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory list of hobbies with categories
hobbies = [
    {"name": "Painting", "description": "Create art with colors!", "tip": "Start with watercolors.", "category": "Creative"},
    {"name": "Gardening", "description": "Grow your own plants.", "tip": "Use pots for small spaces.", "category": "Outdoor"}
]

@app.route("/")
def home():
    # Count hobbies per category
    categories = {}
    for hobby in hobbies:
        categories[hobby["category"]] = categories.get(hobby["category"], 0) + 1
    return render_template("index.html", hobbies=hobbies, categories=categories)

@app.route("/add", methods=["GET", "POST"])
def add_hobby():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        tip = request.form["tip"]
        category = request.form["category"]
        hobbies.append({"name": name, "description": description, "tip": tip, "category": category})
        return redirect("/")
    return render_template("add_hobby.html")

if __name__ == "__main__":
    app.run(debug=True)
    