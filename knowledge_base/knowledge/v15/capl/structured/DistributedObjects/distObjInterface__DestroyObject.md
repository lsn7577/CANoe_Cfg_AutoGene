# distObjInterface::DestroyObject

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long distObjInterface <Interface>::DestroyObject(distObjRef <Interface> object);
long distObjInterface <Interface>::DestroyObject(distObjRef reverse<<Interface>> object);
```

## Description

Destroys a dynamic object.

## Parameters

| Name | Description |
|---|---|
| object | Dynamic object to be destroyed. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {}
}

// CAPL
on key 'a' {
  distObjRef SomeInterface obj;
  distObjRef reverse<SomeInterface> rev_obj;

  distObjBlueprint SomeInterface bp;
  distObjBlueprint reverse<SomeInterface> rev_bp;

  bp = SomeInterface.CreateObjectBlueprint();
  rev_bp = SomeInterface.CreateReverseBlueprint();

  obj = SomeInteface.CreateObject(bp, "SomeNamespace::Obj");
  rev_obj = SomeInteface.CreateObject(rev_bp, "SomeNamespace::RevObj");

  SomeInterface.DestroyObject(obj);
  SomeInterface.DestroyObject(rev_obj);
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
