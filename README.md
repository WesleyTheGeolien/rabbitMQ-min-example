# rabbitMQ-min-example

# To run
1. `docker-compose` -f "docker-compose.yml" up -d --build`
1. Navigate to `http://localhost:15672`
    - Username: user (see docker-compose.yml)
    - Password: password (see docker-compose.yml)
    - If you change these you will need to provide `--user` and `--password` args to `send.py` and `receive.py`
1. Install pika (RabbitMQ python client) `pip install pika` or `pip install -r requirments.txt`
1. Send a message to the Broker
    1. `python send.py` (`--help` for all options and setup)
1. Setup a receiver (this blocks the terminal so maybe a good idea to run in a different terminal)
    1. `python receive.py` (`--help` for all options and setup)

## Default values (using environment variables)
Default values for:
    - host: os.environ.get('BROKER_HOST', 'localhost') # Need to change if not running locally
    - port: os.environ.get('BROKER_PORT', 5672) # Need to change if not default port
    - user: os.environ.get('BROKER_USER', 'user') # Need to change if not running default username in rabbitMQ docker-compose service
    - password: os.environ.get('BROKER_PASSWORD', 'password') # Need to change if not running default password in rabbitMQ docker-compose service
    - queue: 'test'
    - body: 'Hello World!'

# Advanced usage

## Multi queues
You can specify different queues for example testing on different machines.

For example on machine one:
1. `python receive.py --queue machine1`
1. On machine 2: `python receive.py --queue machine2`

Then to test:
1. `python send.py --body 'This should go to machine 1!' --queue machine1`
1. `python send.py --body 'This should go to machine 2!' --queue machine2`

To mock this open 2 different terminals
