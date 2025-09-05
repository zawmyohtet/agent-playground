from langchain_ollama import ChatOllama
import langchain
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from IPython.display import Image, display
langchain.debug = False

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
    base_url="http://host.docker.internal:11434"
)

def count_character(input: str, char: str) -> int:
    """
    Return the character count of a string
    Example:
    Question: How many 'r' in 'Strawberry'
    Answer: 3
    
    Args:
        input: input string
        char: character to count from a input string
    """
    return input.count(char)

tools = [count_character]
llm_with_tools = llm.bind_tools(tools)

# Create a system message that sets the assistant's role and behavior
sys_message = SystemMessage(content="You are a helpful assistant that can count character from a word")

def agent(state: MessagesState):
    """
    Process the current message state by invoking the language model with tools.

    Args:
        state (MessagesState): The current state containing a list of messages.

    Returns:
        dict: A dictionary containing the updated list of messages after processing.
    """
    # Combine the system message with the current messages and invoke the language model with tools
    return {"messages": [llm_with_tools.invoke([sys_message] + state["messages"])]}


# Initialize a StateGraph builder with the MessagesState as the state container
builder = StateGraph(MessagesState)

# Add a node named "agent" linked to the agent function
builder.add_node("agent", agent)

# Add a node named "tools" that wraps the tools using ToolNode
builder.add_node("tools", ToolNode(tools))

# Add an edge from the START node to the "agent" node
builder.add_edge(START, "agent")

# Add conditional edges from "agent" node based on tools_condition function
builder.add_conditional_edges(
    "agent",
    tools_condition,
)

# Add an edge from the "tools" node back to the "agent" node
builder.add_edge("tools", "agent")

# Compile the state graph into a runnable graph object
graph = builder.compile()