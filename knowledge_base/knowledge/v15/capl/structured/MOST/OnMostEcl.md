# OnMostEcl

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostEcl(long eclState);
```

## Description

The event procedure is called when the state of the Electrical Control Line has changed.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

## Parameters

| Name | Description |
|---|---|
| eclState | 0: Low1: High |

## Return Values

—

## Example

Output of ECL changes with time stamp.

```c
OnMostEcl(long eclState)
{
   write(„ECL state at %fs: %d“, mostEventTimeNs() / 1.0e9, eclState);
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
