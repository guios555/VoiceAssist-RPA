import pyaudio

audio = pyaudio.PyAudio()

print("=== APIs DE ÁUDIO ===")

for i in range(audio.get_host_api_count()):
    print(i, audio.get_host_api_info_by_index(i)["name"])

print("\n=== TESTE DO MICROFONE REDRAGON ===")

for i in range(audio.get_device_count()):
    device = audio.get_device_info_by_index(i)

    if device["maxInputChannels"] > 0:
        print(f"\nDispositivo: {device['name']}")
        print(f"Índice: {i}")
        print(f"Host API: {audio.get_host_api_info_by_index(
            device['hostApi']
        )['name']}")

        try:
            audio.is_format_supported(
                44100,
                input_device=i,
                input_channels=1,
                input_format=pyaudio.paInt16
            )
            print("Formato: SUPORTADO")
        except Exception as erro:
            print(f"Formato: NÃO SUPORTADO ({erro})")

audio.terminate()