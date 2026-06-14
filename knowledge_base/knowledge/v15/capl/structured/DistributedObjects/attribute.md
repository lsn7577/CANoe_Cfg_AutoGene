# attribute

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
attribute *
attribute int32
attribute uint32
attribute int64
attribute uint64
attribute double
attribute string
```

## Description

The types of attributes for distributed objects.

These types are not available for user declarations.

## Parameters

| Name | Description |
|---|---|
| int32 | 32-Bit signed integer attribute. Access requires type long in CAPL. |
| unit32 | 32-Bit unsigned integer attribute. Access requires type dword in CAPL. |
| int64 | 64-Bit signed integer attribute. Access requires type int64 in CAPL. |
| unit64 | 64-Bit unsigned integer attribute. Access requires type qword in CAPL. |
| doube | 64-Bit floating point attribute. Access requires type double in CAPL. |
| string | String attribute. Access requires a large enough char array in CAPL. |

## Example

```c
// vCDL
version 1.4;
namespace ExampleNamespace
{
  interface ExampleInterface
  {
    internal data int32 ExampleMember;
  }
  ExampleInterface ExampleObject;
  attribute int32 ExampleIntAttr { mutable; }
  attribute string ExampleStringAttr { mutable; }
}

// CAPL
on start
{
  dword val;

  // reference attributes in CAPL
  ExampleNamespace::ExampleIntAttr;
  ExampleNamespace::ExampleStringAttr;

  // use setAttribute function to set the value of an attribute at an object
  setAttribute(ExampleInterface, ExampleNamespace::ExampleStringAttr, "test");
  setAttribute(ExampleInterface.ExampleMember, ExampleNamespace::ExampleIntAttr, 42);
  setAttribute(ExampleObject, ExampleNamespace::ExampleStringAttr, "test");
  setAttribute(ExampleObject.ExampleMember, ExampleNamespace::ExampleIntAttr, 42);

  // use getAttribute function to read the value of an attribute
  getAttribute(ExampleObject.ExampleMember, _SystemAttributes::AutoSubscribe, val);
  write("AutoSubscribe: %d", val);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | 15 | 15 | 15 | 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
