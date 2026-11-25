import webbrowser
import psutil
import pyautogui

from modules.logger import logger


class Executor:

    def execute(self, action):

        if action == "open_browser":

            webbrowser.open("https://www.google.com")

            logger.info("Navegador aberto")
            return "Abrindo o navegador."

        elif action == "system_status":

            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent

            logger.info("Consulta de status do sistema")

            return (
                f"O uso da CPU está em {cpu}% por cento. "
                f"A memória RAM está em {ram}% por cento."
            )

        elif action == "minimize_all":

            pyautogui.hotkey("win", "d")

            logger.info("Todas as janelas minimizadas")

            return "Área de trabalho exibida."

        elif action == "exit":

            logger.info("Encerramento solicitado")
            return "Até logo."

        else:

            logger.warning(f"Ação desconhecida: {action}")

            return "Não reconheço essa ação."