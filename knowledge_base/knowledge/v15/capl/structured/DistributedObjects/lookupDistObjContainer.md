# lookupDistObjContainer

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjContainerRef * lookupDistObjContainer(char path[]);
```

## Description

Obtains a container by using a string.

A downcast can be used to get a more concrete type.

## Parameters

| Name | Description |
|---|---|
| path | Fully qualified name of the container. |

## Return Values

Container with the given path.
Invalid container if nothing was found.

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
    internal data int32 d;
  }
  Typdef ContainerType = array<SomeInterface, 42>;
  ContainerType Container;
}

// CAPL
on key 'a' {
  distObjContainerRef SomeNamespace::ContainerType x;

  // downcast with typename
  x = (distObjContainerRef SomeNamespace::ContainerType)lookupDistObjRefrence("SomeNamespace::Container");

  // downcast with __type_of
  x = (__type_of(x))lookupDistObjContainer("SomeNamespace::Container");
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
