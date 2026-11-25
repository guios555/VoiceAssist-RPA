import json
from pathlib import Path

from modules.listener import Listener
from modules.speaker import Speaker
from modules.executor import Executor
from modules.logger import logger


BASE_DIR = Path(__file__).resolve().parent

COMMANDS_FILE = BASE_DIR / "config" / "commands.json"


def load_commands():

    with open(COMMANDS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def main():

    speaker = Speaker()
    listener = Listener()
    executor = Executor()

    commands = load_commands()

    logger.info("Wúai iniciada")

    speaker.speak("Assistente iniciada e pronta para ouvir.")

    running = True

    while running:

        command = listener.listen()

        if command is None:
            continue

        action = commands.get(command)

        if action is None:

            speaker.speak("Não reconheci esse comando.")
            logger.warning(f"Comando não reconhecido: {command}")

            continue

        response = executor.execute(action)

        speaker.speak(response)

        if action == "exit":
            running = False

    logger.info("Wúai encerrada")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nAssistente encerrada pelo usuário.")

    except Exception:
        logger.exception("Erro inesperado na aplicação")
        print("Ocorreu um erro. Consulte o arquivo de log.")