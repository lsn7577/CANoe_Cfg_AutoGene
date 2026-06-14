# linSetChecksumCompatibility

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumCompatibility(long channel); // form 1
long linSetChecksumCompatibility(); // form 2
```

## Description

Switches the checksum calculation model of all frames that have at least one subscribed LIN 1.x node to the classic model.

## Parameters

| Name | Description |
|---|---|
| channel | The number of the LIN channel for which the checksum compatibility should be enabled. Value range: 1..32 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on prestart
{
  /*send and receive all frames that are received by at least one Lin 1.x node using the classic checksum model.*/
  linSetChecksumCompatibility();
}
on prestart
{
  /*send and receive all frames on channel 1 that are received by at least one Lin 1.x node using the classic checksum model.*/
  linSetChecksumCompatibility(1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.1 SP6 | 8.1 SP6 | 13.0 | 13.0 | — | 1.1 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
