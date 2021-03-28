Find the project report [here](https://drive.google.com/file/d/1xy7hId1_ne3NBHKCpPFSlTdQ5qJLAonv/view?usp=sharing)
# Initial Setup
> Pull the code into your system
> Install python3 on your system

Run 
> pip install -r requirements.txt 

# Django setup
Shell or Terminal
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

This will run the server at 127.0.0.1:8000 or localhost:8000

* On the front page you will see an error page
* On /accounts/api/login This is the page where you request to check the login credentials, put a POST Request with username and password.
* On /accounts/api/signup This is the page where we send the details to signup a new user, putting a POST request enters data into database.
* On /chatbot/api On GET Request, it sends a the chatbot details of the particular user.
* On /chatbot/api on POST Request, it creates or modifies the chatbot details of the user.


Testing out the Chabot Details
* Enter the url with the required details: 127.0.0.1:8000/chatbot/<username of the admin>/<anonymous_id>. (Please check the user with that username exists, actually this is just for testing out the chatbot on the admin section.)

* Open the admin window alongside in another window, sending messages from the above test page, will then be received on the admin page.(localhost:3000/messages) and vice versa. If it doesnot work, try refreshing this page or check out the console. I have not put much focus on this page.

* On the websocket section, you can see the consumer.py in chatbot app and can view 2 consumers:
### ChatConsumer
This is the websocket for the the rooms. A room is a representation of the users (admin and the consumer) in a chatbox. It works on ws://127.0.0.1:8000/ws/chat/<admin_username>/<consumer_id>.
The format of messages that are shared is of the form:
*** For fetching the rooms, the admin sends a message as 
{
    'command': 'fetch_messages'
}
whose response is sent as 
{
    command: 'messages',
    messages: [Array of messages]
}
Each message is of the format:
{
    author: Name of the author of the message,
    content: Content of the message,
    room: Room to which they belong: Name of the room is of the format "<username> <consumer>",
    created: Date and time of creation of the message.
}
When a new message is encountered, it is of the format:
{
    command: 'new_message',
    message:{
        author: name of the author,
        content: content of the message
    }
}, 
who's response is sent as 
{
    command: 'new_message;,
    message: {
        author: Name of the author of the message,
        content: Content of the message,
        room: Room to which they belong: Name of the room is of the format "<username> <consumer>",
        created: Date and time of creation of the message.
    }
}
This is the whole explanation of the ChatConsumer.
### RoomConsumer
This is the websocket for the admin only. All the actions of adding a new room, or a sending the details of all the rooms of the admin is done by this websocket. It works on ws://127.0.0.1:8000/ws/room/<admin_username>.

When an admin opens up his portal at localhost:3000/messages, as soon as the admin section connects to RoomConsumer Websocket, it sends a request by the format:
{
    'command':'fetch_rooms'
}
who's response is given to the particular admin section as 
{
    command: 'room',
    rooms: [An array of all the rooms.]
}, where a room is of the format:
{
    consumer: name of the consumer of that room,
    messages: [An array of the messages]
}, where a message is of the format:
{
    author: Name of the author of the message,
    content: Content of the message,
    room: Room to which they belong: Name of the room is of the format "<username> <consumer>",
    created: Date and time of creation of the message.
}.
Whenever the consumer connects to the RoomConsumer(every consumer connects with 2 websockets, the RoomConsumer and the ChatConsumer), a message is sent to the consumer in the format of 
{
    command: 'new_room',
    consumer: consumer id
}, on accpeting the request, the consumer checks is it available in the database or a new one.
If the room with the consumer and admin exists in the database, then it will send a command to only the consumer as 
{
    command:'room_exists'
}, 
since the admin must have got this room's info while fetching all the rooms.
If it isn't there, the consumer will save it to the database and then will send a response to the whole of the websocket as 
{
    command:'new_room',
    room: {
        consumer: name of the consumer of that room,
        messages: [An array of the messages]
    }
},
and the admin section will be notified by the above command and will then connect to this particular room's chatsocket with the url:
ws://127.0.0.1:8000/ws/chat/<admin_username>/<consumer_id>.

This is the working of the websocket on the backend.