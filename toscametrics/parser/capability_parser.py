from toscametrics.classes.definitions.attribute  import AttributeDefinition 
from toscametrics.classes.definitions.capability import CapabilityDefinition 
from toscametrics.classes.definitions.property   import PropertyDefinition 
from toscametrics.parser.attributes_parser       import AttributesParser 
from toscametrics.parser.properties_parser       import PropertiesParser 

class CapabilityParser():

    def parse(self, d):
        """ 
        Returns a CapabilityDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        ap = AttributesParser()
        pp = PropertiesParser()

        try:

            properties = d.get('properties')
            attributes = d.get('attributes')
            
            properties_dict = {}
            attributes_dict = {}

            if properties is not None:
                for k in properties:
                    properties_dict[k] = pp.parse(properties[k])

            if attributes is not None:
                for k in attributes:
                    attributes_dict[k] = ap.parse(attributes[k])

            if not bool(properties_dict):   # bool(dict) = False if dict is empty
                properties_dict = None

            if not bool(attributes_dict):   # bool(dict) = False if dict is empty
                attributes_dict = None

            return CapabilityDefinition(
                type=d.get('type'),
                description=d.get('description'),
                properties=properties_dict,
                attributes=attributes_dict,
                validSourceTypes=d.get('valid_source_types'),
                occurrences=d.get('occurrences')
            )

        except Exception:
            return None