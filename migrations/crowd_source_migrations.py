import os
from migrations import BaseConfigMigrationProvider
CROWD_SOURCE_DB_URI = os.getenv('CROWD_SOURCE_DB_URI')
CROWD_SOURCE_DB_NAME = os.getenv('CROWD_SOURCE_DB_NAME')

class CrowdSourceMigration(BaseConfigMigrationProvider):

    def _get_crowd_source_db_name(self):
        return os.getenv('CROWD_SOURCE_DB_NAME')

    def _get_crowd_source_db_uri(self):
        return os.getenv('CROWD_SOURCE_DB_URI')

    def _get_migration_db_name(self):
        return os.getenv('MIGRATION_DB_NAME')

    def _get_migration_db_uri(self):
        return os.getenv('MIGRATION_DB_URI')

    def get_migration_config(self):
        return {
            'STORES':[{
                    'name': self._get_crowd_source_db_name(),
                    'url': self._get_crowd_source_db_uri()
                },
                {
                    'name': self._get_migration_db_name(),
                    'url': self._get_migration_db_uri()
                }],
            'TASKS': [{
                    'from': [{'name': CROWD_SOURCE_DB_NAME}],
                    'to': {'name': self._get_migration_db_name()},
                    'orders':['address', 'actor']
            }],
        }
