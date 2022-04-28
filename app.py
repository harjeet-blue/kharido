from flask import Flask, redirect, url_for, render_template, request

import demo as dm

app = Flask(__name__)


@app.route("/" , methods= ["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["username"]
        passwd = request.form["password"]

        return redirect(url_for("welcome", name = user))
    else:
        return render_template("loginpage.html")

@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name = name)


@app.route("/homepage")
def homepage():
    return render_template("child.html")

@app.route("/Show Tables")
def citizen():
    ci = dm.get_tables()
    return render_template("index.html", content = "Nikunj", list = ci)

@app.route("/clothing")
def clothing():
    cloths = dm.get_cloths()
    return render_template("clothing.html", list = cloths)

@app.route("/cosmetics")
def cosmetics():
    cosmetics = dm.get_cosmetics()
    return render_template("cosmetics.html", list = cosmetics)

@app.route("/electronics")
def electronics():
    electronics = dm.get_electronics()
    return render_template("electronics.html", list = electronics)

@app.route("/eatables")
def eatables():
    eatables = dm.get_eatables()
    return render_template("eatables.html", list = eatables)

@app.route("/Customers")
def Customers():
    Customers = dm.get_Customers()
    return render_template("Customer.html", list = Customers)

@app.route("/Branch")
def Branch():
    Branch = dm.get_Branch()
    return render_template("Branch.html", list = Branch)

@app.route("/Employee")
def Employee():
    Employee = dm.get_Employee()
    return render_template("Employee.html", list = Employee)

@app.route("/Suppliers")
def Suppliers():
    Suppliers = dm.get_Suppliers()
    return render_template("Supplier.html", list = Suppliers)
@app.route("/Query1")
def Query1():
    Query1 = dm.get_Query1()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query2")
def Query2():
    Query2 = dm.get_Query2()
    return render_template("Supplier.html", list=Query2)
@app.route("/Query3")
def Query3():
    Query1 = dm.get_Query3()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query4")
def Query4():
    Query1 = dm.get_Query4()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query5")
def Query5():
    Query1 = dm.get_Query5()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query6")
def Query6():
    Query1 = dm.get_Query6()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query7")
def Query7():
    Query1 = dm.get_Query7()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query8")
def Query8():
    Query1 = dm.get_Query8()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query9")
def Query9():
    Query1 = dm.get_Query9()
    return render_template("Supplier.html", list=Query1)
@app.route("/Query10")
def Query10():
    Query1 = dm.get_Query10()
    return render_template("Supplier.html", list=Query1)
if __name__ == "__main__":
    app.run(debug=True)

