import pyaudio

# Inicializa o teste de microfone
audio = pyaudio.PyAudio()

print("\n=== DISPOSITIVOS DE ÁUDIO ===\n")
# Lista todos os dispositivos de áudio disponíveis
for index in range(audio.get_device_count()):

    device = audio.get_device_info_by_index(index)

    #Filtra apenas os dispositivos de entrada (microfones)
    if device['maxInputChannels'] > 0:

        print(f"Índice: {index}")
        print(f"Nome: {device['name']}")
        print(f"Canais de entrada: {device['maxInputChannels']}")
        print(f"Taxa de amostragem: {device['defaultSampleRate']}")
        print("-" * 40)

#Identifica  o dispositivo padrão

try: 
    default_device = audio.get_default_input_device_info()

    print("\n=== MICROFONE PADRÃO ===")
    print(default_device["name"])
    print("Índice:", default_device["index"])

except OSError:
    print("\nNenhum microfone padrão encontrado.")

#Finalisa o teste de microfone
audio.terminate()
