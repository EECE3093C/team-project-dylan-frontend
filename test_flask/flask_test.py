from flask import request, Flask, render_template
app = Flask(__name__) #flask constuctor

@app.route('/', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        hourly_pay = int(request.form.get("hourly"))
        hours_worked = int(request.form.get("hours"))
        return "Weekly Pay = $" + str((hourly_pay * hours_worked))
    return render_template("layout.html")

if __name__ == '__main__':
    app.run()