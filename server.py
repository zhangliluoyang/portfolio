from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print('look at me: ', __name__)		# >>> look at me:  server

@app.route("/")
def index():
	# getting info from a html file
    return render_template('index.html')

# accessing html file for each page by matching the filename
@app.route("/<string:page_name>")
def get_page(page_name):
	return render_template(page_name)

# store messages left by users to a file
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		username = data['username']
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f"\n{username},{email},{subject},{message}")

# store users' messages to a csv file
def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as csvfile:
		# fieldnames = ['username', 'email', 'subject', 'message']
		# database = csv.DictWriter(csvfile, fieldnames=fieldnames)
		# database.writeheader()		# add header row
		# print(database)			# >>> <csv.DictWriter object at 0x1023ac7f0>
		
		# get value for each attribute
		username = data['username']
		email = data['email']
		subject = data['subject']
		message = data['message']

		# write to csv file
		database = csv.writer(csvfile, delimiter=',')
		database.writerow([username, email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form(): 
	# fetching submitted data and convert it to a dictionary
	data = request.form.to_dict()
	name = data['username']
	write_to_csv(data)
	print(data)
	return render_template("contact_response.html", name=name)

# @app.route("/about.html")
# def about():
# 	return render_template('about.html')

# @app.route("/contact.html")
# def contact():
# 	return render_template('contact.html')

# using the <username> variable to make the URL dynamic.
# add /name and /number to the URL and refresh the page to see result.
@app.route("/<username>/<int:user_id>")
def user(username=None, user_id=None):
    return render_template('users.html', name=username, user_id=user_id)

@app.route("/salvador")    
def hello_salvador():
	# return text as defined here
	return "Here is Salvador! This is a new route."


if __name__ == "__main__":
	app.run(debug=True)

