import librosa


def chunk_audio(file_path, chunk_length_ms=10000):

    # Load audio (cloud-safe)
    y, sr = librosa.load(file_path, sr=16000, mono=True)

    chunk_samples = int(sr * (chunk_length_ms / 1000))

    chunks = []

    for i in range(0, len(y), chunk_samples):

        chunk = y[i:i + chunk_samples]

        time_sec = i / sr

        chunks.append({
            "time": time_sec,
            "chunk": chunk,
            "sr": sr
        })

    return chunks
