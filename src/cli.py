"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "square_root": square_root,
    "sqrt": square_root,
}

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """CLI calculator that performs basic operations."""
    func = OPERATIONS.get(operation)
    if func is None:
        click.echo(f"Unknown operation: {operation}")
        sys.exit(1)

    try:
        result = func(num1) if operation in ("square_root", "sqrt") else func(num1, num2)
    except ZeroDivisionError:
        click.echo("Cannot divide by zero")
        sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

    if result == int(result):
        click.echo(int(result))
    else:
        click.echo(f"{result:.2f}")


if __name__ == "__main__":
    calculate()