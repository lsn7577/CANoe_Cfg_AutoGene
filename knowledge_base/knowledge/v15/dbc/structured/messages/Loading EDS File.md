# Loading EDS File

> Category: `DBC` | Subcategory: `messages` | Type: `concept`

warning 1100

Entry ... is not read because object is not structured.

An attribute is not read because the object is not structured. The entry is not lost, it is displayed in the Unknown Entry window. E.g.:

The SubNumber entry is not read because object type is VAR.

warning 1101

Entry ... is not read because object is structured.

An attribute is not read because the object is structured. The entry is not lost, it is displayed in the Unknown Entry window. So a deactivated field in the attribute window is not filled out. E.g.:

Data type, access type and mapping information are not read because object type is ARRAY.

warning 1102

Entry CompactSubObj is not read because entry SubNumber is bigger or equal null.

Entry CompactSubObj is not read because a entry SubNumber is found in the same section which has a number bigger or equal null. The entry is not lost, it is displayed in the Unknown Entry window. E.g.:

| ID | Notification / Description |
|---|---|
| warning 1100 | Entry ... is not read because object is not structured. An attribute is not read because the object is not structured. The entry is not lost, it is displayed in the Unknown Entry window. E.g.: [1000]ParameterName=Device TypeObjectType=0x7SubNumber=2 The SubNumber entry is not read because object type is VAR. |
| warning 1101 | Entry ... is not read because object is structured. An attribute is not read because the object is structured. The entry is not lost, it is displayed in the Unknown Entry window. So a deactivated field in the attribute window is not filled out. E.g.: [1003]ParameterName=PredefinedErrorFieldObjectType=0x8DataType=0x0007AccessType=rwPDOMapping=0SubNumber=2 Data type, access type and mapping information are not read because object type is ARRAY. |
| warning 1102 | Entry CompactSubObj is not read because entry SubNumber is bigger or equal null. Entry CompactSubObj is not read because a entry SubNumber is found in the same section which has a number bigger or equal null. The entry is not lost, it is displayed in the Unknown Entry window. E.g.: [1400]...CompactSubObj=2SubNumber=2... |

```c
[1000]
ParameterName=Device Type
ObjectType=0x7
SubNumber=2
```

```c
[1003]
ParameterName=PredefinedErrorField
ObjectType=0x8
DataType=0x0007
AccessType=rw
PDOMapping=0
SubNumber=2
```

```c
[1400]
...
CompactSubObj=2
SubNumber=2
...
```
