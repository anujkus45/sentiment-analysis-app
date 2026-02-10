import librosa
import numpy as np


def chunk_audio(file_path, chunk_length_ms=4000):

    y, sr = librosa.load(file_path, sr=16000, mono=True)

    chunk_size = int(sr * (chunk_length_ms / 1000))

    chunks = []

    total_len = len(y)

    for start in range(0, total_len, chunk_size):

        end = start + chunk_size

        chunk = y[start:end]

        # Skip very small chunks
        if len(chunk) < chunk_size * 0.5:
            continue

        time_sec = round(start / sr, 2)

        chunks.append({
            "time": time_sec,
            "chunk": chunk,
            "sr": sr
        })

    return chunks
