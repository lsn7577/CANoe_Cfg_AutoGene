# distObjContainerRef::Erase

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long distObjContainerRef <Typedef name>::Erase(dword index);
```

## Description

Replaces an object at the given index with an invalid object.

It requires that <Typedef name> refers to an object array type.

The length of the container is not changed.

## Parameters

| Name | Description |
|---|---|
| index | Index at which to remove the object. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
    internal data int32 d;
  }
  array<SomeInterface, 42> ObjList;
}

// CAPL
on key 'a' {
  // remove an object
  ObjList.Erase(2);
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
