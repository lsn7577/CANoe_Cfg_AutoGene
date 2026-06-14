# Warnings (CANchkEDS)

> Category: `DBC` | Subcategory: `messages` | Type: `concept`

warning 1

Unknown or not used section [...].

After all checks a section is found which has not been checked, because this section is unknown or not used.

[Tools]

This section is unknown and produce this warning.

[1010]SubNumber=1ObjectType=0x7;...[1010sub0]...

An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked.

warning 2

Redundant sub object [...].

More entries are found than expected. E.g.:

The last sub-object is redundant and causes the warning.

warning 3

Illegal enumeration in section [...].

Enumeration is not correct. E.g.:

Here the Line2=... entry is needed.

warning 4

Access type in section [...] has no clear mapping direction.

Object is mappable and access type is RW. This could possibly cause mapping problems. Instead of RW the attributes RWR or RWW should be used. E.g.:

Instead of RW the RWR or RWW argument should be used.

warning 5

Access type in section [...] has no clear mapping direction concerning PDO section [...].

Access type in mapped section has no clear mapping direction concerning the PDO section. E.g.:

Object mapped to the receive PDO shall have access type WO or RWW. If access type is RW the mapping direction is not clear and possibly can cause mapping problems.

warning 6

There are dynamic channels although entry DynamicChannelsSupported in section [DeviceInfo] is 0.

There is a section [DynamicChannels] although the device does not support dynamic channels (according to entry DynamicChannelsSupported of section [DeviceInfo]). E.g.:

There are dynamic channels defined although the device doesn't support them.

warning 21

Unknown or not used entry ... in section [...].

After all checks an entry is found which has not been checked, because this entry is unknown or not used.

warning 22

Reserved entry ... in section [...].

For compatibility reasons, the entries ProductVersion, LMT_ManufacturerName, LMT_ProductName, Extended-BootUpMaster, ExtendedBootUpSlave and ProductRevision in section [DeviceInfo] are reserved.

warning 23

Data type in entry ... in section [...] can't be checked.

Manufacturer specific data types and device profile specific standard data types can't be checked.

warning 24

Entry ... in section [...] not found.

An important but not mandatory entry doesn't exist in specific section. This notification is shown e.g. if entry DefaultValue is missing in sub object 0.

warning 25

Value in entry DefaultValue in section [...] is not identical to number of last sub object.

This warning is generated for PDO Mapping parameters if the value of DefaultValue is unequal the highest subindex implemented and it granularity is 0 (no variable mapping). E.g.:

warning 26

Access type of section […] is writable although COB-ID of PDO […] is constant or read-only.

For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. After all objects are mapped subindex 0 is set to the valid number of mapped objects. Finally the PDO will be created by writing to it’s communication parameter COB-ID. E.g.:

Because associated COB-ID is constant it makes no sense to allow write access to the mapping parameter object.

warning 30

Value in entry 'DefaultValue' in Section […] is not equal to database…

The default value differs from the value defined in the database.

warning 50

Number of RxPDOs and TxPDOs in section [DeviceInfo] is 0 but compact PDOs are defined.

Although it is denoted that the device supports compact PDOs the number of PDOs is zero. E.g.:

warning 51

Mapped object in section […] is missing.

The mapping parameter contains no reference to a mapped object although the mapping parameter is valid.

| ID | Notification / Description |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| warning 1 | Unknown or not used section [...]. After all checks a section is found which has not been checked, because this section is unknown or not used. Section Error Cause [Tools] This section is unknown and produce this warning. [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. | Section | Error Cause | [Tools] | This section is unknown and produce this warning. | [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... | An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. |
| Section | Error Cause |  |  |  |  |  |  |
| [Tools] | This section is unknown and produce this warning. |  |  |  |  |  |  |
| [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... | An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. |  |  |  |  |  |  |
| warning 2 | Redundant sub object [...]. More entries are found than expected. E.g.: SubNumber=2... [1010sub0]... [1010sub1]... [1010sub2]... The last sub-object is redundant and causes the warning. |  |  |  |  |  |  |
| warning 3 | Illegal enumeration in section [...]. Enumeration is not correct. E.g.: [Comments]Lines=2 Line1=correct line Line3=incorrect enumeration. Has to be 'Line2=...' Here the Line2=... entry is needed. |  |  |  |  |  |  |
| warning 4 | Access type in section [...] has no clear mapping direction. Object is mappable and access type is RW. This could possibly cause mapping problems. Instead of RW the attributes RWR or RWW should be used. E.g.: [6000sub1]... PDOMapping=1 AccessType=rw ... Instead of RW the RWR or RWW argument should be used. |  |  |  |  |  |  |
| warning 5 | Access type in section [...] has no clear mapping direction concerning PDO section [...]. Access type in mapped section has no clear mapping direction concerning the PDO section. E.g.: ;Empfangs-PDO-Mapping-Parameter[1600sub1] DefaultValue=0x62000108 ...[6200sub1]AccessType=rw PDOMapping=1 ... Object mapped to the receive PDO shall have access type WO or RWW. If access type is RW the mapping direction is not clear and possibly can cause mapping problems. |  |  |  |  |  |  |
| warning 6 | There are dynamic channels although entry DynamicChannelsSupported in section [DeviceInfo] is 0. There is a section [DynamicChannels] although the device does not support dynamic channels (according to entry DynamicChannelsSupported of section [DeviceInfo]). E.g.: [DeviceInfo]DynamicChannelsSupported=0...[DynamicChannels]... There are dynamic channels defined although the device doesn't support them. |  |  |  |  |  |  |
| warning 21 | Unknown or not used entry ... in section [...]. After all checks an entry is found which has not been checked, because this entry is unknown or not used. |  |  |  |  |  |  |
| warning 22 | Reserved entry ... in section [...]. For compatibility reasons, the entries ProductVersion, LMT_ManufacturerName, LMT_ProductName, Extended-BootUpMaster, ExtendedBootUpSlave and ProductRevision in section [DeviceInfo] are reserved. |  |  |  |  |  |  |
| warning 23 | Data type in entry ... in section [...] can't be checked. Manufacturer specific data types and device profile specific standard data types can't be checked. |  |  |  |  |  |  |
| warning 24 | Entry ... in section [...] not found. An important but not mandatory entry doesn't exist in specific section. This notification is shown e.g. if entry DefaultValue is missing in sub object 0. |  |  |  |  |  |  |
| warning 25 | Value in entry DefaultValue in section [...] is not identical to number of last sub object. This warning is generated for PDO Mapping parameters if the value of DefaultValue is unequal the highest subindex implemented and it granularity is 0 (no variable mapping). E.g.: [DeviceInfo]Granularity=0 ... [1600]SubNumber=2 ... [1600sub0]DefaulValue=0 ... [1600sub1] ... |  |  |  |  |  |  |
| warning 26 | Access type of section […] is writable although COB-ID of PDO […] is constant or read-only. For changing the PDO mapping first the PDO has to be deleted, the sub-index 0 must be set to 0 (mapping is deactivated). Then the objects can be remapped. After all objects are mapped subindex 0 is set to the valid number of mapped objects. Finally the PDO will be created by writing to it’s communication parameter COB-ID. E.g.: [1400sub1]AccessType=ro...;communication parameter COB-ID is constant[1600sub0]AccessType=rw... Because associated COB-ID is constant it makes no sense to allow write access to the mapping parameter object. |  |  |  |  |  |  |
| warning 30 | Value in entry 'DefaultValue' in Section […] is not equal to database… The default value differs from the value defined in the database. |  |  |  |  |  |  |
| warning 50 | Number of RxPDOs and TxPDOs in section [DeviceInfo] is 0 but compact PDOs are defined. Although it is denoted that the device supports compact PDOs the number of PDOs is zero. E.g.: [DeviceInfo]CompactPDO=3NrOfRXPDO=0NrOfTXPDO=0 |  |  |  |  |  |  |
| warning 51 | Mapped object in section […] is missing. The mapping parameter contains no reference to a mapped object although the mapping parameter is valid. |  |  |  |  |  |  |

| Section | Error Cause |
|---|---|
| [Tools] | This section is unknown and produce this warning. |
| [1010]SubNumber=1ObjectType=0x7;...[1010sub0]... | An error notification reports that entry SubNumber is not allowed, because object type is VAR. Therefore no sub objects are checked and section [1010sub0] is not checked. |

```c
SubNumber=2
...
[1010sub0]
...
[1010sub1]
...
[1010sub2]
...
```

```c
[Comments]
Lines=2
Line1=correct line
Line3=incorrect enumeration. Has to be 'Line2=...'
```

```c
[6000sub1]...

PDOMapping=1

AccessType=rw

...
```

```c
;Empfangs-PDO-Mapping-Parameter
[1600sub1]
DefaultValue=0x62000108
...

[6200sub1]
AccessType=rw
PDOMapping=1
...
```

```c
[DeviceInfo]
DynamicChannelsSupported=0
...

[DynamicChannels]
...
```

```c
[DeviceInfo]
Granularity=0
...
[1600]
SubNumber=2
...
[1600sub0]
DefaulValue=0
...
[1600sub1]
...
```

```c
[1400sub1]
AccessType=ro
...

;communication parameter COB-ID is constant

[1600sub0]
AccessType=rw
...
```

```c
[DeviceInfo]
CompactPDO=3
NrOfRXPDO=0
NrOfTXPDO=0
```
