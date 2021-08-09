import click

from bin.run_app import run_app_functions

flatten = lambda list_of_list: [item for mylist in list_of_list for item in mylist]

CMD_FUNCTIONS = flatten([run_app_functions])

# Please see more refs on how click works  https://click.palletsprojects.com/en/7.x/
@click.group(chain=True)
def app():
    """Command line entry, choose from the commands listed below"""


def build_command():
    for fn in CMD_FUNCTIONS:
        app.add_command(fn)


if __name__ == "__main__":
    build_command()
    app()
