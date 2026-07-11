import chatlas as ctl

chat = ctl.ChatBedrockAnthropic()

# NOTE: in some environments, you may need to wrap
# the `await` call in an async function.
# (this will just work in Positron or a Notebook environment)
await chat.register_mcp_tools_http_stream_async(
  url="https://mcp.deepwiki.com/mcp",
)

await chat.chat_async("Summarize what's in cpsievert/scipy26-tutorial on GitHub")
