# diagGetCurrentEcu

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCurrentEcu (char[] qualifier, dword bufferLen)
```

## Description

Gets the qualifier of the ECU for which the last event was processed, especially if a response was received from this ECU. This function can be used to determine the ECU that responded to a functional request.

In a diagnostics event handler in the measurement setup this function will return the target of request primitives and the source of response primitives (the other communication partner is always a tester).

## Parameters

| Name | Description |
|---|---|
| qualifier | Output buffer |
| bufferLen | Length of the output buffer |

## Return Values

Error code or length of the name provided.

## Example

```c
on diagResponse *
{
  char ecu[100];
  diagGetCurrentEcu( ecu, elcount(ecu));
  write( "Received response from %s", ecu);
}

on key 'a'
{
  // Diagnostic description with ECU qualifier 'FunctionalGroup' configured for Functional Group Requests (FGR)
  diagRequest FunctionalGroup.DefaultSession_Start req1;

  diagSendRequest( req1); // Request is sent to functional group, therefore multiple ECUs may respond
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.1 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
