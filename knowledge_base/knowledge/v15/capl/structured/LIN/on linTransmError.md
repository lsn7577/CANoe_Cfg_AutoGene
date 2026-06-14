# on linTransmError

> Category: `LIN` | Type: `event`

## Description

The event procedure on linTransmError is called when no Slave responded to a transmission request.

The keyword this and the selectors (see Option .LIN: linTransmError selectors) can be used to access the data of the event that has just been received.

## Example

Handle transmission error for a certain frame on channel 1:

```c
on linTransmError
{
if (this.MsgChannel == 1 && this.ID == 0x33) {
…
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | LIN | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| linTransmError |  |
|---|---|
| linTransmError | ../Selectors/CAPLfunctionLINTransmError.htm |
