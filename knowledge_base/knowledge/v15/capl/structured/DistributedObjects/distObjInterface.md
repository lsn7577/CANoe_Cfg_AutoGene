# distObjInterface

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjInterface *
distObjInterface <Interface>
```

## Description

A type for creating blueprints and dynamic distributed objects.

All distObjInterface types are singleton types. The value of each type is bound to the name of the corresponding interface.

The types are not available for user declarations.

## Parameters

| Name | Description |
|---|---|
| Interface | The optionally qualified name of a distributed object interface. It is also possible to take the reverse of in interface by using the reverse<…> operator. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {}
  attribute int32 SomeAttribute;
}

// CAPL
on start {
  distObjRef SomeInterface obj;
  distObjBlueprint SomeInterface bp;

  bp = SomeInterface.CreateObjectBlueprint();
  obj = SomeInterface.CreateObject(bp, "SomeNamespace::Obj");

  SomeInterface.DestroyObject("SomeNamespace::Obj");
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
