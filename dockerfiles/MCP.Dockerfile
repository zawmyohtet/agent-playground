# =================================
# Python MCP Server Image
# =================================
FROM python:3.13

RUN apt-get install curl

# Set working directory
WORKDIR /workspace

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python MCP SDK and development tools
RUN pip install --no-cache-dir \
    mcp \
    "mcp[cli]" \
    fastapi \
    uvicorn \
    websockets \
    pydantic \
    python-dotenv \
    pytest \
    black \
    flake8 \
    uv \
    fastmcp

# Install Node.js (Latest LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install essential Node.js packages globally
RUN npm install -g \
    npm@latest \
    yarn \
    pnpm \
    typescript \
    ts-node \
    nodemon \
    eslint \
    prettier \
    @types/node \
    npx

# Expose development port
EXPOSE 8000