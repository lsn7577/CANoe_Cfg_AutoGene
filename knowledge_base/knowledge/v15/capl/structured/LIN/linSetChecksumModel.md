# linSetChecksumModel

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumModel(long channel, long frameID, long checksumModel); // form 1
long linSetChecksumModel(long frameID, long checksumModel); // form 2
```

## Description

Sets the checksum calculation model of a single frame.

## Parameters

| Name | Description |
|---|---|
| channel | The channel for which the checksum model of the frame should be changed. Value range: 1..32 |
| frameId | The unprotected identifier of the frame. Value range: 0 .. 63 (excluding 60 and 61). |
| checksumModel | Value range: 0..1 0: classic (LIN 1.x) checksum model 1: enhanced (LIN 2.x) checksum model |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on prestart
{
  /*send and receive the frame with the ID “4” using the classic checksum model*/
  linSetChecksumModel(4,0);
}
on prestart
{
  /*send and receive the frame with the ID “4” on channel 1 using the classic checksum model*/
  linSetChecksumModel(1,4,0);
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
