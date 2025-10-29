# LiveKit Assistant

First, create a virtual environment, update pip, and install the required packages:

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ python -m pip install --upgrade pip
$ pip install "livekit-agents[groq,silero,turn-detector]~=1.2"
$ pip install python-dotenv
```

You need to set up the following environment variables:

```
LIVEKIT_URL=...
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
GROQ_API_KEY=...
```

Then, run the assistant:

```
$ python agent.py download-files
$ python agent.py console or python agent.py start
```

Finally, you can load the [hosted playground](https://agents-playground.livekit.io/) and connect it.