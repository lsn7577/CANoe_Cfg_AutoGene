# OnMostEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEclSequence(long state);
```

## Description

The event procedure is called before the beginning and after the end of a sequence on the Electrical Control Line.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Parameters

| Name | Description |
|---|---|
| state | 0: ECL sequence is stopped1: ECL sequence is started |

## Return Values

—

## Example

Output of ECL sequence changes with time stamp.

```c
OnMostEclSequence(long state)
{
   if(state == 0)
      write(„ECL sequence stopped at %fs“, MostEventTimeNs() / 1.0e9);
   else
      write(„ECL sequence started at %fs“, MostEventTimeNs() / 1.0e9);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 SP2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
