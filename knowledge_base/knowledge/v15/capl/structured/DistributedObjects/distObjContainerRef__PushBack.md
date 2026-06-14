# distObjContainerRef::PushBack

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long distObjContainerRef <Typedef name>::PushBack(); // form 1
long distObjContainerRef <Typedef name>::PushBack(char path[]); // form 2
long distObjContainerRef <Typedef name>::PushBack(distObjRef <Interface> target); // form 3
long distObjContainerRef <Typedef name>::PushBack(distObjBlueprint <Interface> blueprint); // form 4
```

## Description

Adds an element at the end of the container.

It requires that <Typedef name> refers to a list type.

The first overload is available for lists of objects and references. It appends a default object or reference.

Form 2 and 3 are only available when <Typedef name> refers to a (nested) list of references. Here the parameter can be used to directly set the target of the new reference.

Form 4 is only available when <Typedef name> refers to a (nested) list of objects.

## Parameters

| Name | Description |
|---|---|
| path | Fully qualified name of the target object. |
| target | Target object. |
| blueprint | Blueprint which is used for object creation. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
    internal data int32 d;
  }
  object Obj : SomeInterface {}
  list<SomeInterface> ObjList;
  list<reference<SomeInterface>> RefList;
}

// CAPL
on key 'a' {
  // append default object or reference to list
  ObjList.PushBack();
  RefList.PushBack();

  // append reference with a specific target
  RefList.PushBack(Obj);
  RefList.PushBack("SomeNamespace::Obj");
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
