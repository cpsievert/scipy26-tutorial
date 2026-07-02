## Title: Intro to Safe, Verifiable, and Maintainable AI Apps in Python

**Welcome (15 min)**

- Introductions
- Pre-requisites 
  - Bring your own API key 
  - Or download local model via LMStudio
- Backup computing environment: Jupyterlite? Shinylive? Codespaces? Something else?


**AI: feel the feelings (10 min)**

- I feel deeply conflicted about AI
  - I'm so much more productive, but at what cost?
    - Personal (am I losing the ability to think for myself?)
    - Societal (am I a bad person?)
  - What's the alternative?
    - If I practice abstinence, is that any better than helping people practice "safe AI"? 

- In data science (my background), correctness matters!
  - Design systems where humans can help "course correct" and "verify"
  - Posit assistant is an example of this
  - Plug my colleagues talk on "correctness, reproducibility, etc"


**LLMs: embrace the good, engineer around the bad (20 min)**

- LLM capabilities are jagged
  - Some "easy" tasks (e.g., counting r's in strawberry) they are terrible at, but some "hard" tasks (e.g., coding) they are awesome at!
  - Focus LLMs on what they're good at (language->code)
  - Engineer around the bad (i.e., provide a "harness" with tools, prompts, etc)
- Agent "harnesses" are becoming quite capable!
  - [What is an agent](https://tidydesign.substack.com/p/what-is-an-agent)?
    - An agent is an LLM, in a harness, that calls tools repeatedly in a loop, deciding each next step from the last result. 
    - Most agents have two types of tools: read tools that can observe the world, and write tools that can change the world. 
  - Claude Code, codex, etc
    - Has radically changed the way I work over last 6 months
  - YOLO mode: terrifying, but so useful!
    - Under right conditions it's viable, but where isn't it viable?
    - "Local dev" agents are very different from "hosted prod" agents
  - Hallucinations, sycophancy, and overconfidence is still an issue.
    - Context management is important!
    - Prime directive is important!
    - Safe execution is (sometimes) important!
    - How much "leash" are you willing to give the agent?
- Don't overthink it
  - You probably don't need: complex RAG, multi-agent, etc
  - Unless you have scale issues, agentic search of text files works quite well

**Querychat: a case study**

- Querychat: safe but capable "self-service analytics"
  - Restricted to SQL/ggsql execution
  - Verifiable/reproducible output
  - Missing/in-progress: a context layer
  - 


- Reinforce:
  - Q: What things is querychat doing to reinforce safe and verifiable?



**Break (5 min)**

**Programming with LLMs made easy via chatlas (60 min)**

- Basic usage (console, notebook, streaming, async, etc)
- User vs. system prompt
- Tool calling
  - Custom tools
  - Built-in tools (e.g., web fetch/search)
- Brief mention of other capabilities
  -  MCP, structured data, reasoning, evals, etc
- *Hands-on* (~15 min)
  - Tired: Modify this existing chatlas example to do XYZ
  - Wired: ask your favorite chatbot to "Create for me a chatlas Python app to do XYZ"


**Break (5 min)**

**Chatbots made easy with chatlas+shinychat (45 min)**

- Basic usage
  - Pass chatlas client directly to shinychat, get all the things!
  - Manually wire to support other backends (e.g., LangChain)
- Brief overview of shinychat features
  - File attachments, history, slash commands, etc.
- Custom tool displays
- Understand user activity via OTel
- *Hands-on* (~15 min)
  - Exercise to reinforce basics (custom tool/display)
  - Deploy a chatbot to Connect Cloud?


**Break (5 min)**

**Case study: querychat -- a self-service analytics platform (45 min)**

- Basic usage
  - Pass chatlas client and data source to querychat, get all the things!
  - Supports streamlit, dash, etc., but Shiny is best experience
- Built-in tools
  - Filter, query, and visualize
- Context management
  - Auto-generated vs user-supplied context
- Security benefits of code execution model
- *Hands-on* (~15 min)
  - Hook up querychat to your own data (or use some other source that we curate)
  - Add web search capabilities to the app
  - Add your own custom tool capabilities

**Recap and sendoff (10 min)**

- Reinforce how far we can get with context engineering and tools 
- Feedback survey 
