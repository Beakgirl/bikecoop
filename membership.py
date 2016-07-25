import flask
from flask import render_template
from flask import request
import webbrowser

f = open("membership.html")

filename = "/Users/Beakgirl/PycharmProjects/bikemembership/membership.html"
webbrowser.open_new_tab(filename)

app = flask.Flask("MyApp")

rider = raw_input ("Why do you ride a bike? ")
maillist = raw_input ("How do you feel about learning more about our events? ")


print "So you ride your bike because %r and feel %r about being on the mailing list! Cool!" % (
	rider, maillist)


membership = raw_input("Would you like to be a member?")
print "hell %r, well you can sign up below!" % ( membership)


@app.route("/")
def hello():
    return render_template("signup.html")


@app.route("/membership/<name>")
def hello_someone(name):
    return render_template("signup.html", name=name.title())


@app.route("/membership/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    print form_data['email']
    print form_data['age']
    print form_data['telephone']
    return "All OK"


app.run()
