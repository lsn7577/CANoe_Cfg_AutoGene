# distObjRef::IsConnected

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
dword distObjRef::IsConnected(); // form 1
dword distObjMemberRef::IsConnected(); // form 2
```

## Description

Form1: Checks if every member of the object is connected to its virtual network.

Form2: Checks if the object member is connected to its assigned virtual network.

## Example

Example Form 1

Example Form 2

```c
on start
{
  distObjRef * object = ExampleObject;
  if (object.IsConnected())
  {
    write(“Connected”);
  }
}
on start
{
  distObjRef ExampleInterface object = ExampleObject;
  if (object.ExampleMember.IsConnected())
  {
    write(“Connected”);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | 13.0 | 14 | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
