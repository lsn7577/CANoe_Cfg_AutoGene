# on any_value_update

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a value of the given set is updated. The sets are defined by the DO interface members (e.g. SomeInterface.SomeData, SomeInterface.SomeData.SubscriptionState). Each value at a derived object is part of such a set.

## Example

```c
// vCDL
version 1.4;
namespace SomeNamespace
{
  interface SomeInterface
  {
    internal data int32 SomeData;
  }
  SomeInterface Obj1;
  SomeInterface Obj2;

  // CAPL requires named interfaces for use in handlers
  typedef SomeInterfaceRev = reverse<SomeInterface>;
  SomeInterfaceRev Obj3;
}

// CAPL
on key 'a'
{
  $Obj1.SomeData = 42;
}
on key 'b'
{
  $Obj2.SomeData = 42;
}
on key 'c'
{
  $Obj3.SomeData = 42;
}

// helper function to compare DOs by identity
dword equals(distObjRef * a, distObjRef * b)
{
  if (!a.IsValid || !b.IsValid)
  return 0;
  return strncmp(a.Path, b.Path, _max(elCount(a.Path), elCount(b.Path))) == 0;
}
// handler for Obj1 and Obj2
on any_value_update SomeInterface.SomeData
{
  write("Updated SomeData at object %s to value %d",
  this.object.Path,
  $this.value);
  if (equals(this.object, Obj2))
  {
    write("Specialized code for Obj2");
  }
}
// handler for Obj3
on any_value_update SomeInterfaceRev.SomeData
{
  write("Updated SomeData at object %s to value %d",
  this.object.Path,
  $this.value);
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
| object Parent object of the updated value. | distObjRef <T> | Read only |
| value New value | valueHandle <T> | Read only |
