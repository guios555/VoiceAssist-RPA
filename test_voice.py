import pyttsx3

try:
    print("Inicializando VoiceAssist...")

    engine = pyttsx3.init("sapi5")

    voices = engine.getProperty("voices")
    print(f"Vozes encontradas: {len(voices)}")

    engine.setProperty("volume", 1.0)
    engine.setProperty("rate", 170)

    print("Iniciando teste de áudio...")

    engine.say("Olá! Eu sou a Wúai.")
    engine.runAndWait()

    print("Teste de áudio finalizado!")

except Exception as erro:
    print(f"ERRO: {erro}")