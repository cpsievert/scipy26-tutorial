import chatlas as ctl

chat = ctl.ChatBedrockAnthropic()

# TODO: Define+register a tool to report the current date and time

chat.chat("What day is it today?")
