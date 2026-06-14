# distObjInterfaceMember

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjInterfaceMember *
distObjInterfaceMember <Interface Member>
```

## Description

The types of distributed object interface members. They are only useful for specifying value sets at type handlers (i.e. any_value_update, …) and for accessing attributes at distributed object interface members.

All distObjInterfaceMember types are singleton types.

The types are not available for user declarations.

## Parameters

| Name | Description |
|---|---|
| <Interface Member> | The path of the interface member. |

## Example

```c
// vCDL
version 1.4;
namespace SomeNamespace
{
  [Binding="Abstract", AutoSubscribe=false]
  interface SomeInterface 
  {
    consumed data int32 SomeData;
  }
  SomeInterface SomeObject;
  reverse<SomeInterface> OtherObject;
}

// CAPL
on start 
{
  char str[100];
  getAttribute(SomeInterface.SomeData, _SystemAttributes::Binding, str);
  write("Binding: %s", str);
}
on key 'a'
{
  SomeObject.SomeData.subscribe();
}
on key 'b'
{
  $OtherObject.SomeData += 1;
}
on any_value_update SomeInterface.SomeData
{
  write("value of %s.SomeData updated to %d", this.object.Path, $this.value);
}
on any_value_update SomeInterface.SomeData.SubscriptionState
{
  write("subscription state of %s.SomeData updated", this.object.Path);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 13.0 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
