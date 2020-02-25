import re

from toscametrics.yml.loc import LOC

class CLOC(LOC):
    """ This class is responsible for providing the methods to count the comments lines of code (cloc) in a given .yaml file"""

    def count(self):
        cloc = 0

        for l in self.getyml().splitlines():            
            comment = re.search(r'#[\s\w\W]+', str(l.strip()))
            if comment is not None:   
                cloc = cloc + 1

        return cloc