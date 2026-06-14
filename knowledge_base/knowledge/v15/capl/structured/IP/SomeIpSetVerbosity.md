# SomeIpSetVerbosity

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetVerbosity( long verbosity);
```

## Description

Sets the verbosity level of SOME/IP IL messages in the Write Window.

## Parameters

| Name | Description |
|---|---|
| verbosity | Verbosity level: 0: Silent - do not write messages to the Write Window 1: Error - write only error messages (default) 2: Warning - write warning and error messages 3: Information - write information, warning and error messages |

## Example

```c
on key '0'
{
  char buffer[1024];
  // set verbosity level to "Silent" mode
  if(SomeIpSetVerbosity(0) == 0)
  {
    write("SOME/IP IL verbosity level was set to mode \"silent\"");
  } // if
  else
  {
    // check if last function was executed correct
    SomeIpGetLastErrorText(elcount(buffer),buffer);
    write("Error setting verbosity level if SOME/IP IL: %s", buffer);
  } // else
}
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
