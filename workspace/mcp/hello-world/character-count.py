from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("character-count", stateless_http=True)

# Add an addition tool
@mcp.tool()
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
    return input.lower().count(char.lower())

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')