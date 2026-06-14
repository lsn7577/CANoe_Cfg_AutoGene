# on any_fct_called

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a provided method of a distributed object derived from the given interface is called. At this time, the automatic answering feature has already set the out parameters and return value to their default values if it is configured.

## Example

```c
// vCDL
version 1.4;
namespace SomeNamespace
{
  interface SomeInterface
  {
    internal method void SomeMethod(int32 p);
  }
  SomeInterface Obj1;
  SomeInterface Obj2;
}

// CAPL
on key 'a'
{
  Obj1.SomeMethod.CallAsync(1);
}
on key 'b'
{
  Obj2.SomeMethod.CallAsync(2);
}
on any_fct_called SomeInterface.SomeMethod
{
  write("Called SomeMethod at object %s with parameter %d",
  this.object.Path,
  this.context.p);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | 15 | 15 | 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| object Parent object of the called method. | distObjRef <T> | Read only |
| context Call context of the method call. | callContext <T> | Read only |
