# distObjRef

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjRef *
distObjRef <Interface>
distObjRef reverse<<Interface>>
```

## Description

References a distributed object that is derived from the denoted interface.

## Parameters

| Name | Description |
|---|---|
| Interface | The optionally qualified name of a distributed object interface. |
| reverse<Interface> | The reverse of a distributed object interface. |

## Example

```c
on start
{
  distObjRef reverse<::ExampleNamespace::ExampleInterface> x;
  distObjRef * y[42], z = ExampleNamespace::ExampleObject;
  x = (distObjRef reverse<ExampleInterface>)z;
  if (x.IsValid)
  {
    y[0] = x;
  }
  func(y[0]);
}

void func(distObjRef *& p)
{
  write("Path: %s", p.Path);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | 15 | 14 | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
