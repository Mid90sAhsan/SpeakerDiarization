from pyannote.audio import Pipeline

# Load the pretrained model
pipeline = Pipeline.from_pretrained(
  "pyannote/speaker-diarization-3.1",
  use_auth_token="HUGGING-FACE-TOKEN")

# Run on your audio file (must be WAV or compatible format)
diarization = pipeline("sample.wav")

# Print the results
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.1f}s - {turn.end:.1f}s: Speaker {speaker}")