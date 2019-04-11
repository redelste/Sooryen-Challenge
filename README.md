# CODE CHALLENGE: SOORYEN

## Getting started

### Server

1. Enter the `server` directory.

	```bash
	cd server
	```

2. Create a `.env` file with your database configuration using `.env.sample` as a template.

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