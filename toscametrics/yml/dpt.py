from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class DPT(BlueprintMetric):
    """ This class implements the metric 'Depth of Blueprint' in a TOSCA script. """
    def __depth(self, d, level=0):
        """ Measure the depth of a template. """
        if not d:
            return level

        if not isinstance(d, dict) and not type(d) == list:
            return level
        
        if type(d) == list:
            return max(self.__depth(k, level) for k in d)
        else:
            return max(self.__depth(d[k], level + 1) for k in d)

    def count(self):
        """ Return the depth of a blueprint. """
        return self.__depth(self.getyml)