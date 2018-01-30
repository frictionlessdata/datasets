This data package contains data for testing "string" formats ("default", "email" and "uri") according to specs provided here https://frictionlessdata.io/specs/table-schema/#string.

You should expect following errors when validating data against the schema in datapackage.json:

* "default" field values cannot be empty as it has "required" constraint
* "email" field value in row 3 is not an email
* "uri" field value in row 3 is not a URI
