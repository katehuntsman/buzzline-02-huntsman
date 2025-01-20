# buzzline-02-huntsman

```
This project demonstrates how to set up and use Apache Kafka for real-time streaming and message processing. It includes a Kafka producer that generates custom sentence messages and a Kafka consumer that processes and logs those messages.

In this project, I've created a custom Kafka producer and consumer to handle real-time streaming of sentence-based messages.

Kafka Producer (kafka_producer_huntsman.py): Generates sentence-based messages and sends them to a Kafka topic.
The producer sends predefined sentence-based messages to a Kafka topic at regular intervals. These messages are randomly selected from a list and sent to the Kafka broker. The producer is set up to run indefinitely until interrupted by the user.

Key Features:
- Generates real sentence messages instead of just timestamps.
- Sends messages at regular intervals (configurable).
- Logs the generated message and when it is sent to the Kafka topic.

Kafka Consumer (kafka_consumer_huntsman.py): Consumes messages from the Kafka topic and processes them by logging the details.
The consumer listens to the Kafka topic and processes the messages it receives. Each message is logged along with its details, including the message content and its offset within the Kafka topic.

Key Features:
- Consumes messages from the Kafka topic buzzline.
- Logs the message details and processes the content (in this case, just logging the message).
- Can be configured to start from the earliest offset to consume all available messages.

```

Streaming data is often too big for any one machine. 
A streaming platform helps organize our pipelines.

A common pattern for managing streaming pipelines is publish-subscribe, similar to how Twitter operates:

- Producers publish streaming information.
- Consumers subscribe to specific "topics" to process, analyze, and generate alerts based on detected conditions.

In this project, we use Apache Kafka, a popular, open-source streaming platform.
We write producers that send data to topics and consumers that read from topics.

> Kafka needs space - it's big. We'll use the Windows Subsystem for Linux on Windows machines. 

## Task 1. Install and Start Kafka (using WSL if Windows)

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> first. 
Python 3.11 is required. 

In this task, we will download, install, configure, and start a local Kafka service. 

1. Install Windows Subsystem for Linux (Windows machines only)
2. Install Kafka Streaming Platform
3. Start the Zookeeper service (leave the terminal open).
4. Start the Kafka service (leave the terminal open).

For detailed instructions, see:

- [SETUP-KAFKA](docs/SETUP-KAFKA.md) (all machines)


## Task 2. Copy This Example Project & Rename

Copy/fork this project into your GitHub account
and create your own version of this project to run and experiment with. 
Name it `buzzline-02-yourname` where yourname is something unique to you.
Follow the instructions in [FORK-THIS-REPO.md](https://github.com/denisecase/buzzline-01-case/blob/main/docs/FORK-THIS-REPO.md)).
    

## Task 3. Manage Local Project Virtual Environment

Follow the instructions in [MANAGE-VENV.md](https://github.com/denisecase/buzzline-01-case/blob/main/docs/MANAGE-VENV.md) to:
1. Create your .venv
```
python3.11 -m venv .venv
```

2. Activate .venv
```
source .venv/bin/activate
```

3. Install the required dependencies using requirements.txt.

## Task 4. Start a Kafka Producer

Producers generate streaming data for our topics.

In VS Code, open a terminal.
Use the commands below to activate .venv, and start the producer. 

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.kafka_producer_huntsman
```

## Task 5. Start a Kafka Consumer

Consumers process data from topics or logs in real time.

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.kafka_consumer_huntsman
```

## Later Work Sessions
When resuming work on this project:
1. Open the folder in VS Code. 
2. Start the Zookeeper service.
3. Start the Kafka service.
4. Activate your local project virtual environment (.env).

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a valuable skill. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.
