**_What is the project?_**

This is a web server that connects multiple cars to multiple users at the same time, these users can control physical cars (using ESP32) with inputs from a website. These users can race their cars in the real world to win, the races are moderated by the admin who controls the whole race. 

**_Brief Introduction to the Project_**

• The server connects a remotely controlled car that uses an ESP32, with its user.

• This specific website was made for handling multiple such connections for conducting a race.

• The admin controls when the race has begun, when new players can join and end the session of current players.

• Each car also gives video input to the server and the player can run the car using the video input.

• This gives the user the ability to connect to the car from anywhere in the world, provided the server is deployed.

**_Specifications_**

• The project has a config.py file from which the number of players can be changed easily and the appropriate changes will be made throughtout the program.

• This project uses web sockets to handle user inputs as well as video inputs from the car and outputs the set of instructions to the car:  
this gives much higher refresh rates, I was able achieve upto 30Hz refresh rate, much faster as compared the a dozen or so from standard HTTPS GET or POST requests. 

• Because this project was made for an event we were supposed to conduct, the users that join must enter their phone numbers, name and so on, which is stored on a local database for later reference.

• As the link to the website is public knowledge and I didn't want previous players to interfere with the game, the website reuses the previous player with a new password, thus allowing a smooth operation of the race.

• The server uses Bcrypt for password encryption, SQLAlchemy for the database, python-Flask as the backend, Socketio for handling sockets, cv2 from OpenCV for saving and loading images, and javascript for dynamic handling the user inputs from the frontend, as well as HTML Bootstrap for styling the pages.
