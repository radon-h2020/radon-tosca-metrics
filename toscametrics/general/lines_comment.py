import re

from toscametrics.general.lines_code import LinesCode


class LinesComment(LinesCode):
    """ This class counts the blueprint's commented lines"""

    def count(self):
        cloc = 0

        for l in self.blueprint.splitlines():
            comment = re.search(r'#[\s\w\W]+', str(l.strip()))
            if comment is not None:   
                cloc = cloc + 1

        return cloc
