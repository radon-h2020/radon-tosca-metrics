from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getArtifacts
from toscametrics.general.loc import LOC
from toscametrics.general.etp import ETP

from io import StringIO

class NA(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of artifacts defined in a given .yaml file"""
    

    def _get_elements(self):
        '''Function which collects all the artifacts with their attributes in a list'''
        try:
            template = self.getyml
            artifacts = getArtifacts(template)

            arts = []
            for art in artifacts:
                if isinstance(art, list):
                    arts.extend(art)

                elif isinstance(art, dict):
                    arts.append(art)

                else:
                    continue

            return arts

        except (KeyError, AttributeError):
            return []    


    def count(self):
        '''Function which counts the number of artifacts within the whole script'''
        try:
            artifacts = self._get_elements()

            names = []
            for art in artifacts:
                names.extend(art.keys())
            unique_names = set(names)

            return len(unique_names)

        except AttributeError:
            return 0


    def relative(self):
        '''Count relative to the lines of code'''
        try:
            strio = StringIO(self.getStringIOobject)
            return self.count() / LOC(strio).count()

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0


    def entropy(self):
        '''Counts the entropy for the _get_elements blocks'''
        try:
            strio = StringIO(self.getStringIOobject)

            block = {}
            for element in self._get_elements():
                if isinstance(element, dict):
                    block.update(element)
            
            return ETP(strio).count(custom=block)

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0


# from io import StringIO

# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\SeaCloudsEU\SeaCloudsPlatform\Industry\splittednuro_adp-iaas.general'
# with open(path, 'r') as file:
#             general = file.read()
#             print(general)

# general = StringIO(general.expandtabs(2))
# metric = NA(general)

# print('NA count: ', metric.count())
# print(metric._get_elements())




