from opera.parser.yaml.node import Node

from ..entity import Entity
from ..list import List
from ..map import Map
from ..string import String
from ..void import Void

from .operation_implementation_definition import (
    OperationImplementationDefinition,
)
from .parameter_definition import ParameterDefinition


class OperationDefinitionForType(Entity):
    ATTRS = dict(
        description=String,
        implementation=OperationImplementationDefinition,
        inputs=Map(ParameterDefinition),
        outputs=Map(List(Void)),
    )

    @classmethod
    def normalize(cls, yaml_node):
        if not isinstance(yaml_node.value, (str, dict)):
            cls.abort("Expected string or map.", yaml_node.loc)
        if isinstance(yaml_node.value, str):
            return Node({Node("implementation"): yaml_node})
        return yaml_node
