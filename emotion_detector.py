import streamlit as st
import numpy as np
from transformers import pipeline


TARGET_SAMPLE_RATE = 16000


# ---------------- MODEL CACHE ----------------

@st.cache_resource
def load_model():
    """
    Load model only once and keep in RAM.
    """
    return pipeline(
        "audio-classification",
        model="superb/wav2vec2-base-superb-er",
        top_k=None
    )


# ---------------- PREDICT ----------------

def predict_emotion(samples, sr=TARGET_SAMPLE_RATE):
    """
    Input: numpy float32 samples
    Output: emotion + confidence
    """

    try:
        samples = np.array(samples).astype("float32")

        if samples.size == 0:
            return {"emotion": "neutral", "confidence": 0.0}

        model = load_model()

        outputs = model(
            samples,
            sampling_rate=sr
        )

        if not outputs:
            return {"emotion": "neutral", "confidence": 0.0}

        best = max(outputs, key=lambda x: x["score"])

        return {
            "emotion": best["label"],
            "confidence": round(float(best["score"]), 3)
        }

    except Exception:
        return {"emotion": "neutral", "confidence": 0.0}
