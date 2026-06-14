# distObjMemberBlueprint::SetAttribute

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long distObjMemberBlueprint::SetAttribute(char name[], char value[]);
long distObjMemberBlueprint::SetAttribute(char name[], long value);
long distObjMemberBlueprint::SetAttribute(char name[], dword value);
long distObjMemberBlueprint::SetAttribute(char name[], int64 value);
long distObjMemberBlueprint::SetAttribute(char name[], qword value);
long distObjMemberBlueprint::SetAttribute(char name[], double value);
```

## Description

Sets an attribute at the member blueprint.

The attribute type must correspond to the overload that is called. Otherwise an error code will be returned. Integer types will be converted if they fall in the range of the attribute type.

## Parameters

| Name | Description |
|---|---|
| name | Fully qualified name of the attribute. |
| value | Value of the attribute. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
  consumed event int32 SomeEvent;
  }
  attribute int32 IntegerAttribute;
  attribute string StringAttribute;
}

// CAPL
on key 'a' {
  distObjBlueprint SomeInterface bp;
  bp = SomeInterface.CreateObjectBlueprint();

  bp.SomeEvent.SetAttribute("SomeNamespace::IntegerAttribute", 42);
  bp.SomeEvent.SetAttribute("SomeNamespace::StringAttribute", "test");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
