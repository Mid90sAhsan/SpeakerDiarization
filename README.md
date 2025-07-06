# 🗣️ Speaker Diarization with `pyannote/speaker-diarization-3.1`

This repo demonstrates how to run a **local AI model** that performs **speaker diarization** – identifying **who spoke when** in a `.wav` audio file using Hugging Face's [`pyannote/speaker-diarization-3.1`](https://huggingface.co/pyannote/speaker-diarization-3.1).

Perfect for use cases like:
- Podcasts
- Interviews
- Meeting recordings
- Audio segmentation

---

## 🔥 What You'll Get

Given a `.wav` file, the model returns output like:

0.0s - 7.2s: Speaker SPEAKER_00
8.8s - 15.6s: Speaker SPEAKER_01
