# AvbSetVerbosity

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbSetVerbosity(long verbosity);
```

## Description

Sets the verbosity level of AVB IL messages in the Write Window.

## Parameters

| Name | Description |
|---|---|
| verbosity | Verbosity level: 0: Silent - do not write messages to the Write Window 1: Error - write only error messages (default) 2: Warning - write warning and error messages 3: Information - write information, warning and error messages |

## Return Values

Number of copied characters.

## Example

```c
on key '0'
{
  char buffer[1024];
  // set verbosity level to "Silent" mode
  if (AvbSetVerbosity(0) == 0)
  {
    write("AVB IL verbosity level was set to mode
    \"silent\"");
  }
  else
  {
    // check if last function was successfully executed
    AvbGetLastErrorText(elcount(buffer), buffer);
    write("Error setting verbosity level if AVB IL: %s", buffer);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
