from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection
conn = 'mongodb://localhost:27017'


# @TODO: connect to mongo db and collection
client = pymongo.MongoClient(conn)
db = client.inventory


@app.route('/')
def index():
    # @TODO: write a statement that finds all the items in the db and sets it to a variable
    produce_ls = list(db.produce.find())
    print(produce_ls)

    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return render_template('index.html', produce=produce_ls)


if __name__ == "__main__":
    app.run(debug=True)
