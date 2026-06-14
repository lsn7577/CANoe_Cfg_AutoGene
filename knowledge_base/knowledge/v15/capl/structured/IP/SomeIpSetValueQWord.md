# SomeIpSetValueQWord

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetValueQWord( dword objectHandle, char valuePath[], qword value );
```

## Description

This function can be used to set a raw value in the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Parameters

| Name | Description |
|---|---|
| objectHandle | Handle to a SOME/IP IL object, which must be completely described in the FIBEX database.The following objects are supported. Messages Fields Method calls: Handle to a method call that was created with SomeIpCreateMethodCall. |
| valuePath | Access path of the value to be set. |
| value | Raw Value |

## Example

See SomeIpSetValueDWord

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
