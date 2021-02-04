from abc import ABC, abstractmethod
from migrations.constants import Migrations


class BaseConfigMigrationProvider(ABC):

    @abstractmethod
    def get_migration_config(self):
        pass



def get_migration_objects():
    from migrations.crowd_source_migrations import CrowdSourceMigration


    migration_dict = {}

    migration_dict[Migrations.CROWDSOURCE.value] = CrowdSourceMigration()
    return migration_dict


