# Number of Parameters 

## Description

Returns the number of inputs within a blueprint's interface. 


---

## Example
The following interface has **5 parameters**, namely `db_host`, `db_port`, `db_name`, `db_user`, `db_password`.


``` yaml
inputs:
  db_host: { get_attribute: [ db_server, private_address ] }
  db_port: { get_property: [ mysql, port ] }
  db_name: { get_property: [ wordpress_db, name ] }
  db_user: { get_property: [ wordpress_db, user ] }
  db_password: { get_property: [ wordpress_db, password ] }
```

---


## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of parameters |
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_parameters import NumParameters

str = 'inputs:\n\tdb_host: { get_attribute: [ db_server, private_address ] }\n\tdb_port: { get_property: [ mysql, port ] }\n\tdb_name: { get_property: [ wordpress_db, name ] }\n\tdb_user: { get_property: [ wordpress_db, user ] }\n\tdb_password: { get_property: [ wordpress_db, password ] }'
interface = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of parameters: ' + str(NumParameters(interface).count()))

>>> Number of parameters: 5
```