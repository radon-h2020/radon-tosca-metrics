from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList
from toscametrics.utils import getInputs

class NINP(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of inputs defined in a given .yaml file"""


    def _get_elements(self):
        '''Function which collects all the inputs with their attributes in a list'''
        try:
            template = self.getyml     
            inputs = getInputs(template)

            input_list = []
            for input in inputs:
                if isinstance(input, dict):
                    input_list.append(input)
                else:
                    continue
            return input_list

        except (KeyError, AttributeError):
            return []   

    def count(self):
        '''Function which counts the number of inputs in a given .yaml file'''
        try:
            input_list = self._get_elements()

            inputs = []
            for input in input_list:
                inputs.extend(input.keys())

            unique_inputs = set(inputs)
            return len(unique_inputs)
        
        except AttributeError:
            return 0


# from io import StringIO

# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB\n    \n    wordpress:\n      type: tosca.nodes.WebApplication.WordPress\n      interfaces:\n        Standard:\n          configure:\n            inputs:\n              wp_db_name: { get_property: [ mysql_database, name ] }\n                  \n#Combination of the nn,nnt_2_1 and section 4.4.2.3 example TOSCA simple profile v1.3'
# #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup:\n              implementation: backup.sh\n              inputs:\n                storage_url: { get_input: storage_url }\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          valid_states: [available]\n        - target: mysql\n          valid_states: [started, available]\n          attributes:\n            my_attribute: [ready]\n      inputs:\n        storage_url:\n          type: string\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup'
# #string = 'tosca_definitions_version: alien_dsl_2_0_0\n\n#\n# Ystia Forge\n# Copyright (C) 2018 Bull S. A. S. - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.\n#\n\nmetadata:\n  template_name: org.ystia.ssl.ansible.certificates\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\ndescription: Generate Certificates using Ansible\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - yorc-types:1.1.0\n\nnode_types:\n  org.ystia.ssl.ansible.certificates.nodes.SSLCertificateGenerator:\n    derived_from: tosca.nodes.SoftwareComponent\n    metadata:\n      icon: /icons/ssl-certificate.png\n    properties:\n      common_name:\n        type: string\n        description: Certificate common name\n      key_path:\n        type: string\n        description: Path of a directory where private keys should be stored.\n      certificate_path:\n        type: string\n        description: Path of a directory where certificates should be stored.\n      linux_owner:\n        type: string\n        description: >\n          Linux user that should be the owner of the certificates and keys. This user should have rights to write on\n          certificate_path and key_path. By default it is the user used to connect to the machine.\n        required: false\n        default: ""\n      key_name:\n        type: string\n        required: false\n        description: Name including extention of the private key file. By default it will be the node template within the topology + \'.key\'\n        default: ""\n      certificate_name:\n        type: string\n        required: false\n        description: Name including extention of the certificate file. By default it will be the node template within the topology + \'.pem\'\n        default: ""\n      private_key:\n        type: string\n        required: false\n        description: Content of a private key to use to generate the certificate\n        default: ""\n      extra_sub_alt_name:\n        type: string\n        required: false\n        default: ""\n        description: Optional coma separated list of subject alternative names (format is \'IP:<An IP Address>,DNS:<A DNS Name>\')\n      extended_key_usage:\n        type: list\n        entry_schema:\n          type: string\n        description: Additional restrictions (e.g. client authentication, server authentication) on the allowed purposes for which the public key may be used.\n        required: false\n        default: []\n      ca_key:\n        type: string\n        description: Private key of the Certificate Authority\n        # TODO make it optional by generating a CA if needed\n        required: true\n        #default: ""\n      ca_certificate:\n        type: string\n        description: Certificate Authority certificate\n        # TODO make it optional by generating a CA if needed\n        required: true\n        #default: ""\n      ca_passphrase:\n        type: string\n        description: Pass pharse for the Certificate Authority private key\n        default: ""\n        required: false\n    interfaces:\n      Standard:\n        create: playbooks/create.yml\n        configure:\n          inputs:\n            KEY_NAME: { get_property: [SELF, key_name] }\n            CERTIFICATE_NAME: { get_property: [SELF, certificate_name] }\n            KEY_PATH: { get_property: [SELF, key_path] }\n            CERTIFICATE_PATH: { get_property: [SELF, certificate_path] }\n            GEN_CERT_BECOME_USER: { get_property: [SELF, linux_owner] }\n            PRIVATE_KEY: { get_property: [SELF, private_key] }\n            EXTRA_SUB_ALT_NAME: { get_property: [SELF, extra_sub_alt_name] }\n            COMMON_NAME: { get_property: [SELF, common_name] }\n            CA_KEY: { get_property: [SELF, ca_key] }\n            CA_CERTIFICATE: { get_property: [SELF, ca_certificate] }\n            CA_PASSPHRASE: { get_property: [SELF, ca_passphrase] }\n            EXTENDED_KEY_USAGE: { get_property: [SELF, extended_key_usage]}\n            IP_ADDRESS: { get_attribute: [HOST, ip_address] }\n            PUBLIC_ADDRESS: { get_attribute: [HOST, public_address] }\n          implementation: playbooks/configure.yml\n        delete:\n          inputs:\n            KEY_NAME: { get_property: [SELF, key_name] }\n            CERTIFICATE_NAME: { get_property: [SELF, certificate_name] }\n            KEY_PATH: { get_property: [SELF, key_path] }\n            CERTIFICATE_PATH: { get_property: [SELF, certificate_path] }\n            GEN_CERT_BECOME_USER: { get_property: [SELF, linux_owner] }\n          implementation: playbooks/delete.yml\n\n\n  org.ystia.ssl.ansible.certificates.nodes.SSLRootCAInstaller:\n    derived_from: tosca.nodes.SoftwareComponent\n    metadata:\n      icon: /icons/ssl-certificate.png\n    properties:\n      certificate_authorities:\n        type: list\n        entry_schema:\n          type: string\n        description: Additional Root CA certificates to install, it should be the PEM-encoded certificate content.\n        required: true\n    interfaces:\n      Standard:\n        configure:\n          inputs:\n            CA_CERTS: { get_property: [SELF, certificate_authorities] }\n          implementation: playbooks/ca_installer/configure.yaml'

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NINP(yml)


# print('NINP count: ', metric.count())

# #metric._get_elements()
