# distObjInterface::CreateObjectBlueprint

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
distObjBlueprint reverse<<Interface>> distObjInterface <Interface>::CreateObjectBlueprint();
distObjBlueprint reverse<<Interface>> distObjInterface <Interface>::CreateObjectBlueprint(distObjRef reverse<<Interface>> object);
```

## Description

Creates a blueprint for the reverse of the given interface.

## Parameters

| Name | Description |
|---|---|
| object | Object from which to copy attributes and virtual networks. |

## Return Values

New object blueprint.
Invalid object blueprint if an error occurred.

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {}
  object Obj : reverse<SomeInterface> {}
}

// CAPL
on key 'a' {
  distObjBlueprint reverse<SomeInterface> bp;

  bp = SomeInterface.CreateReverseObjectBlueprint();
  bp = SomeInterface.CreateReverseObjectBlueprint(Obj);
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
