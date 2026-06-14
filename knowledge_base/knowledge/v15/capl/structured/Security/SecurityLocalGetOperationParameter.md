# SecurityLocalGetOperationParameter

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGetOperationParameter(long key, qword value, char description[], dword descriptionLength)
```

## Description

Gets the value and description of the operation parameter of the specified key.

Which and how many operation parameters exist, which values are valid for an operation parameter differs from Security Source to Security Source.

Please refer to the Security Source specific manual to get more information about operation parameters. The manual can be opened from the Vector Security Manager on the OEM specific ribbon page.

## Parameters

| Name | Description |
|---|---|
| long key | the numeric identifier of the operation parameter. |
| qword value | the current value of the operation parameter. [out] |
| char description[] | the buffer for the description of the parameter. Usable for output and documentation of the parameter i.e. Test Units if the buffer is too small the description is truncated. [in/out] |
| dword descriptionLength | the length of the description buffer [in]. If the specified length is zero, no description is returned (faster). The value of descriptionLength is changed to the length of the description if the specified buffer is not completely used. [out] |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP4 | 11.0 SP4 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
