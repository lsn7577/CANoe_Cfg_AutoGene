# distObjMemberBlueprint

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjMemberBlueprint
```

## Description

A type for configuring the attributes and virtual network of an object blueprint member.

This type cannot be used in declarations.

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
