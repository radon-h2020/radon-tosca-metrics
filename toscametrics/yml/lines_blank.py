from toscametrics.yml.loc import LOC

class BLOC(LOC):
    """ This class is responsible for providing the methods to count the blank lines of code (bloc) in a given .yaml file"""

    def count(self):
        bloc = 0

        for l in self.getyml().splitlines():            
            if not l.strip():
                bloc = bloc + 1

        return bloc