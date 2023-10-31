from flask.cli import AppGroup
from .users import seed_users, undo_users
from .fighters import seed_fighters, undo_fighters
from .medals import seed_medals, undo_medals
from .teams import seed_teams, undo_teams
from .tour_result import seed_tour_results, undo_tour_results
from .season_result import seed_season_results, undo_season_results
from .team_results import seed_team_results, undo_team_results
from .schedule import seed_all_schedule, undo_schedule


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_fighters()
        undo_teams()
        undo_tour_results()
        undo_season_results()
        undo_schedule
    seed_users()
    seed_fighters()
    seed_teams()
    seed_medals()
    seed_tour_results()
    seed_season_results()
    seed_team_results()
    seed_all_schedule()
    print('everything has been seeded!')
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_fighters()
    undo_teams()
    undo_medals()
    undo_tour_results()
    undo_season_results()
    undo_team_results()
    undo_schedule()
    # Add other undo functions here
