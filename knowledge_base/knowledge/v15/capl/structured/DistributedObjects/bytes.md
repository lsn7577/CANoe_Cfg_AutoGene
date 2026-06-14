# bytes

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
bytes
```

## Description

The corresponding CAPL type for the bytes type in vCDL. Reading and writing is done via memcpy overloads. The length of a bytes value can be determined with the elCount operator.

This type is not available for user declarations.

## Example

```c
// vCDL
version 1.4;
namespace ExampleNamespace
{
  object ExampleObject
  {
    internal data bytes ExampleMember;
  }
}

// CAPL
on start
{
  byte buffer[100];

  // write whole buffer to bytes value
  memcpy($ExampleNamespace::ExampleObject.ExampleMember, buffer);
  // write part of buffer to bytes value
  memcpy($ExampleNamespace::ExampleObject.ExampleMember, buffer, 42);
  // read from bytes value
  memcpy(buffer, $ExampleNamespace::ExampleObject.ExampleMember);
  write("Length: %d", elCount($ExampleNamespace::ExampleObject.ExampleMember));
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
