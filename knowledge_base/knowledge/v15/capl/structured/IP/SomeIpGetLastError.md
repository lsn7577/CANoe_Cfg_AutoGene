# SomeIpGetLastError

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpGetLastError();
```

## Description

This function can be used to check whether the last called function of SOME/IP IL has been successfully executed. The call of this function does not reset the saved error.

In the Event of an error, a detailed error description can be read out using the SomeIpGetLastErrorText function.

## Example

```c
long retVal;

// resume sending messages
SomeIpILControlResume();

// check if last function was executed correct
if((retVal = SomeIpGetLastError()) != 0)
{
  write("SOME/IP IL error occured: Error code: %d", retVal);
} // if
```

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
