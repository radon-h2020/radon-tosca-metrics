import toscametrics.utils as utils
from toscametrics.classes.definitions.artifact  import ArtifactDefinition

class ArtifactsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ArtifactDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        artifacts = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'artifacts':
                values = kv[1]
                
                for d in values:
                    item = values[d]
                    artifact = self.parse(item)
                    if artifact is not None:
                        artifacts.append(artifact)

        return artifacts

    def parse(self, item):
        """ 
        Returns a ArtifactDefinition
        item -- a dictionary to parse.
        """ 

        if not isinstance(item, dict):
            return None
       
        try:
            return ArtifactDefinition(
                    type=item.get('type'),
                    file=item.get('file'),
                    description=item.get('description'),
                    repository=item.get('repository'),
                    artifactVersion=utils.toString(item.get('version')),
                    deployPath=item.get('deploy_path'),
                    checksum=item.get('checksum'),
                    checksumAlgorithm=item.get('checksum_algorithm'),
                    properties=item.get('properties')
            )
        except (TypeError, ValueError):
            return None