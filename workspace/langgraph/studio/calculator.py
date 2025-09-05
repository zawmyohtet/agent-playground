from langchain_ollama import ChatOllama
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    base_url="http://host.docker.internal:11434"
)

def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

def add(a: int, b: int) -> int:
    """Add a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

tools = [add, multiply, divide]

llm_with_tools = llm.bind_tools(tools)

sys_message = SystemMessage(content="You are a helpful assistant that can multiply, add, and divide numbers.")

def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_message] + state["messages"])]}

sys_message_2 = SystemMessage(content="You are a helpful assistant which can explain the context. Plz write a summary in professonal tone")

def summary(state: MessagesState):
    return {"messages": [llm.invoke([sys_message_2] + state["messages"])]}

builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_node("summary", summary)

builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
builder.add_edge("tools", "assistant")

def should_call_tools(state: MessagesState) -> str:
    last_message = state["messages"][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "call_tools"
    return "process_data"

builder.add_conditional_edges(
    "assistant",
    should_call_tools,
    {
        "call_tools": "tools",
        "process_data": "summary"
    }
)

builder.add_edge("summary", END)

graph = builder.compile()