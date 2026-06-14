# diagGetCommunicationErrorString

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetCommunicationErrorString( long communicationError, char descriptionOut, dword bufferLen);
```

## Description

Returns a description for the given communication error.

## Parameters

| Name | Description |
|---|---|
| communicationError | Value returned by diagGetLastCommunicationError. |
| descriptionOut | Output buffer for the meaning of the communication error. |
| bufferLen | Capacity of the output buffer. |

## Return Values

Number of characters written to the buffer.

## Example

```c
...
if (0 == TestWaitForDiagResponse( req, 2000))
{
  char errStr[100];
  err = DiagGetLastCommunicationError();
  DiagGetCommunicationErrorString( err, errStr, elcount(errStr));
  write("LastCommunicationError=%d - %s", err, errStr);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | — | — | — | 2.1 SP3 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
