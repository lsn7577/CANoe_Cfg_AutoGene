# C2xEnableCV2xMode

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xEnableCV2xMode ( long appChannel );
```

## Description

This function enables the CV2x protocol for a channel. The function has to be called in the event handler on preStart.

## Parameters

| Name | Description |
|---|---|
| appChannel | 0 = current Channel 1 = Ath1 2 = Ath2 |

## Example

```c
on preStart()
{
  // enable CV2x for the first channel (Ath1)
  C2xEnableCV2xMode (1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | — | — | — | 4.0 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
