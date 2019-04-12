# CODE CHALLENGE: SOORYEN

## Getting started

### Server

1. Enter the `server` directory.

	```bash
	cd server
	```

2. Create a `.env` file with your database configuration using `.env.sample` as a template. 
	* NOTE: Switch PY_ENV to DEV if you wish to run on SQLite in memory. If you mark the PY_ENV as DEV you do not need to fill out the rest of the .env file.
	* If you choose to switch PY_ENV to PRODUCTION to run using an AWS instance.

	
3. Create a virtual environment:

	```bash
	python3 -m venv venv
	```

4. Install the dependencies:

	```bash
	pip3 install -r requirements.txt
	```

5. Run the server:

	```bash
	python3 server.py
	```

### Client

1. In a new terminal, with the server still running, enter the `frontend` directory.

	```bash
	cd frontend
	```

2. Install the dependencies.

	```bash
	npm i
	```

3. Run the client:

	```bash
	npm start
	```
