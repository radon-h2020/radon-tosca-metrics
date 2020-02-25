import unittest

from toscametrics.classes.definitions.artifact import ArtifactDefinition
from toscametrics.parser.artifacts_parser      import ArtifactsParser

class TestArtifactsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ArtifactsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ArtifactsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"description": "Image for virtual machine", "type": "tosca.artifacts.Deployment.Image.VM", "file": "http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2", "checksum": "ba411cafee2f0f702572369da0b765e2", "version": 3.2, "checksum_algorithm": "MD5", "properties": { "name": "vSRX", "container_format": "BARE", "disk_format": "QCOW2", "min_disk": "1 GB", "size": "649 MB"}}
        parser = ArtifactsParser()
        actual = parser.parse(input)
        expected = ArtifactDefinition(
            type='tosca.artifacts.Deployment.Image.VM',
            file='http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2',
            description='Image for virtual machine',
            artifactVersion='3.2',
            checksum='ba411cafee2f0f702572369da0b765e2',
            checksumAlgorithm='MD5',
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '1 GB',
                        'size': '649 MB'
            }
        )
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()