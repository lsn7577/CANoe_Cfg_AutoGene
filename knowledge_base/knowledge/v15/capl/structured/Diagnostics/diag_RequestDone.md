# diag_RequestDone

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diag_RequestDone(); // form 1
long diag_RequestDone(char target[]); // form 2
```

## Description

The processing of the current diagnostic request completed. This function can be called if the diagnostic communication layer detected a timeout, i.e. the ECU did not respond in time. Calling this function allows the CAPL program to abort waiting for a response on the request.

## Parameters

| Name | Description |
|---|---|
| target | Stop processing of the current request sent to the ECU with this qualifier. |

## Return Values

Error code

## Example

```c
on timer tP2
{
  // No response was received within P2
  diag_RequestDone( gCurrentECU);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
