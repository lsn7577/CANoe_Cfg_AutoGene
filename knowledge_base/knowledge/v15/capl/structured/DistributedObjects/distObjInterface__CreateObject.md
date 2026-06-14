# distObjInterface::CreateObject

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
distObjRef <Interface> distObjInterface <Interface>::CreateObject(distObjBlueprint <Interface> blueprint, char path[]);
distObjRef reverse<<Interface>> distObjInterface <Interface>::CreateObject(distObjBlueprint reverse<<Interface>> blueprint, char path[]);
```

## Description

Creates a dynamic object from the blueprint.

## Parameters

| Name | Description |
|---|---|
| blueprint | Blueprint which sets the attributes and virtual networks of the dynamic object. |
| path | Fully qualified name of the dynamic object. |

## Return Values

New dynamic object.
Invalid object if an error occurred.

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {}
}

// CAPL
on key 'a' {
  distObjBlueprint SomeInterface bp;
  distObjBlueprint reverse<SomeInterface> rev_bp;

  bp = SomeInterface.CreateObjectBlueprint();
  rev_bp = SomeInterface.CreateReverseBlueprint();

  SomeInteface.CreateObject(bp, "SomeNamespace::Obj");
  SomeInteface.CreateObject(rev_bp, "SomeNamespace::RevObj");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
