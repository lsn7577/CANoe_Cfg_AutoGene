# Option EDS to XDD

> Category: `DBC` | Subcategory: `windows` | Type: `concept`

## Export EDS/DCF to XDD/XDC

If the check box Create parameters for manufacturer and profile dependent objects is activated, parameters for objects with index>1FFFh (if it not already refers to an existing parameter) are created. Parameters describe CANopen objects more comprehensive. Parameters can be referenced by other elements of XDD/XDC files also.

If the object is structured, parameters are created for sub objects with sub index>0 only. If the object has a profile or device specific data type, no parameter is created for this object.
