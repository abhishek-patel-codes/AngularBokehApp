# Demo Registration Application

## Description:

This is a sample Project developed to demonstrate an end to end web application built using flask API's and Angular as client side framework.

## Getting Started

### Prerequisites

1. Python 3.6
2. MongoDB
3. Angular

### Installation

Install the required software.
Clone the source code into a folder and follow the steps below:

#### Client side

1. Open the angular application folder (demo) in the command prompt and run the following command to install dependencies:
	"npm i"
2. To host the client side code locally run the following command:
	"ng serve"
	This should host the code locally in port 4200 by default.

#### Server side

1. Open the server side code in a command prompt and run the following command to install the required python modules.
	"pip install -r requirements.txt"
2. Run the following command to insert initial data into DB:
	"python db_script.py"
3. Start the flask server by running the following command"
	"python demoapi.py"
	
#### MongoDB

1. Create a folder anywhere for local DB storage.
2. Navigate to the folder where MongoDB is installed and move into the bin folder.
3. Open a command prompt in that location and run the following command to start the MongoDB server:
4. For easy access, install ROBO3T for viewing the DB data.
