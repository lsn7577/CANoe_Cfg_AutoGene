# on any_fct_retured

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a method of a distributed object derived from the given interface has returned at the consumer.

## Example

```c
// vCDL
version 1.4;
namespace SomeNamespace
{
  interface SomeInterface
  {
    internal method int32 SomeMethod();
  }
  SomeInterface Obj1;
  SomeInterface Obj2;
}

// CAPL
on key 'a'
{
  $Obj1.SomeMethod.DefaultResult = 1;
  Obj1.SomeMethod.CallAsync();
}
on key 'b'
{
  $Obj2.SomeMethod.DefaultResult = 2;
  Obj2.SomeMethod.CallAsync();
}
on any_fct_returned SomeInterface.SomeMethod
{
  write("SomeMethod is returned at object %s with value %d",
  this.object.Path,
  this.context.Result);
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
| object Parent object of the returned method. | distObjRef <T> | Read only |
| context Call context of the method call. | callContext <T> | Read only |
