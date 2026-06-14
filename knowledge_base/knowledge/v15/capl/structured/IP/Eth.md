# Eth

> Category: `IP` | Type: `function`

## Syntax

```c
Eth <Ethernet Channel Number>;
```

## Description

Can be used to get the status and statistics of the Ethernet link.

Use ethResetStatistics to reset the statistics values.

## Parameters

| Name | Description |
|---|---|
| Ethernet Channel Number | Channel number 1..32. |

## Example

```c
switch(Eth1.status)
{
  case 0:
    write("Ethernet link on Eth1 is down” );
    break;
  case 1:
    write("Ethernet link on Eth1 is up with %dMBit/sec“, Eth1.bitrate/1000);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 11.0 (Statistics selectors) | 8.5 11.0 (Statistics selectors) | 13.0 | — | — | 2.0 SP2 3.0 (Statistics selectors) |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
