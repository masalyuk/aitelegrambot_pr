from importlib.metadata import version

WELCOME_MESSAGE: str = f"""
Hello! I am running aitelegrambot v{version('aitelegrambot')}.

To inference something please run, /infer.

I am licensed under the GPLv3. For more information, Please find the source code at https://github.com/tusharhero/aitelegrambot.git/
"""
HELP_MESSAGE: str = """
*Normal commands*:
- /start
- /infer <query>
- /help
*Administration commands*:
- /list\_models
- /change\_model <model\_name>
- /pull\_model <model\_name>
- /remove\_model <model\_name>
"""
