import argparse
import asyncio
import os


def _get_api_key() -> str:
    """Returns the API key, prompting the user if missing."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        api_key = input("Enter your Google API key: ").strip()
        os.environ["GOOGLE_API_KEY"] = api_key
    return api_key

from genai_processors.core import audio_io
import commentator
import pyaudio

QUIZ_PROMPT_PARTS = [
    (
        "You are a contestant in a quiz competition. You cannot see any video. "
        "Listen carefully to the questions and answer as accurately and "
        "succinctly as possible."
    ),
]

API_KEY = _get_api_key()


async def run_competition(model_name: str) -> None:
    """Runs the audio-only AI competitor."""
    pya = pyaudio.PyAudio()

    async def input_stream():
        try:
            while True:
                await asyncio.sleep(1)
        finally:
            pass

    competitor_processor = commentator.create_live_commentator(
        API_KEY,
        chattiness=0.0,
        prompt_parts=QUIZ_PROMPT_PARTS,
        model_name=model_name,
    )

    consume_output = audio_io.PyAudioOut(pya)

    agent = audio_io.PyAudioIn(pya) + competitor_processor + consume_output

    async for _ in agent(input_stream()):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default="models/gemini-2.5-pro-latest",
        help="Gemini model to use",
    )
    args = parser.parse_args()
    asyncio.run(run_competition(model_name=args.model))
