import gradio as gr
import numpy as np
from scipy.io.wavfile import write
import tempfile

def stress_to_music(stress_level):
    sr = 22050  # sample rate
    duration = 2  # seconds
    t = np.linspace(0, duration, int(sr * duration), False)
    freq = 220 + stress_level * 3
    tone = 0.5 * np.sin(2 * np.pi * freq * t)
    
    tmp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(tmp_wav.name, sr, (tone * 32767).astype(np.int16))
    return tmp_wav.name

demo = gr.Interface(
    fn=stress_to_music,
    inputs=gr.Slider(0, 100, step=1, label="Stress Level"),
    outputs="audio",
    title="Stress → Music Converter",
    description="Move the slider to generate calming or intense music based on stress level 🎶"
)

if __name__ == "__main__":
    demo.launch()
