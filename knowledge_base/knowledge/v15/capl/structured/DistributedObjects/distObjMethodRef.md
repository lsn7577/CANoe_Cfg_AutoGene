# distObjMethodRef

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjMethodRef <Member>
```

## Description

References a distributed object method member. This type cannot be used in declarations. This is a subtype of distObjMemberRef <Member>.

## Parameters

| Name | Description |
|---|---|
| Member | Path of a distributed object method member. |

## Example

```c
on start
{
  distObjRef ExampleInterface object = ExampleObject;
  $object.ExampleMethodMember.AutoAnswerMode = 0;
  $object.ExampleMethodMember.AutoAnswerTimeNS = 100;
  object.ExampleMethodMember.CallAsync();
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
