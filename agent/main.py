import os

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from langchain.agents import create_agent
from langchain_aws import ChatBedrockConverse

from tools import add, multiply, delete, list_saved

app = BedrockAgentCoreApp()

model = ChatBedrockConverse(
    model=os.environ.get("MODEL_ID", "us.anthropic.claude-sonnet-4-5-20250929-v1:0"),
    region_name=os.environ.get("AWS_REGION", "us-east-1"),
)

agent = create_agent(
    model=model,
    tools=[add, multiply, delete, list_saved],
    system_prompt=(
        "You are a calculator assistant. Use the tools to add and multiply "
        "numbers, save results by name, list them, and delete them. "
        "Never do arithmetic yourself."
    ),
)


@app.entrypoint
def invoke(payload: dict) -> dict:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": payload.get("prompt", "")}]}
    )
    return {"result": result["messages"][-1].text}


if __name__ == "__main__":
    app.run()
