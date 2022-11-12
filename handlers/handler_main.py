from handlers.handler_com import HandlerCommands


class HandlerMain:
    """
    Class-componer
    """

    def __init__(self, bot):
        self.bot = bot
        self.handler_commands = HandlerCommands(self.bot)

    def handle(self):
        self.handler_commands.handle()
