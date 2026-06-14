# trigger

> Category: `Other` | Type: `function`

## Syntax

```c
void trigger();
```

## Description

Sends a trigger event to all CANoe Logging or Trigger Blocks.

For a Logging Block, the trigger event starts and stops logging, depending on

set in the Trigger Configuration dialog of this block.

For a trigger block, the trigger event starts and stops the data stream (like a filter) for the whole analysis branch or a single analysis window, depending also on trigger mode and trigger conditions in the Trigger Configuration dialog.

## Return Values

—

## Example

```c
on message 100 
{
  write("logging start");
  trigger(); // start logging
  setTimer(logging,1000); // for 1000 ms
}

on timer logging
{
  trigger(); // Stop logging
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
