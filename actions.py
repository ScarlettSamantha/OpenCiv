import argparse
import os
import glob
import sys
from typing import Any

# This is to make sure it can still finds its references.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class MaintenanceActions:
    def __init__(self):
        pass

    def remove_logs(self, **kwargs: Any) -> None:
        """Remove all .log files from specified directories."""
        directories = ["logs/debug", "logs/engine", "logs/gameplay", "logs/graphics", "logs/misc", "logs/ursina"]

        for directory in directories:
            log_files = glob.glob(os.path.join(directory, "*.log"))
            for log_file in log_files:
                try:
                    os.remove(log_file)
                    print(f"Removed {log_file}")
                except Exception as e:
                    print(f"Failed to remove {log_file}: {e}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Maintenance actions script")
    parser.add_argument("function_name", type=str, help="The name of the function to call")
    known_args, unknown_args = parser.parse_known_args()

    kwargs = {}
    for arg in unknown_args:
        if arg.startswith("--"):
            key, value = arg.split("=")
            key = key.lstrip("--")
            kwargs[key] = value

    return known_args, kwargs


def main() -> None:
    known_args, kwargs = parse_args()
    action_name = known_args.function_name

    actions = MaintenanceActions()
    if hasattr(actions, action_name):
        method = getattr(actions, action_name)
        method(**kwargs)
    else:
        print(f"Function {action_name} not found.")


if __name__ == "__main__":
    main()
