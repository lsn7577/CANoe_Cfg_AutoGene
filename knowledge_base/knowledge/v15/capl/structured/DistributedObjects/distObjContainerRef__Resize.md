# distObjContainerRef::Resize

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long distObjContainerRef <Typedef name>::Resize(dword size);
long distObjContainerRef <Typedef name>::Resize(dword index, distObjBlueprint <Interface> blueprint);
```

## Description

This method resizes the container. If the new size is greater than the old size, new elements will be added at the end. If the new size is less than the old size, elements will be removed at the end.

It requires that <Typedef name> refers to a list type.

The first overload is available for lists of objects and references. It appends default objects or empty references.

The second Overload is only available when <Typedef name> refers to a (nested) list of objects. Here the objects are created according to the blueprint argument.

## Parameters

| Name | Description |
|---|---|
| size | The new size of the container. |
| blueprint | The blueprint according to which objects are created. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  virtualnetwork SomeNetwork;
  interface SomeInterface {
    internal data int32 d;
  }
  list<SomeInterface> ObjList;
  list<reference<SomeInterface>> RefList;
}

// CAPL
on key 'a' {
  stack distObjBlueprint SomeInterface bp = SomeInterface.CreateObjectBlueprint();
  bp.d.SetVirtualNetwork(SomeNetwork);

  // resize with default objects or emtpy references
  ObjList.Resize(42);
  RefList.Resize(42);

  // resize with object blueprint
  ObjList.Resize(100, bp);
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
