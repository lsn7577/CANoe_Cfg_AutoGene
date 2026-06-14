# setJitter

> Category: `Other` | Type: `function`

## Syntax

```c
setJitter(int min, int max);
```

## Description

The Jitter interval for the timers of a network node can be set with this function. The two values may lie between –10000 and 10000 (corresponds to –100.00% to 100.00%). If one of the two values does not lie within this range, a message is output in the Write Window.

## Parameters

| Name | Description |
|---|---|
| min | Integer for the lower interval limit. |
| max | Integer for the upper interval limit. |

## Return Values

—

## Example

```c
...
// Set a Jitter with +–4 percent
setJitter(-400, 400);
...
...
// Set a Jitter with +–4 percent
// and a Drift of 17 percent
setJitter(1300, 2100);
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 3.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
