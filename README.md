# Agent CLI

`agent-cli` is a collection of **_local-first_**, AI-powered command-line agents that run entirely on your machine.
It provides a suite of powerful tools for voice and text interaction, designed for privacy, offline capability, and seamless integration with system-wide hotkeys and workflows.

> [!IMPORTANT]
> **Local and Private by Design**
> All agents in this tool are designed to run **100% locally**.
> Your data, whether it's from your clipboard, microphone, or files, is never sent to any cloud API.
> This ensures your privacy and allows the tools to work completely offline.
> You can also optionally configure the agents to use OpenAI/Gemini services.

## Why I built this

I got tired of typing long prompts to LLMs. Speaking is faster, so I built this tool to transcribe my voice directly to the clipboard with a hotkey.

What it does:
- Voice transcription to clipboard with system-wide hotkeys (Cmd+Shift+R on macOS)
- Autocorrect any text from your clipboard
- Edit clipboard content with voice commands ("make this more formal")
- Runs locally - no internet required, your audio stays on your machine
- Works with any app that can copy/paste

I use it mostly for the `transcribe` function when working with LLMs. Being able to speak naturally means I can provide more context without the typing fatigue.

## Features

- **`autocorrect`**: Correct grammar and spelling in your text (e.g., from clipboard) using a local LLM with Ollama or OpenAI.
- **`transcribe`**: Transcribe audio from your microphone to text in your clipboard using a local Whisper model or OpenAI's Whisper API.
- **`speak`**: Convert text to speech using a local TTS engine or OpenAI's TTS API.
- **`voice-edit`**: A voice-powered clipboard assistant that edits text based on your spoken commands.
- **`assistant`**: A hands-free voice assistant that starts and stops recording based on a wake word.
- **`chat`**: A conversational AI agent with tool-calling capabilities.

## Quick Start

### Just want the CLI tool?

If you already have AI services running (or plan to use OpenAI), simply install:

```bash
# Using uv (recommended)
uv tool install agent-cli

# Using pip
pip install agent-cli
```

Then use it:
```bash
agent-cli autocorrect "this has an eror"
```

### Want automatic setup with everything?

We offer two ways to set up agent-cli with all services:

#### Option A: Using Shell Scripts (Traditional)

```bash
# 1. Clone the repository
git clone https://github.com/dasmrpmunna/Al-Native-CLI-Agent---Natural-Language

# 2. Run setup (installs all services + agent-cli)
./scripts/setup-macos.sh  # or setup-linux.sh

# 3. Start services
./scripts/start-all-services.sh

# 4. (Optional) Set up system-wide hotkeys
./scripts/setup-macos-hotkeys.sh  # or setup-linux-hotkeys.sh

# 5. Use it!
agent-cli autocorrect "this has an eror"
```

#### Option B: Using CLI Commands (New!)

```bash
# 1. Install agent-cli
uv tool install agent-cli

# 2. Install all required services
agent-cli install-services

# 3. Start all services
agent-cli start-services

# 4. (Optional) Set up system-wide hotkeys
agent-cli install-hotkeys

# 5. Use it!
agent-cli autocorrect "this has an eror"
```

The setup scripts automatically install:
- ✅ Package managers (Homebrew/uv) if needed
- ✅ All AI services (Ollama, Whisper, TTS, etc.)
- ✅ The `agent-cli` tool
- ✅ System dependencies
- ✅ Hotkey managers (if using hotkey scripts)

<details><summary><b><u>[ToC]</u></b> 📚</summary>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Installation](#installation)
  - [Option 1: CLI Tool Only](#option-1-cli-tool-only)
  - [Option 2: Automated Full Setup](#option-2-automated-full-setup)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Run the Setup Script](#step-2-run-the-setup-script)
    - [Step 3: Start All Services](#step-3-start-all-services)
    - [Step 4: Test Your Installation](#step-4-test-your-installation)
- [System Integration](#system-integration)
  - [macOS Hotkeys](#macos-hotkeys)
  - [Linux Hotkeys](#linux-hotkeys)
- [Prerequisites](#prerequisites)
  - [What You Need to Install Manually](#what-you-need-to-install-manually)
  - [What the Setup Scripts Install for You](#what-the-setup-scripts-install-for-you)
    - [Core Requirements (Auto-installed)](#core-requirements-auto-installed)
    - [AI Services (Auto-installed and configured)](#ai-services-auto-installed-and-configured)
    - [Alternative Cloud Services (Optional)](#alternative-cloud-services-optional)
    - [Alternative Local LLM Servers](#alternative-local-llm-servers)
- [Usage](#usage)
  - [Installation Commands](#installation-commands)
  - [Configuration](#configuration)
    - [Service Provider](#service-provider)
  - [`autocorrect`](#autocorrect)
  - [`transcribe`](#transcribe)
  - [`speak`](#speak)
  - [`voice-edit`](#voice-edit)
  - [`assistant`](#assistant)
  - [`chat`](#chat)
- [Development](#development)
  - [Running Tests](#running-tests)
  - [Pre-commit Hooks](#pre-commit-hooks)
- [Contributing](#contributing)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

</details>


## Installation

### Option 1: CLI Tool Only

If you already have AI services set up or plan to use cloud services (OpenAI/Gemini):

```bash
# Using uv (recommended)
uv tool install agent-cli

# Using pip
pip install agent-cli
```

### Option 2: Automated Full Setup

For a complete local setup with all AI services:

#### Step 1: Clone the Repository

```bash
git clone https://github.com/basnijholt/agent-cli.git
cd agent-cli
```

#### Step 2: Run the Setup Script

| Platform | Setup Command | What It Does | Detailed Guide |
|----------|---------------|--------------|----------------|
| **🍎 macOS** | `./scripts/setup-macos.sh` | Installs Homebrew (if needed), uv, Ollama, all services, and agent-cli | [macOS Guide](docs/installation/macos.md) |
| **🐧 Linux** | `./scripts/setup-linux.sh` | Installs uv, Ollama, all services, and agent-cli | [Linux Guide](docs/installation/linux.md) |
| **❄️ NixOS** | See guide → | Special instructions for NixOS | [NixOS Guide](docs/installation/nixos.md) |
| **🐳 Docker** | See guide → | Container-based setup (slower) | [Docker Guide](docs/installation/docker.md) |

#### Step 3: Start All Services

```bash
./scripts/start-all-services.sh
```

This launches all AI services in a single terminal session using Zellij.

#### Step 4: Test Your Installation

```bash
agent-cli autocorrect "this has an eror"
# Output: this has an error
```

> [!NOTE]
> The setup scripts handle everything automatically. For platform-specific details or troubleshooting, see the [installation guides](docs/installation/).

<details><summary><b>Development Installation</b></summary>

For contributing or development:

```bash
git clone https://github.com/basnijholt/agent-cli.git
cd agent-cli
uv sync
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

</details>

## System Integration

Want system-wide hotkeys? You'll need the repository for the setup scripts:

```bash
# If you haven't already cloned it
git clone https://github.com/basnijholt/agent-cli.git
cd agent-cli
```

### macOS Hotkeys

```bash
./scripts/setup-macos-hotkeys.sh
```

This script automatically:
- ✅ Installs Homebrew if not present
- ✅ Installs skhd (hotkey daemon) and terminal-notifier
- ✅ Configures these system-wide hotkeys:
  - **`Cmd+Shift+R`** - Toggle voice transcription
  - **`Cmd+Shift+A`** - Autocorrect clipboard text
  - **`Cmd+Shift+V`** - Voice edit clipboard text

> [!NOTE]
> After setup, you may need to grant Accessibility permissions to skhd in System Settings → Privacy & Security → Accessibility

### Linux Hotkeys

```bash
./scripts/setup-linux-hotkeys.sh
```

This script automatically:
- ✅ Installs notification tools if needed
- ✅ Provides configuration for your desktop environment
- ✅ Sets up these hotkeys:
  - **`Super+Shift+R`** - Toggle voice transcription
  - **`Super+Shift+A`** - Autocorrect clipboard text
  - **`Super+Shift+V`** - Voice edit clipboard text


<!-- OUTPUT:END -->

</details>

## Development

### Running Tests

The project uses `pytest` for testing. To run tests using `uv`:

```bash
uv run pytest
```

### Pre-commit Hooks

This project uses pre-commit hooks (ruff for linting and formatting, mypy for type checking) to maintain code quality. To set them up:

1. Install pre-commit:

   ```bash
   pip install pre-commit
   ```

2. Install the hooks:

   ```bash
   pre-commit install
   ```

   Now, the hooks will run automatically before each commit.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. If you'd like to contribute code, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
