from sqlalchemy.orm import registry

from noxer.infrastructure.database.tables import metadata

mapper_registry = registry(metadata=metadata)
