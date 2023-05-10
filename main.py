from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

Task_List = [{"Task": "Sample Task", "Done": False}]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_task", methods=["POST"])
def add():
    Task_List = request.form['Task']
    Task_List.append({"Task": Task, "Done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods = ["GET", "POST"])
def edit(index):
    Task = Task_List[index]
    if request.method == "POST":
        Task_List['Task'] = request.form["Task"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", Task = Task, index = index)

@app.route("/check/<int:index>")    
def check(index):
    Task_List[index]['Done'] = not Task_List[index]['Done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del Task_List[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug = True)