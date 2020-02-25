import unittest

from toscametrics.classes.definitions.artifact   import ArtifactDefinition

class TestArtifactEq(unittest.TestCase):

    def testEqual(self):
        a1 = ArtifactDefinition(
            type='tosca.artifacts.Deployment.Image.VM',
            file='http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2',
            description='Image for virtual machine',
            deployPath='deploy/path',
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

        a2 = ArtifactDefinition(
            type='tosca.artifacts.Deployment.Image.VM',
            file='http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured.qcow2',
            description='Image for virtual machine',
            deployPath='deploy/path',
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

        self.assertEqual(a1, a2, 'Test failed because expected equality but actual is \'not equal\'!') 


 

    def testNotEqual(self):
        a1 = ArtifactDefinition(
            type='tosca.artifacts.Deployment.Image.VM',
            file='http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured1.qcow2',
            description='Image for virtual machine',
            artifactVersion='3.0',
            checksum='ba411cafee2f0f702572369da0b765e2',
            checksumAlgorithm='MD5',
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '1 GB',
                        'size': '649 MB'
            }
        )

        a2 = ArtifactDefinition(
            type='tosca.artifacts.Deployment.Image.VM',
            file='http://10.10.86.141/images/Juniper_vSRX_15.1x49_D80_preconfigured2.qcow2',
            description='Image for virtual machine',
            artifactVersion='3.2',
            checksum='ba411cafee2f0f702572369da0b765e2',
            checksumAlgorithm='SHA',
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '2 GB',
                        'size': '750 MB'
            }
        )

        self.assertNotEqual(a1, a2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()