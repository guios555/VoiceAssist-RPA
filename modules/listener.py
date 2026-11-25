import speech_recognition as sr


class Listener:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        try:
            with sr.Microphone() as source:

                print("\nOuvindo...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=6
                )

            command = self.recognizer.recognize_google(
                audio,
                language="pt-BR"
            )

            print(f"Comando recebido: {command}")

            return command.lower()

        except sr.UnknownValueError:
            print("Não consegui entender o comando.")
            return None

        except sr.RequestError:
            print("Erro na conexão com o serviço de reconhecimento.")
            return None

        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada.")
            return None

        except OSError as error:
            print(f"Erro no microfone: {error}")
            return None