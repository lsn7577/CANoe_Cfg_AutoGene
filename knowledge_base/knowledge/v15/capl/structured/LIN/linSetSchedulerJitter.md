# linSetSchedulerJitter

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetSchedulerJitter (long mode); // form 1
long linSetSchedulerJitter (long mode, long jitterInMicSecs); // form 2
```

## Description

Sets/resets the jitter mode and the jitter of the LIN hardware scheduler. (the channel is determined by the CAPL program context).

## Parameters

| Name | Description |
|---|---|
| mode | 0: deactivates the jitter; 1: sets the min-/max-mode; the minimum (0) and the maximum (specified value) jitter will be used alternatively 2: sets the random jitter-mode; the jitter-offset will be equally distributed in the min/max range |
| jitterInMicSecs | The jitter in microseconds to be used. Default: Jitter value from LDF. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'j'
{
if (0!=linSetSchedulerJitter(1))
{
// for the next LIN hardware scheduler will use jitter specified in the LDF
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
