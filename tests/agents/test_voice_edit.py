"""Tests for the voice assistant agent."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from agent_cli.cli import app

runner = CliRunner()


@patch("agent_cli.agents.voice_edit.asyncio.run")
def test_voice_edit_agent(mock_run: MagicMock) -> None:
    """Test the voice assistant agent."""
    result = runner.invoke(
        app,
        [
            "voice-edit",
            "--config",
            "missing.toml",
            "--llm-provider",
            "local",
            "--asr-provider",
            "local",
            "--tts-provider",
            "local",
            "--openai-api-key",
            "test",
        ],
    )
    assert result.exit_code == 0, result.output
    mock_run.assert_called_once()


@patch("agent_cli.agents.voice_edit.process.kill_process")
def test_voice_edit_stop(mock_kill_process: MagicMock) -> None:
    """Test the --stop flag."""
    mock_kill_process.return_value = True
    result = runner.invoke(app, ["voice-edit", "--stop"])
    assert result.exit_code == 0
    assert "Voice assistant stopped" in result.stdout
    mock_kill_process.assert_called_once_with("voice-edit")


@patch("agent_cli.agents.voice_edit.process.kill_process")
def test_voice_edit_stop_not_running(mock_kill_process: MagicMock) -> None:
    """Test the --stop flag when the process is not running."""
    mock_kill_process.return_value = False
    result = runner.invoke(app, ["voice-edit", "--stop"])
    assert result.exit_code == 0
    assert "No voice assistant is running" in result.stdout


@patch("agent_cli.agents.voice_edit.process.is_process_running")
def test_voice_edit_status_running(mock_is_process_running: MagicMock) -> None:
    """Test the --status flag when the process is running."""
    mock_is_process_running.return_value = True
    with patch(
        "agent_cli.agents.voice_edit.process.read_pid_file",
        return_value=123,
    ):
        result = runner.invoke(app, ["voice-edit", "--status"])
    assert result.exit_code == 0
    assert "Voice assistant is running" in result.stdout


@patch("agent_cli.agents.voice_edit.process.is_process_running")
def test_voice_edit_status_not_running(mock_is_process_running: MagicMock) -> None:
    """Test the --status flag when the process is not running."""
    mock_is_process_running.return_value = False
    result = runner.invoke(app, ["voice-edit", "--status"])
    assert result.exit_code == 0
    assert "Voice assistant is not running" in result.stdout
