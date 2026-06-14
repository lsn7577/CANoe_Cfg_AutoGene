# distObjBlueprint

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjBlueprint *
distObjBlueprint <Interface>
```

## Description

A blueprint type for dynamically creating distributed objects.

Variables are initialized with an invalid blueprint. The blueprints have a copy semantic when they are assigned (assignment operator, call-by-value parameter, function return value). Stack allocated variables and temporary values are automatically destroyed when they go out of scope. Blueprint types cannot be used for copy-restore parameters.

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
  write("%d", bp.IsValid); // output: 0

  bp = SomeInterface.CreateObjectBlueprint();
  write("%d", bp.IsValid); // output: 1

  obj = bp.CreateObject("SomeNamespace::Obj");
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
