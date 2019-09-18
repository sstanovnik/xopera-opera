from .constraint_clause import ConstraintClause
from .schema_definition import SchemaDefinition
from .status import Status
from ..bool import Bool
from ..entity import Entity
from ..list import List
from ..map import Map
from ..reference import DataTypeReference
from ..string import String
from ..void import Void


# TODO(@tadeboro): Unify ParameterDefinition and PropertyDefinition and add
# runtime checks. Refinement will be a PITA ...


class ParameterDefinition(Entity):
    ATTRS = dict(
        type=DataTypeReference("data_types"),
        description=String,
        required=Bool,
        default=Void,
        status=Status,
        constraints=List(ConstraintClause),
        key_schema=SchemaDefinition,
        entry_schema=SchemaDefinition,
        external_schema=String,
        metadata=Map(String),
        value=Void,
    )
