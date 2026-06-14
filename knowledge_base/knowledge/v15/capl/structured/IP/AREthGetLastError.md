# AREthGetLastError

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthGetLastError();
```

## Description

This function can be used to check whether the last called function of AUTOSAR Eth IL has been successfully executed. The call of this function does not reset the saved error.

In the Event of an error, a detailed error description can be read out using the AREthGetLastErrorText function.

## Example

```c
long retVal;

// resume sending messages
AREthILControlResume();

// check if last function was executed correct
if((retVal = AREthGetLastError()) != 0)
{
  write("AUTOSAR Eth IL error occured: Error code: %d", retVal);
} // if
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
