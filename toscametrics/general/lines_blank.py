from toscametrics.general.lines_code import LinesCode


class LinesBlank(LinesCode):
    """ This class counts the blank lines in a blueprint"""

    def count(self):
        bloc = 0

        for l in self.blueprint.splitlines():
            if not l.strip():
                bloc = bloc + 1

        return bloc
