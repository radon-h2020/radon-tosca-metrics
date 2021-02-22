# General blueprint
from toscametrics.general.lines_blank import LinesBlank
from toscametrics.general.lines_comment import LinesComment
from toscametrics.general.lines_code import LinesCode
from toscametrics.general.num_keys import NumKeys
from toscametrics.general.num_suspicious_comments import NumSuspiciousComments
from toscametrics.general.num_tokens import NumTokens
from toscametrics.general.text_entropy import TextEntropy

# Blueprint blueprint
from toscametrics.blueprint.num_imports import NumImports
from toscametrics.blueprint.num_inputs import NumInputs
from toscametrics.blueprint.num_interfaces import NumInterfaces
from toscametrics.blueprint.num_node_templates import NumNodeTemplates
from toscametrics.blueprint.num_node_types import NumNodeTypes
from toscametrics.blueprint.num_parameters import NumParameters
from toscametrics.blueprint.num_properties import NumProperties
from toscametrics.blueprint.num_relationship_templates import NumRelationshipTemplates
from toscametrics.blueprint.num_relationship_types import NumRelationshipTypes
from toscametrics.blueprint.num_shell_scripts import NumShellScripts

general_metrics = {
    'lines_code': LinesCode,
    'lines_blank': LinesBlank,
    'lines_comment': LinesComment,
    'num_keys': NumKeys,
    'num_suspicious_comments': NumSuspiciousComments,
    'num_tokens': NumTokens,
    'text_entropy': TextEntropy,
}

blueprint_metrics = {
    'num_imports': NumImports,
    'num_inputs': NumInputs,
    'num_interfaces': NumInterfaces,
    'num_node_templates': NumNodeTemplates,
    'num_node_types': NumNodeTypes,
    'num_parameters': NumParameters,
    'num_properties': NumProperties,
    'num_relationship_templates': NumRelationshipTemplates,
    'num_relationship_types': NumRelationshipTypes,
    'num_shell_scripts': NumShellScripts
}
