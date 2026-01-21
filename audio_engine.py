"""
Audio Engine for generating sounds during sorting
"""
import numpy as np
import pyaudio
from constants import SAMPLE_RATE, MIN_FREQUENCY, MAX_FREQUENCY, SOUND_DURATION, MIN_VALUE, MAX_VALUE


class AudioEngine:
    """Handles audio generation for the sorting visualizer"""
    
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=SAMPLE_RATE,
            output=True
        )
    
    def play_note(self, value):
        """
        Play a sound based on the value
        Maps array values to frequencies
        """
        # Map value to frequency range
        frequency = MIN_FREQUENCY + (value - MIN_VALUE) * (MAX_FREQUENCY - MIN_FREQUENCY) / (MAX_VALUE - MIN_VALUE)
        
        # Generate sine wave
        samples = np.arange(int(SAMPLE_RATE * SOUND_DURATION))
        wave = 0.3 * np.sin(2 * np.pi * frequency * samples / SAMPLE_RATE)
        
        # Apply envelope to avoid clicks
        envelope = np.linspace(1, 0, len(wave))
        wave = wave * envelope
        
        # Play the sound
        self.stream.write(wave.astype(np.float32).tobytes())
    
    def cleanup(self):
        """Clean up audio resources"""
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()