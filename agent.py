# agent.py  python agent.py console
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from Jarvis_prompts import behavior_prompts, Reply_prompts

load_dotenv()

# tiny prompts (swap for Jarvis_prompts import if you have that file)

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=behavior_prompts)

async def entrypoint(ctx: agents.JobContext):
    # Direct, minimal RealtimeModel usage (assumes plugin API matches)
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(voice="Charon")
    )

    # Start session with noise cancellation and video enabled
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True
        ),
    )

    # make sure we are connected to LiveKit control plane
    await ctx.connect()

    # Send greeting
    await session.generate_reply(instructions=Reply_prompts)

    # keep running until session ends
    await session.wait_closed()

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
