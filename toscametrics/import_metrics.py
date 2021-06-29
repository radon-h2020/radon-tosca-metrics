# General blueprint
from toscametrics.general.lines_blank import LinesBlank
from toscametrics.general.lines_comment import LinesComment
from toscametrics.general.lines_code import LinesCode
from toscametrics.general.num_keys import NumKeys
from toscametrics.general.num_suspicious_comments import NumSuspiciousComments
from toscametrics.general.num_tokens import NumTokens
from toscametrics.general.text_entropy import TextEntropy

# Blueprint blueprint
from toscametrics.blueprint.avg_workflow_size import AvgWorkflowSize
from toscametrics.blueprint.lcot import LCOT
from toscametrics.blueprint.num_artifact_types import NumArtifactTypes
from toscametrics.blueprint.num_capabilities import NumCapabilities
from toscametrics.blueprint.num_capability_types import NumCapabilityTypes
from toscametrics.blueprint.num_data_types import NumDataTypes
from toscametrics.blueprint.num_group_types import NumGroupTypes
from toscametrics.blueprint.num_imports import NumImports
from toscametrics.blueprint.num_inputs import NumInputs
from toscametrics.blueprint.num_interfaces import NumInterfaces
from toscametrics.blueprint.num_node_templates import NumNodeTemplates
from toscametrics.blueprint.num_node_types import NumNodeTypes
from toscametrics.blueprint.num_parameters import NumParameters
from toscametrics.blueprint.num_policy_types import NumPolicyTypes
from toscametrics.blueprint.num_properties import NumProperties
from toscametrics.blueprint.num_relationship_templates import NumRelationshipTemplates
from toscametrics.blueprint.num_relationship_types import NumRelationshipTypes
from toscametrics.blueprint.num_requirements import NumRequirements
from toscametrics.blueprint.num_shell_scripts import NumShellScripts
from toscametrics.blueprint.num_workflows import NumWorkflows

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
    'avg_workflow_size': AvgWorkflowSize,
    'lcot': LCOT,
    'num_artifact_types': NumArtifactTypes,
    'num_capabilities': NumCapabilities,
    'num_capability_types': NumCapabilityTypes,
    'num_data_types': NumDataTypes,
    'num_group_types': NumGroupTypes,
    'num_imports': NumImports,
    'num_inputs': NumInputs,
    'num_interfaces': NumInterfaces,
    'num_node_templates': NumNodeTemplates,
    'num_node_types': NumNodeTypes,
    'num_parameters': NumParameters,
    'num_policy_types': NumPolicyTypes,
    'num_properties': NumProperties,
    'num_relationship_templates': NumRelationshipTemplates,
    'num_relationship_types': NumRelationshipTypes,
    'num_requirements': NumRequirements,
    'num_shell_scripts': NumShellScripts,
    'num_workflows': NumWorkflows
}
