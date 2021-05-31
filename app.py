from flask import Flask
from flask import request, jsonify
from User import User
from Database import Database
from Event import Event


app = Flask(__name__)


db = Database()

@app.route('/add_user', methods = ['POST'])
def add_user():
    data = request.get_json()
    data = data['Users']

    for user_data in data:
        email = user_data.get('Email')
        user_name = user_data.get('userName')
        user = User(email,  user_name)
        db.users_in_database.append(user)
        db.map_users[email] = user

    return "Users Added successfully!!"

@app.route('/add_event', methods = ['POST'])
def add_event():
    data = request.get_json()
    email = data['Email']
    event_description = data['eventDescription']
    event_date = data['date']
    eventId = data['eventId']

    start_time = data['start_time']
    end_time = data['end_time']
    isRecurring = data['isRecurring']
    recur = data['recur']

    user = db.users_in_database.get(email)
    if user:
        user.calender.addEvent(event_date, start_time,  end_time, event_description, eventId, isRecurring, recur, db)
        return "Event added to user"
    else:
        return "User does not exists"

@app.route('/show_calender/<string:email>', methods = ['GET'])
def show_calender(email):
    user = db.map_users.get(email)
    calender = user.calender
    list_events = calender.showCalender()
    response = []
    for event in list_events:
        response.append((event.eventId ,event.start_time,event.end_time, event.event_accept_reject_status))

    return jsonify({"Event" : response})


@app.route('/update_event/<string:event_id>', methods = ['PUT'])
def update_event(event_id):
    data = request.get_json()
    email = data['Email']
    event_description = data['eventDescription']
    event_date = data['date']
    eventId = data['eventId']

    start_time = data['start_time']
    end_time = data['end_time']
    isRecurring = data['isRecurring']
    recur = data['recur']

    event = db.map_events.get(event_id)
    event.email = email
    event.event_description = event_description
    event.event_date = event_date
    event.start_time = start_time
    event.end_time = end_time
    event.isRecurring = isRecurring
    event.recur = recur

    return "Event update!!"

@app.route('/accept_invite/<string:email>/<string:event_id>', methods = ['GET'])
def accept_invite(email, event_id):
    event = db.map_events.get(event_id)
    event.accept_event()
    return "Event Accepted"

@app.route('/reject_invite/<string:email>/<string:event_id>', methods=['GET'])
def reject_invite(email, event_id):
    event = db.map_events.get(event_id)
    event.accept_event()
    return "Event Rejected"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
