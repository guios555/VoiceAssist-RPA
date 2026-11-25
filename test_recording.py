
import pyaudio
import wave
import time
import math
from array import array

# Configurações da captura
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
DEVICE_INDEX = 1

audio = pyaudio.PyAudio()
stream = None

try:
    # Identifica o microfone selecionado
    device = audio.get_device_info_by_index(DEVICE_INDEX)

    print(f"Microfone: {device['name']}")
    print(f"Índice: {DEVICE_INDEX}")
    print("Preparando gravação...")

    frames = []

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=DEVICE_INDEX,
        frames_per_buffer=CHUNK
    )

    print("Gravando! Fale normalmente por 5 segundos.")

    inicio = time.monotonic()
    limite = inicio + RECORD_SECONDS

    while time.monotonic() < limite:
        data = stream.read(
            CHUNK,
            exception_on_overflow=False
        )
        frames.append(data)

    tempo_total = time.monotonic() - inicio

    stream.stop_stream()
    stream.close()
    stream = None

    # Analisa o sinal capturado
    audio_data = b"".join(frames)
    samples = array("h")
    samples.frombytes(audio_data)

    pico = max(abs(sample) for sample in samples)

    rms = math.sqrt(
        sum(sample * sample for sample in samples) / len(samples)
    )

    # Salva o arquivo WAV
    arquivo = "captura.wav"

    with wave.open(arquivo, "wb") as wav:
        wav.setnchannels(CHANNELS)
        wav.setsampwidth(audio.get_sample_size(FORMAT))
        wav.setframerate(RATE)
        wav.writeframes(audio_data)

    # Verifica a duração real do arquivo
    duracao_wav = (
        len(audio_data) /
        (RATE * CHANNELS * audio.get_sample_size(FORMAT))
    )

    print("\n--- DIAGNÓSTICO DA CAPTURA ---")
    print(f"Tempo de captura: {tempo_total:.2f} segundos")
    print(f"Duração WAV: {duracao_wav:.2f} segundos")
    print(f"Amostras: {len(samples)}")
    print(f"Pico: {pico}")
    print(f"RMS: {rms:.2f}")
    print(f"Arquivo salvo: {arquivo}")

finally:
    if stream is not None:
        stream.stop_stream()
        stream.close()

    audio.terminate()
