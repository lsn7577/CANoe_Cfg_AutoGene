# LINtp_FirstFrameIndication

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_FirstFrameIndication(long sender, long receiver, long announcedLen);
```

## Description

Indicates the start of a segmented reception.

## Parameters

| Name | Description |
|---|---|
| sender | Address of sender node, or 0 for master. |
| receiver | Address of receiver node, or 0 for master. |
| announcedLen | Number of bytes to be expected. |

## Return Values

—

## Example

```c
LINtp_FirstFrameIndication(long sender, long receiver, long announcedLen)
{
  write( "Start reception of %d bytes", announcedLen);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
