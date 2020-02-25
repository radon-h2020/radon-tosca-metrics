import re

class VersionType():

    def __init__(self, version):
        self.fix = None
        self.qualifier = None
        self.build = None

        version = re.findall(r'(\d+)(\.\d+)(\.?\d+)*(\.?\w+)*(-?\d+)*', version)
        
        if len(version) == 0:
            raise ValueError('Version must be major.minor.<fix>.<qualifier>-<build>')

        self.major = int(version[0][0])
        self.minor = int(str(version[0][1].replace('.','')))
        
        fix = version[0][2].replace('.','')
        if fix is not None and fix != '':
            self.fix = int(fix)
        
        self.qualifier = version[0][3].replace('.','')

        build = version[0][4].replace('-','')
        if build is not None and build != '':
            self.build = int(build)
        

    @property
    def major(self): 
        return self.__major

    @major.setter
    def major(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError('Major version must be an integer')

        if value < 0:
            raise ValueError('Major version must be an integer greater than or equal to 0')

        self.__major = value

    @property
    def minor(self): 
        return self.__minor

    @minor.setter
    def minor(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError('Minor version must be an integer')

        if value < 0:
            raise ValueError('Minor version must be an integer greater than or equal to 0')

        self.__minor = value

    @property
    def fix(self): 
        return self.__fix

    @fix.setter
    def fix(self, value):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError('Fix version must be an integer')

            if value < 0:
                raise ValueError('Fix version must be an integer greater than or equal to 0')

        self.__fix = value

    @property
    def build(self): 
        return self.__build

    @build.setter
    def build(self, value):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError('Build version must be an integer')

            if value < 0:
                raise ValueError('Build version must be an integer greater than or equal to 0')

        self.__build = value
        
    @property
    def qualifier(self): 
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, value):
        if value is not None and not isinstance(value, str):
                raise TypeError('Qualifier must be a string')
                
        self.__qualifier = value


    def __eq__(self, other):
        if isinstance(other, VersionType):
            return (self.major     == other.major and 
                    self.minor     == other.minor and
                    self.qualifier == other.qualifier and
                    self.build     == other.build
                )

        return False

    def __repr__(self):
        return '({}.{}.{}.{}-{})'.format(self.major, self.minor, self.fix, self.qualifier, self.build)