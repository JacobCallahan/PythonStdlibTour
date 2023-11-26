"""ChainMaps are a way to combine multiple dictionaries into a single dictionary-like object"""
import argparse
from collections import ChainMap
import os

static_file_settings = {"host": "localhost", "port": 8080, "debug": False}

# Environment variable settings
env_var_settings = {
    "host": os.environ.get("APP_HOST"),
    "port": os.environ.get("APP_PORT"),
    "debug": os.environ.get("APP_DEBUG"),
}
# Remove any environment variables that are missing
env_var_settings = {k: v for k, v in env_var_settings.items() if v is not None}

# Command-line argument settings
parser = argparse.ArgumentParser(description="Command-line application with settings.")
parser.add_argument("--host", help="Host address")
parser.add_argument("--port", type=int, help="Port number")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
cmd_line_args = vars(parser.parse_args())
# Remove any command-line arguments that are missing
cmd_line_args = {k: v for k, v in cmd_line_args.items() if v is not None}

# Combine dictionaries using ChainMap
combined_settings = ChainMap(cmd_line_args, env_var_settings, static_file_settings)

# Accessing command-line application settings
print("Settings:")
print(f"Host: {combined_settings['host']}")
print(f"Port: {combined_settings['port']}")
print(f"Debug Mode: {combined_settings['debug']}")
