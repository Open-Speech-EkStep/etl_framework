import carry
import argparse

from migrations import get_migration_objects
from migrations.constants import Migrations

migration_list = [migration.value for migration in Migrations]

parser = argparse.ArgumentParser(
    description='Util for running ETL migrations for ekstep')

parser.add_argument('-m', '--migration', required=True, help='Name of the migration to run', choices=migration_list, dest='migration')
processor_args = parser.parse_args()


def run_migration(migration_name):
    migration_objs = get_migration_objects()
    migration_obj = migration_objs.get(migration_name)
    carry.run(migration_obj.get_migration_config())


if __name__ == '__main__':
    run_migration(processor_args.migration)

