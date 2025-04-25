Install dependencies: $ pip install "fastapi[standard]" $ pip install uvicorn $ pip install websockets

/CreateProfile.py "Profile" class: sets up attributes: name, email, class_year, field_of_study, interests, and filters

Defines attribute validation functions:
"email*validate": checks for email format WILL HOPEFULLY check against existing database of emails and act as unique key for each user

database does NOT yet exist --> will need to find a way to store users in global database

"class_year_validate": checks that the inputted year is from current students 2025 to 2028 takes boolean parameter to add 'any' when in filter

"gender_validate": checks against pre-populated gender options takes boolean parameter to add 'any' when in filter

"field_of_study_validate": checks against pre-populated field cluster options takes boolean parameter to add 'any' when in filter

"create_profile" function: Creates and returns Profile object from user input. Defines and, if needed, validates each attribute on user input. Attributes "interests" and "filters" exist as dictionaries of lists of strings, the former separated by "academic", "career", and "extracurricular" and the latter by "gender", "field_of_study", and "class_year". Interests are arbitrary and can be user specific. Filters refer to preferences they would like in possible matches and are validated.

"main" function: Runs the scheme of app in terminal. Creates, prints, and stores profile in (placeholder) database of users.

/MatchProfiles.py "MatchProfiles" Takes two paramaters: profile1 and profile2, both are Profile objects Compares attributes and filters between both and returns boolean if all areas match

/Servermain.py "Server" class uses import Websocket to make connections

"websocket_endpoint" async function, awaits websockets and covers disconnection

"main" runs server on host

/Client1.py and /Client2.py For purposes of client chatting, sending and receiving messages using websocket connection from FastAPI

"get_username" takes user input of name

"send_message" async function, takes websocket and username parameters sends and prints message from client

"receive_message" async function, takes websocket and username parameters receives and prints message from other client

"chat_client" async function, takes username paramater connect url's

"main" gets username and runs client of name
