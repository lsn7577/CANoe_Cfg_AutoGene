# Check of EDS and DCF Files

> Category: `DBC` | Subcategory: `Document` | Type: `concept`

The application allows to check EDS and DCF file in different ways.

## Check while file is read

When a file is read after a file open command few simple test are done to inform the user if faulty values can not be read.

## Compare objects with database objects

Single objects can be compared with the database. If a value differs the object is marked with the icon .

An object is compared with its database by selecting it in the EDS Window and start command Compare Database. An object is also compared after a value in the attribute window has changed and another object is selected.

All objects are compared with the selected database after a file is read.

## Check a file with CANchkEDS

The command Check EDS starts the big EDS check. All objects are checked according to the Electronic Data Sheet Specification for CANopen (CiA306) and test description for CANopen Devices (Appendix to CiA301 V4.0).

If the check detect an error the corresponding object is marked with the icon .
