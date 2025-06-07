# HF Spaces Demo

This directory contains a minimal example for hosting the **GenAI Processors** demos on [Hugging Face Spaces](https://huggingface.co/spaces).

The `app.py` script exposes a simple interface for generating music via Google's Live Music API. Upload the contents of this folder to a new Space and specify the dependencies listed in `requirements.txt`.

## Files

- `app.py` – Gradio application that connects to the Live Music API and returns the generated audio.
- `requirements.txt` – Python dependencies.

Make sure your Space has the `GOOGLE_API_KEY` environment variable set or enter it in the provided textbox when launching the app.
