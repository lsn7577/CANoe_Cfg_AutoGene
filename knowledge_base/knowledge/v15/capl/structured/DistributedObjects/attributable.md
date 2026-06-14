# attributable

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
attributable
```

## Description

The type of objects that can have attributes. This type is a supertype of distObjRef *, distObjMemberRef *, distObjInterface *, distObjInterfaceMember *, and virtNet.

The type is not available for user declarations.

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
