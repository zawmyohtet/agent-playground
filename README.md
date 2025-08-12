### Agentic Application Development Environments 🚀

This repository provides a containerized development environment designed for building and experimenting with agentic applications. It includes two primary environments: one tailored for general agentic application development and another specifically for Model Context Protocol (MCP) server development. Both environments come pre-configured with essential packages to minimize setup time and help you get started quickly.

### Getting Started

Before you begin, please ensure you have Docker installed on your system.

1. Clone the Repository
First, clone this repository to your local machine:

```
git clone git@github.com:zawmyohtet/agent-playground.git
cd agent-playground
```

2. Start the Containers
To launch both development environments, execute the following command:

```
docker compose up -d
```

This command will start the containers in detached mode, running them in the background.

3. Check Container Status
You can verify that all services are running correctly using:

```
docker compose ps
```

#### Accessing the Environments

You can access the shell of each container independently to run commands, manage dependencies, and develop your applications.

For Jupyter:
```
docker compose exec jupyter bash
```

For MCP Server:
```
docker compose exec mcp-dev bash
```

### Using Jupyter Notebook 📊

The Jupyter Notebook interface is accessible directly from your web browser.

- URL: `http://localhost:8888`
- Default Token: `1234`

The work/ directory from your host machine is automatically mounted inside the Jupyter container. This allows you to seamlessly access and work with your project files. You can modify the default token and other configuration settings within the `docker-compose.yml` file.

### Using MCP Inspector 🕵️‍♀️

The Model Context Protocol (MCP) Inspector is a tool designed to monitor and visualize the interactions and data flow within MCP server. It helps in debugging and understanding how agents process and share information. A sample application demonstrating the MCP Inspector is located in the `work/mcp` directory.

Steps to Access:
1. Enter the MCP environment:

```
docker compose exec mcp-dev bash
```

2. Navigate to the sample application directory and run the command:

```
cd mcp/hello-world
HOST=0.0.0.0 ALLOWED_ORIGINS=http://0.0.0.0:6274,http://0.0.0.0:6277 DANGEROUSLY_OMIT_AUTH=false npx @modelcontextprotocol/inspector uv run character-count.py
```

3. Access the Inspector:

Open your web browser and navigate to `http://0.0.0.0:6274.`

Exposed Ports:
The environment exposes several ports by default, which can be adjusted in the docker-compose.yml file as needed for different protocols or applications:

- 8000
- 6274
- 5173
- 6277
- 3000

### Using ADK Web 🌐

Google ADK Web refers to the web interface for the Agent Development Kit (ADK). It provides a platform for building, testing, and deploying agentic applications developed with Google's tools and frameworks, offering a visual way to interact with and manage your agents. A sample application built with the Agent Development Kit (ADK) Web is provided in the `work/adk/sample` directory.

#### Steps to Access:
1. Enter the Jupyter environment:

```
docker compose exec jupyter bash
```

2. Set up the environment variables:

```
cd work/adk/sample
cp .env.example .env
```

**Important:** Be sure to set your `GOOGLE_API_KEY` in the newly created .env file for the sample application to function correctly.

3. Run the ADK web server:

```
cd ../ # Go back to the 'work/adk' directory
adk web --host=0.0.0.0
```

4. Access ADK Web:

The ADK web application will be available at `http://0.0.0.0:8000.`

### Using LangGraph Studio 🖼️
LangGraph Studio is a development environment for visualizing, debugging, and iterating on LangGraph applications. It allows developers to graphically inspect the state and flow of their LLM-powered applications, making it easier to build complex, multi-step agentic workflows. A sample application for LangGraph Studio is included in the work/langgraph directory.

#### Steps to Access:
1. Enter the Jupyter environment:

```
docker compose exec jupyter bash
```

2. Set up the environment variables:

```
cd work/langgraph/studio
cp .env.example .env
```

Adjust the environment variables within the `.env` file to suit your specific requirements.

4. Run LangGraph Studio:

```
langgraph dev --host=0.0.0.0
```

5. Access LangGraph Studio:

Open your web browser and navigate to `https://smith.langchain.com/studio/?baseUrl=http://0.0.0.0:2024`. You need to allow `Insecure content` from site setting to make it works properly. To work around this, run the above command with `--tunnel` to access Studio via a secure tunnel.

### Accessing Containers via VS Code Dev Containers 🚀

For an integrated development experience, you can use the VS Code Dev Containers extension to work directly within the Docker containers.

#### Steps:

1. Open VS Code.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
3. Typing "Dev Containers: Attach to running container...)
4. Select any container you want to attach

VS Code will now build (if necessary) and connect to the development container, allowing you to use its integrated terminal, installed tools, and extensions seamlessly within the containerized environment.