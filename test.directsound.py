import pyaudio

audio = pyaudio.PyAudio()

print("Iniciando teste DirectSound...")

try:
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        input_device_index=1,
        frames_per_buffer=1024,
        start=False
    )

    print("Microfone aberto com sucesso!")

    stream.start_stream()

    print("Capturando áudio por 5 segundos...")

    for _ in range(0, int(44100 / 1024 * 5)):
        data = stream.read(1024, exception_on_overflow=False)

    print("Captura finalizada com sucesso!")

    stream.stop_stream()
    stream.close()

except Exception as erro:
    print(f"ERRO NA CAPTURA: {erro}")

finally:
    audio.terminate()