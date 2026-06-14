# Errors (CANchkEDS)

> Category: `DBC` | Subcategory: `messages` | Type: `concept`

error 1

Section [...] not found.

Section doesn’t exist in the EDS because section name has wrong spelling or doesn’t exist.

error 2

Incorrect brackets in section [...].

Section has no or incorrect enclosing brackets. E.g.:

or

error 3

Illegal position of section name [...].

Left bracket of a section isn’t in the leftmost column.

error 4

Duplicate section [...].

Two or more sections in the EDS have the same section name. E.g.:

An error is produced because two identical sections exist. Here the function reading the EDS overwrite value '1004' of the entry with value '1007'. This could produce additional confusing errors.

error 5

Insufficient entries in section [...].

Value in the first entry is bigger than number of following entries. E.g.:

error 6

Insufficient sub objects in main section [...].

Number of sub objects in the main object is bigger than number of following sub objects. E.g.:

Section [1004sub1] is missing.

error 7

Link [...] related to non-existent object.

Linked section related to non-existent object. E.g.:

Object [0001] doesn't exist.

error 8

Access type in section [...] contradicts direction of PDO section [...].

Access type contradicts direction of the PDO section. An object mapped to a transmitting PDO could have access type RO, CONST or RWR. An object mapped to a receiving PDO could have access type WO or RWW. Access type RWW and RWR is used for objects that can be read and written via SDO but can be mapped only in one type of PDO. E.g.:

Object mapped to the receive PDO shall have access type WO or RWW.

error 9

Mandatory section [...] not found.

An object in the database is marked as mandatory but it doesn't exist in the EDS.

error 10

Index in section [...] appears also in section [...].

Index in a fixed module section appears also in another non-module section. E.g.:

Module section has same index 6000.

error 11

Mapping parameter section [...] shall have no gaps in the sub object list.

A mapping parameter section shall have no gaps in the sub object list. E.g.:

If section [1600] has two sub objects, the sub objects must have sub index 0 and 1.

error 12

Section name [...] has an illegal character (e.g. leading 0 or 0x is not allowed).

Section name has an illegal character. Note that a leading 0x and leading 0 are not allowed for index and sub index. Whitespaces are not allowed too. E.g.:

error 13

Object ... linked in section [...] does not exist.

A link points to an section which doesn't exist. E.g.:

If object [10] does not exist, this error is generated.

error 14

Section ... of structured object [...] not found.

Sub object 0 of a structured object is missing. E.g.:

Structured object has no sub objects. But sub object 0 is mandatory, e.g.:

Structured object has a sub object. But sub object 0 is missing.

error 21

Illegal format of entry ... in section [...].

Value in entry has an illegal format. E.g.:

Subnumber=1X

Value is no numerical number, so it can't be evaluated.

Subnumber=5

DefaultValue=018

The leading zero describes an octal number. But value is no octal number because octal numbers does not contain single numbers bigger than 7.

DefaultValue=020

OrderCode=

If an entry is mandatory a value has to be declared.

OrderCode=0x7

error 22

Value in entry ... in section [...] is outside of valid area.

Value in entry is out of specific value range. E.g.:

Value area of entry Subnumber is Unsigned8 and its value range is [0..255].

error 23

Too many character in entry ... in section [...].

Value in entry has too much characters. Number of characters of key name plus number of characters of value have to be less than 255. E.g.:

error 24

Unknown entry ... in section [...].

Unknown entry in an info section.

error 25

Duplicate entry ... in section [...].

Two or more entries in a section has the same key name.

error 26

Entry ... in section [...] not found.

Mandatory entry doesn’t exist in specific section.

error 27

Entry ... in section [...] is not allowed.

Entry is not allowed in specific section. Some object types do not support particular entries e.g. objects of type VAR must not have an entry Subnumber.

error 28

Value in entry ... in section [...] is outside of valid object area.

Object value in an entry is out of specific value range. E.g.:

This index is outside of the valid index range for optional objects.

error 29

Illegal value in entry ...in section [...].

Value of an entry has wrong format or there is no value although the entry is mandatory.

error 30

Value in entry ... in section [...] is not equal to database (...).

Value of an entry in the EDS differs from the value in the accompanying database entry. In the last brackets the possible correct values are shown.

error 31

Complex data type in entry ... in section [...] is not allowed.

A predefined complex data type of object type DEFSTRUCT should not exist in an EDS.

error 32

Data type in entry ... in section [...] is reserved.

A reserved index pointing to a data type should not exist in an EDS.

error 33

Database requires description of sub objects in section [...].

If the data base defines a minimal number of elements, a description of sub objects is needed (Subnumber=... or CompactSubObj=...).

error 34

Description of sub objects in section [...] is missing.

Object type is ARRAY, RECORD or DEFSTRUCT but object has no description of sub objects. In the last brackets the possible correct values are shown. E.g.:

error 35

Mapped object [...] shall have value 1 in entry PDOMapping.

The object is mapped but value of entry PDOMapping is 0. E.g.:

Object is mapped but has mapping is not allowed.

error 36

Value in entry DefaultValue in section [...] is not identical to number of last sub object.

The value of DefaultValue is unequal the highest sub index implemented for this object. E.g.:

Default value in section [1026sub0] has to be 4.

error 37

Duplicate index in entry ... in section [...].

Index in a section is multiple used. E.g.:

Index 1003 is multiple used.

error 38

Maximal number of sub objects of section [...] is smaller in database (...).

Value of entry SubNumber is bigger than number of entry MaxElements in the database. E.g.:

Number of entry MaxElements in database is 4.

error 39

Minimal number of sub objects in section [...] is bigger in database (...).

Value of entry SubNumber is less than number of entry MinElements in the database. In the last brackets the possible correct values are shown. E.g.:

Number of entry MinElements in database is 4.

error 40

Entry ... in section [...] has no corresponding sub object.

An entry in a name section has no corresponding sub object. E.g.:

Only sub object 0 and 1 are defined. So a name for the unknown entry 2 is not correct.

error 41

Entry EDSVersion in section [FileInfo] missing or value<4.0.

The check relates to EDS files of version 4.0 or higher.

error 42

Data type of section […] differs from other data types in the array

The sub objects of an array must have the same data type. Otherwise this error is reported. E.g.:

Data types of [1003sub1] and [1003sub2] are different.

error 51

Module description ... points to fixed and extended objects too.

A module description points to fixed and extension objects too. E.g.:

It is not allowed to define fixed and extended objects for the same index (here:1).

error 52

Fixed or extended object description [...] not found.

A fixed or extension module description is expected but not found. E.g.:

Section [M1FixedObjects] or [M1SubExtends] is missing.

error 53

Multiple used object [...] differs in entry ....

If several modules contain the same fixed objects, their attributes shall be equal. E.g.:

The same fixed object has different data types.

error 54

Module list [1027] is missing.

If the section [SupportedModules] exist, object [1027] shall exist too.

error 55

Module list [1027] is redundant.

If the object [1027] exist, section [SupportedModules] shall exist too.

error 61

There is no suitable PDO for section [...].

If no RxPDO or no TxPDO exists, an object with entry ‘PDOMapping=1’ only shall have corresponding access types. E.g.:

For these attributes there is no PDO available.

error 62

Number in entry ... in section [DeviceInfo] differs from number of supported PDOs.

If no compact PDOs exist, the number of PDOs given in section [DeviceInfo] differs from the number of existing PDOs. E.g.:

An PDO exists although NrOfTXPDO is null.

error 63

Mapped object ... does not exist.

A mapped object doesn’t exist in the EDS file. E.g.:

If mapped section [6200sub1] doesn't exist, these error is reported.

error 64

Total length of mapped objects in section […] is bigger than 8 Byte.

The total length of mapped objects is bigger than 8 byte. E.g.:

Total length of 65 Bits is too big.

error 65

Object length in section […] doesn't match data type of mapped object.

The object length doesn't match data type of mapped object. E.g.:

The data type of mapped object is Unsigned32 and object length in the mapping parameter is 64 bit.

error 66

Data type in section […] is not mappable.

The given data type is not mappable but object is mapped. E.g.:

The data type Visible String is not mappable.

error 67

Access type in section […] is writable although sub object 0 is constant or read-only.

For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. If the access type of sub-index 0 of a PDO mapping parameter object is constant or read-only no variable mapping is supported and therefore the access type of further sub-indexes have to be constant or read-only. E.g.:

The access type have to be CONST or RO because object does not support variable mapping.

error 68

Access type in section […] is constant or read-only although sub object 0 writable.

For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. If the access type of sub-index 0 of a PDO mapping parameter object is writable then variable mapping is supported and therefore the access type of further sub-indexes have to be writable too. E.g.:

DAccess type have to be writable too.

error 69

Entry Granularity in section [DeviceInfo] has to be 0 because all PDOs support constant mapping.

No PDO parameter object supports variable mapping. Therefore the granularity has to be 0. E.g.:

Granularity has to be 0 because mapping is not modifiable.

Note

This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly.

error 70

Entry Granularity in section [DeviceInfo] has to be bigger than 0 because all PDOs support variable mapping.

All PDO parameter objects supports variable mapping. Therefore the granularity has to be bigger than 0. E.g.:

Granularity has to be bigger than 0 because mapping is modifiable.

error 71

Number of Rx/TxPDOs in entry DefaultValue in section [1004sub0] differs from number of Rx/TxPDOs in section [DeviceInfo].

In object 0x1004 the default value of sub index 0 describes the overall number PDOs supported. This value has to be equal to the number of PDOs in section [DeviceInfo]. E.g.:

The LSB of the default value defines the number of TxPDOs and the MSB defines the number of RxPDOs. Therefore the correct value must be 0x30002. All sub-indexes of PDO mapping parameter objects access type is RO or CONST.

error 72

Number of Rx/TxPDOs in entry DefaultValue in section [1004subX] is bigger than number of Rx/TxPDOs in section [DeviceInfo].

In object 0x1004 the default value of sub index 1 describes the number of synchronous PDOs and sub index 2 the number of asynchrony PDOs. These values have to be smaller or equal to the number of PDOs in section [DeviceInfo]. E.g.:

The LSB of the default value defines the number of synchronous TxPDOs and the MSB defines the number of asynchronous RxPDOs. Therefore the correct value must be 0x10002, 0x10001, 0x10000, 2, 1 or 0.

error 73

Entry GroupMessaging in section [DeviceInfo] has to be set to 1 because there are multiplexed PDOs.

There are multiplexed PDOs (MPDOs) in the object dictionary. Therefore entry GroupMessaging has to be set to 1. E.g.:

If the default value of sub object 0 of a PDO mapping parameter is 254 or 255 then this PDO is a multiplexed PDO.

error 74

Invalid use of dummy mapping in TxPDO section […].

Dummy mapping is used in a TxPDO. E.g.:

It is not allowed to use dummy mapping in a TxPDO.

error 75

Object length in section […] is smaller than granularity.

The length of a mapped object is smaller than the granularity of the device. E.g.:

Granularity is 64 but a object with data type UNSIGNED32 is mapped.

error 76

Length of selected dummy mapping entry DummyXXX in section [DummyUsage] is smaller than granularity.

Dummy mapping of a data type smaller than granularity is enabled. E.g.:

It is not allowed to map a BOOLEAN if granularity is 8.

error 130

Entry “DefaultValue” in section [1018subX] differs from value … of section [DeviceInfo].

The values RevisionNumber, VendorNumber and ProductNumber of section [DeviceInfo] must agree with the values in object 0x1018. E.g.:

Default value in 1018sub3 is not equal to revision number in [DeviceInfo].

error 1600

Condition of CODB description in invalid syntax (…, …, …).

Condition syntax of an object description in a database has invalid syntax.

| ID | Notification / Description |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| error 1 | Section [...] not found. Section doesn’t exist in the EDS because section name has wrong spelling or doesn’t exist. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 2 | Incorrect brackets in section [...]. Section has no or incorrect enclosing brackets. E.g.: [sectionname) or sectionname] |  |  |  |  |  |  |  |  |  |  |  |  |
| error 3 | Illegal position of section name [...]. Left bracket of a section isn’t in the leftmost column. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 4 | Duplicate section [...]. Two or more sections in the EDS have the same section name. E.g.: [1004ObjectLinks]ObjectLinks=1; 1=1004;[1004ObjectLink] ObjectLinks=1; 1=1007; An error is produced because two identical sections exist. Here the function reading the EDS overwrite value '1004' of the entry with value '1007'. This could produce additional confusing errors. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 5 | Insufficient entries in section [...]. Value in the first entry is bigger than number of following entries. E.g.: [Comments]Lines=2Line1=second comment line ‘Line2’ is missing |  |  |  |  |  |  |  |  |  |  |  |  |
| error 6 | Insufficient sub objects in main section [...]. Number of sub objects in the main object is bigger than number of following sub objects. E.g.: [1004] SubNumber=2...[1004sub0] ... Section [1004sub1] is missing. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 7 | Link [...] related to non-existent object. Linked section related to non-existent object. E.g.: [0001ObjectLinks]... Object [0001] doesn't exist. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 8 | Access type in section [...] contradicts direction of PDO section [...]. Access type contradicts direction of the PDO section. An object mapped to a transmitting PDO could have access type RO, CONST or RWR. An object mapped to a receiving PDO could have access type WO or RWW. Access type RWW and RWR is used for objects that can be read and written via SDO but can be mapped only in one type of PDO. E.g.: ;Receive PDO Mapping Parameter[1600sub1]DefaultValue=0x62000108...[6200sub1]AccessType=ROPDOMapping=1... Object mapped to the receive PDO shall have access type WO or RWW. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 9 | Mandatory section [...] not found. An object in the database is marked as mandatory but it doesn't exist in the EDS. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 10 | Index in section [...] appears also in section [...]. Index in a fixed module section appears also in another non-module section. E.g.: [6000]... [M1Fixed6000]... Module section has same index 6000. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 11 | Mapping parameter section [...] shall have no gaps in the sub object list. A mapping parameter section shall have no gaps in the sub object list. E.g.: [1600]... [1600sub0]...[1600sub2]... If section [1600] has two sub objects, the sub objects must have sub index 0 and 1. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 12 | Section name [...] has an illegal character (e.g. leading 0 or 0x is not allowed). Section name has an illegal character. Note that a leading 0x and leading 0 are not allowed for index and sub index. Whitespaces are not allowed too. E.g.: [0x1000];'0x' is not allowed[1600sub01];leading '0' is not allowed for the sub index[1600 sub2];whitespace is not allowed[M01Comments];leading '0' is not allowed for module number |  |  |  |  |  |  |  |  |  |  |  |  |
| error 13 | Object ... linked in section [...] does not exist. A link points to an section which doesn't exist. E.g.: [1281ObjectLinks]ObjectLinks=11=10 If object [10] does not exist, this error is generated. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 14 | Section ... of structured object [...] not found. Sub object 0 of a structured object is missing. E.g.: [1600]ParameterName=Receive PDO Mapping ParameterObjectType=0x9SubNumber=0 Structured object has no sub objects. But sub object 0 is mandatory, e.g.: [1600]ParameterName=Receive PDO Mapping ParameterObjectType=0x9SubNumber=1[1600sub1]... Structured object has a sub object. But sub object 0 is missing. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 21 | Illegal format of entry ... in section [...]. Value in entry has an illegal format. E.g.: Entry Error Cause Solution Subnumber=1X Value is no numerical number, so it can't be evaluated. Subnumber=5 DefaultValue=018 The leading zero describes an octal number. But value is no octal number because octal numbers does not contain single numbers bigger than 7. DefaultValue=020 OrderCode= If an entry is mandatory a value has to be declared. OrderCode=0x7 | Entry | Error Cause | Solution | Subnumber=1X | Value is no numerical number, so it can't be evaluated. | Subnumber=5 | DefaultValue=018 | The leading zero describes an octal number. But value is no octal number because octal numbers does not contain single numbers bigger than 7. | DefaultValue=020 | OrderCode= | If an entry is mandatory a value has to be declared. | OrderCode=0x7 |
| Entry | Error Cause | Solution |  |  |  |  |  |  |  |  |  |  |  |
| Subnumber=1X | Value is no numerical number, so it can't be evaluated. | Subnumber=5 |  |  |  |  |  |  |  |  |  |  |  |
| DefaultValue=018 | The leading zero describes an octal number. But value is no octal number because octal numbers does not contain single numbers bigger than 7. | DefaultValue=020 |  |  |  |  |  |  |  |  |  |  |  |
| OrderCode= | If an entry is mandatory a value has to be declared. | OrderCode=0x7 |  |  |  |  |  |  |  |  |  |  |  |
| error 22 | Value in entry ... in section [...] is outside of valid area. Value in entry is out of specific value range. E.g.: Subnumber=256... Value area of entry Subnumber is Unsigned8 and its value range is [0..255]. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 23 | Too many character in entry ... in section [...]. Value in entry has too much characters. Number of characters of key name plus number of characters of value have to be less than 255. E.g.: ;value of entry 'VendorName' must not have more than 244 characters |  |  |  |  |  |  |  |  |  |  |  |  |
| error 24 | Unknown entry ... in section [...]. Unknown entry in an info section. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 25 | Duplicate entry ... in section [...]. Two or more entries in a section has the same key name. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 26 | Entry ... in section [...] not found. Mandatory entry doesn’t exist in specific section. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 27 | Entry ... in section [...] is not allowed. Entry is not allowed in specific section. Some object types do not support particular entries e.g. objects of type VAR must not have an entry Subnumber. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 28 | Value in entry ... in section [...] is outside of valid object area. Object value in an entry is out of specific value range. E.g.: [OptionalObjects]... 20=0x2000; This index is outside of the valid index range for optional objects. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 29 | Illegal value in entry ...in section [...]. Value of an entry has wrong format or there is no value although the entry is mandatory. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 30 | Value in entry ... in section [...] is not equal to database (...). Value of an entry in the EDS differs from the value in the accompanying database entry. In the last brackets the possible correct values are shown. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 31 | Complex data type in entry ... in section [...] is not allowed. A predefined complex data type of object type DEFSTRUCT should not exist in an EDS. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 32 | Data type in entry ... in section [...] is reserved. A reserved index pointing to a data type should not exist in an EDS. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 33 | Database requires description of sub objects in section [...]. If the data base defines a minimal number of elements, a description of sub objects is needed (Subnumber=... or CompactSubObj=...). |  |  |  |  |  |  |  |  |  |  |  |  |
| error 34 | Description of sub objects in section [...] is missing. Object type is ARRAY, RECORD or DEFSTRUCT but object has no description of sub objects. In the last brackets the possible correct values are shown. E.g.: [1004]ParameterName=PredefinedErrorField ObjectType=0x8 ;object type ARRAY ;entry SubNumber is missing[1004sub1]... |  |  |  |  |  |  |  |  |  |  |  |  |
| error 35 | Mapped object [...] shall have value 1 in entry PDOMapping. The object is mapped but value of entry PDOMapping is 0. E.g.: [1600sub1] DefaultValue=0x62000108 ...[6200sub1]PDOMapping=0 ... Object is mapped but has mapping is not allowed. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 36 | Value in entry DefaultValue in section [...] is not identical to number of last sub object. The value of DefaultValue is unequal the highest sub index implemented for this object. E.g.: [1026]... SubNumber=2 [1026sub0]DefaulValue=1... [1026sub4]... Default value in section [1026sub0] has to be 4. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 37 | Duplicate index in entry ... in section [...]. Index in a section is multiple used. E.g.: [OptionalObjects] 2=1003 1=1003 NrOfEntries=2 Index 1003 is multiple used. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 38 | Maximal number of sub objects of section [...] is smaller in database (...). Value of entry SubNumber is bigger than number of entry MaxElements in the database. E.g.: [1280]SubNumber=5 ... Number of entry MaxElements in database is 4. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 39 | Minimal number of sub objects in section [...] is bigger in database (...). Value of entry SubNumber is less than number of entry MinElements in the database. In the last brackets the possible correct values are shown. E.g.: [1280]SubNumber=3 ... Number of entry MinElements in database is 4. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 40 | Entry ... in section [...] has no corresponding sub object. An entry in a name section has no corresponding sub object. E.g.: [6000]...CompactSubObj=2[6000Name]...2=NameofSubindex2 Only sub object 0 and 1 are defined. So a name for the unknown entry 2 is not correct. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 41 | Entry EDSVersion in section [FileInfo] missing or value<4.0. The check relates to EDS files of version 4.0 or higher. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 42 | Data type of section […] differs from other data types in the array The sub objects of an array must have the same data type. Otherwise this error is reported. E.g.: [1003]ParameterName=Pre-defined Error FieldObjectType=0x8SubNumber=3[1003sub0]...[1003sub1]...DataType=0x0006[1003sub2]...DataType=0x0007 Data types of [1003sub1] and [1003sub2] are different. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 51 | Module description ... points to fixed and extended objects too. A module description points to fixed and extension objects too. E.g.: [M1FixedObjects]... [M1SubExtends]... It is not allowed to define fixed and extended objects for the same index (here:1). |  |  |  |  |  |  |  |  |  |  |  |  |
| error 52 | Fixed or extended object description [...] not found. A fixed or extension module description is expected but not found. E.g.: [SupportedModules] NrOfEntries=2; [M2SubExtends]... Section [M1FixedObjects] or [M1SubExtends] is missing. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 53 | Multiple used object [...] differs in entry .... If several modules contain the same fixed objects, their attributes shall be equal. E.g.: [M1Fixed6423]... DataType=0x0007 ... [M5Fixed6423]... DataType=0x0008 ... The same fixed object has different data types. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 54 | Module list [1027] is missing. If the section [SupportedModules] exist, object [1027] shall exist too. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 55 | Module list [1027] is redundant. If the object [1027] exist, section [SupportedModules] shall exist too. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 61 | There is no suitable PDO for section [...]. If no RxPDO or no TxPDO exists, an object with entry ‘PDOMapping=1’ only shall have corresponding access types. E.g.: ;condition: in the EDS exist no Transmit PDO Mapping Parameter[6000sub1] ...AccessType=ro PDOMapping=1 ... For these attributes there is no PDO available. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 62 | Number in entry ... in section [DeviceInfo] differs from number of supported PDOs. If no compact PDOs exist, the number of PDOs given in section [DeviceInfo] differs from the number of existing PDOs. E.g.: [DeviceInfo]...NrOfTXPDO=0; [1A00];Transmit PDO Mapping Parameter... An PDO exists although NrOfTXPDO is null. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 63 | Mapped object ... does not exist. A mapped object doesn’t exist in the EDS file. E.g.: ;Receive PDO Mapping Parameter[1600sub1]DefaultValue=0x62000108... If mapped section [6200sub1] doesn't exist, these error is reported. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 64 | Total length of mapped objects in section […] is bigger than 8 Byte. The total length of mapped objects is bigger than 8 byte. E.g.: [1600]...[1600sub0]....[1600sub1].DefaultValue=0x50000040...[1600sub2] DefaultValue=0x50020001... Total length of 65 Bits is too big. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 65 | Object length in section […] doesn't match data type of mapped object. The object length doesn't match data type of mapped object. E.g.: DefaultValue=0x50010040 [1600sub1] ;Receive PDO Mapping Paramter[5001]DataType=0x0007 ... The data type of mapped object is Unsigned32 and object length in the mapping parameter is 64 bit. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 66 | Data type in section […] is not mappable. The given data type is not mappable but object is mapped. E.g.: [1600sub1]DefaultValue=0x50030020 ...[5003] DataType=0x0009 The data type Visible String is not mappable. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 67 | Access type in section […] is writable although sub object 0 is constant or read-only. For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. If the access type of sub-index 0 of a PDO mapping parameter object is constant or read-only no variable mapping is supported and therefore the access type of further sub-indexes have to be constant or read-only. E.g.: [1600sub0]AccessType=ro ... [1600sub1]AccesxType=wr The access type have to be CONST or RO because object does not support variable mapping. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 68 | Access type in section […] is constant or read-only although sub object 0 writable. For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. If the access type of sub-index 0 of a PDO mapping parameter object is writable then variable mapping is supported and therefore the access type of further sub-indexes have to be writable too. E.g.: [1600sub0]AccessType=rw ...[1600sub1]AccesxType=ro DAccess type have to be writable too. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 69 | Entry Granularity in section [DeviceInfo] has to be 0 because all PDOs support constant mapping. No PDO parameter object supports variable mapping. Therefore the granularity has to be 0. E.g.: ;access type all sub-indexes of PDO mapping parameter objects is ro or const [DeviceInfo]Granularity=8 Granularity has to be 0 because mapping is not modifiable. Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. | Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |  |  |  |  |  |  |  |  |  |  |  |
| Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| error 70 | Entry Granularity in section [DeviceInfo] has to be bigger than 0 because all PDOs support variable mapping. All PDO parameter objects supports variable mapping. Therefore the granularity has to be bigger than 0. E.g.: ;all sub-indexes of PDO mapping parameter;objects access type is writable[DeviceInfo]Granularity=0 Granularity has to be bigger than 0 because mapping is modifiable. Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. | Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |  |  |  |  |  |  |  |  |  |  |  |
| Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| error 71 | Number of Rx/TxPDOs in entry DefaultValue in section [1004sub0] differs from number of Rx/TxPDOs in section [DeviceInfo]. In object 0x1004 the default value of sub index 0 describes the overall number PDOs supported. This value has to be equal to the number of PDOs in section [DeviceInfo]. E.g.: [DeviceInfo]NrOfRxPDO=3NrOfTxPDO=2...[1004sub0]DefaultValue=0x30003... The LSB of the default value defines the number of TxPDOs and the MSB defines the number of RxPDOs. Therefore the correct value must be 0x30002. All sub-indexes of PDO mapping parameter objects access type is RO or CONST. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 72 | Number of Rx/TxPDOs in entry DefaultValue in section [1004subX] is bigger than number of Rx/TxPDOs in section [DeviceInfo]. In object 0x1004 the default value of sub index 1 describes the number of synchronous PDOs and sub index 2 the number of asynchrony PDOs. These values have to be smaller or equal to the number of PDOs in section [DeviceInfo]. E.g.: [DeviceInfo]... NrOfTxPDO=2 NrOfRxPDO=1 [1004sub1]DefaultValue=0x10003... The LSB of the default value defines the number of synchronous TxPDOs and the MSB defines the number of asynchronous RxPDOs. Therefore the correct value must be 0x10002, 0x10001, 0x10000, 2, 1 or 0. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 73 | Entry GroupMessaging in section [DeviceInfo] has to be set to 1 because there are multiplexed PDOs. There are multiplexed PDOs (MPDOs) in the object dictionary. Therefore entry GroupMessaging has to be set to 1. E.g.: [DeviceInfo]GroupMessaging=0...[1600sub0]DefaultValue=255... If the default value of sub object 0 of a PDO mapping parameter is 254 or 255 then this PDO is a multiplexed PDO. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 74 | Invalid use of dummy mapping in TxPDO section […]. Dummy mapping is used in a TxPDO. E.g.: [1a00sub1]...DefaultValue=0x00020008... It is not allowed to use dummy mapping in a TxPDO. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 75 | Object length in section […] is smaller than granularity. The length of a mapped object is smaller than the granularity of the device. E.g.: [DeviceInfo]...Granularity=64[1a00sub1]...DefaultValue=0x20000120[2000sub1]...DataType=0x0007 Granularity is 64 but a object with data type UNSIGNED32 is mapped. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 76 | Length of selected dummy mapping entry DummyXXX in section [DummyUsage] is smaller than granularity. Dummy mapping of a data type smaller than granularity is enabled. E.g.: [DeviceInfo]Granularity=8...[DummyUsage]Dummy0001=1... It is not allowed to map a BOOLEAN if granularity is 8. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 130 | Entry “DefaultValue” in section [1018subX] differs from value … of section [DeviceInfo]. The values RevisionNumber, VendorNumber and ProductNumber of section [DeviceInfo] must agree with the values in object 0x1018. E.g.: [DeviceInfo]VendorNumber=5;ProductNumber=2; RevisionNumber=1;...;Vendor ID[1018sub1]DefaultValue=5...;Product code[1018sub2]DefaultValue=2...;Revision number[1018sub3]DefaultValue=2... Default value in 1018sub3 is not equal to revision number in [DeviceInfo]. |  |  |  |  |  |  |  |  |  |  |  |  |
| error 1600 | Condition of CODB description in invalid syntax (…, …, …). Condition syntax of an object description in a database has invalid syntax. |  |  |  |  |  |  |  |  |  |  |  |  |

| Entry | Error Cause | Solution |
|---|---|---|
| Subnumber=1X | Value is no numerical number, so it can't be evaluated. | Subnumber=5 |
| DefaultValue=018 | The leading zero describes an octal number. But value is no octal number because octal numbers does not contain single numbers bigger than 7. | DefaultValue=020 |
| OrderCode= | If an entry is mandatory a value has to be declared. | OrderCode=0x7 |

| Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |
|---|

| Note This error is not generated if some PDOs support variable mapping and others don't support it because this case is not specified clearly. |
|---|

```c
[sectionname)
```

```c
sectionname]
```

```c
[1004ObjectLinks]
ObjectLinks=1;
1=1004;

[1004ObjectLink]
ObjectLinks=1;
1=1007;
```

```c
[Comments]
Lines=2
Line1=second comment line ‘Line2’ is missing
```

```c
[1004]
SubNumber=2
...
[1004sub0]
...
```

```c
[0001ObjectLinks]...
```

```c
;Receive 
PDO Mapping Parameter
[1600sub1]
DefaultValue=0x62000108
...

[6200sub1]
AccessType=RO
PDOMapping=1
...
```

```c
[6000]
...

[M1Fixed6000]
...
```

```c
[1600]
...

[1600sub0]
...

[1600sub2]
...
```

```c
[0x1000]
;'0x' is not allowed

[1600sub01]
;leading '0' is not allowed for the sub index

[1600 sub2]
;whitespace is not allowed

[M01Comments]
;leading '0' is not allowed for module number
```

```c
[1281ObjectLinks]
ObjectLinks=1
1=10
```

```c
[1600]
ParameterName=Receive PDO Mapping Parameter
ObjectType=0x9
SubNumber=0
```

```c
[1600]
ParameterName=Receive PDO Mapping Parameter
ObjectType=0x9
SubNumber=1

[1600sub1]
...
```

```c
Subnumber=256
...
```

```c
;value of entry 'VendorName' 
must not have more than 244 characters
```

```c
[OptionalObjects]
...
20=0x2000;
```

```c
[1004]
ParameterName=PredefinedErrorField
ObjectType=0x8

;object type ARRAY
;entry SubNumber is missing

[1004sub1]
...
```

```c
[1600sub1]
DefaultValue=0x62000108
...

[6200sub1]
PDOMapping=0
...
```

```c
[1026]...

SubNumber=2

[1026sub0]
DefaulValue=1
...
[1026sub4]
...
```

```c
[OptionalObjects] 2=1003

1=1003

NrOfEntries=2
```

```c
[1280]
SubNumber=5
...
```

```c
[1280]
SubNumber=3
...
```

```c
[6000]
...
CompactSubObj=2

[6000Name]
...
2=NameofSubindex2
```

```c
[1003]
ParameterName=Pre-defined Error Field
ObjectType=0x8
SubNumber=3

[1003sub0]
...

[1003sub1]
...
DataType=0x0006

[1003sub2]
...
DataType=0x0007
```

```c
[M1FixedObjects]
...

[M1SubExtends]
...
```

```c
[SupportedModules] NrOfEntries=2;

[M2SubExtends]
...
```

```c
[M1Fixed6423]
...
DataType=0x0007
...

[M5Fixed6423]
...
DataType=0x0008
...
```

```c
;condition: in the EDS exist 
no Transmit PDO Mapping Parameter
[6000sub1]
...
AccessType=ro
PDOMapping=1
...
```

```c
[DeviceInfo]
...
NrOfTXPDO=0;

[1A00]
;Transmit PDO Mapping Parameter
...
```

```c
;Receive 
PDO Mapping Parameter
[1600sub1]
DefaultValue=0x62000108
...
```

```c
[1600]
...
[1600sub0].
...

[1600sub1].
DefaultValue=0x50000040
...

[1600sub2]
DefaultValue=0x50020001
...
```

```c
DefaultValue=0x50010040

[1600sub1]

;Receive 
PDO Mapping Paramter

[5001]
DataType=0x0007
...
```

```c
[1600sub1]
DefaultValue=0x50030020
...

[5003]
DataType=0x0009
```

```c
[1600sub0]
AccessType=ro
...

[1600sub1]
AccesxType=wr
```

```c
[1600sub0]
AccessType=rw
...
[1600sub1]
AccesxType=ro
```

```c
;access type all sub-indexes 
of PDO mapping parameter objects is ro or const
[DeviceInfo]
Granularity=8
```

```c
;all sub-indexes of PDO mapping 
parameter
;objects access type is writable
[DeviceInfo]
Granularity=0
```

```c
[DeviceInfo]
NrOfRxPDO=3
NrOfTxPDO=2
...

[1004sub0]
DefaultValue=0x30003
...
```

```c
[DeviceInfo]
...

NrOfTxPDO=2

NrOfRxPDO=1

[1004sub1]
DefaultValue=0x10003
...
```

```c
[DeviceInfo]
GroupMessaging=0
...

[1600sub0]
DefaultValue=255
...
```

```c
[1a00sub1]
...
DefaultValue=0x00020008
...
```

```c
[DeviceInfo]
...
Granularity=64

[1a00sub1]
...
DefaultValue=0x20000120

[2000sub1]
...
DataType=0x0007
```

```c
[DeviceInfo]
Granularity=8
...

[DummyUsage]
Dummy0001=1
...
```

```c
[DeviceInfo]
VendorNumber=5;
ProductNumber=2;
RevisionNumber=1;
...

;Vendor ID
[1018sub1]
DefaultValue=5
...

;Product 
code
[1018sub2]
DefaultValue=2
...

;Revision number
[1018sub3]
DefaultValue=2
...
```
