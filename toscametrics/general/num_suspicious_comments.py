import re
from toscametrics.blueprint_metric import BlueprintMetric


class NumSuspiciousComments(BlueprintMetric):
    """ This class counts the number of suspicious comments in the blueprint"""

    def count(self):
        """ Return the number of suspicious comments in the script. """
        suspicious = 0

        for line in self.plain_blueprint.splitlines():
            comment = re.search(r'#.+', str(line.strip()))
            if comment is not None:
                if re.search(r'TODO|FIXME|HACK|XXX|CHECKME|DOCME|TESTME|PENDING', comment.group()) is not None:
                    suspicious += 1

        return suspicious
