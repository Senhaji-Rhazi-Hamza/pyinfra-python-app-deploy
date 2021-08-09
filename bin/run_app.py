import os
import click

from app.server import app


@click.command(name="run_app")
def run_app():
    app.run(
        debug=True, host="0.0.0.0", port=os.getenv('PORT', 8000)
        )


run_app_functions = [
  run_app
]
