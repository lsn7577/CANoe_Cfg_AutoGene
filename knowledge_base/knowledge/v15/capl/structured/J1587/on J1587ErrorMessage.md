# on J1587ErrorMessage

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for an erroneous J1708 message. The error code is contained in J1587ErrorMessage::J1587_Error.

For passing this message to other node, output(this) must be called inside the event handler.

## Example

```c
on J1587ErrorMessage 50 //50 is Sender MID, can be dbNode name or MID
{
  write (“Msg with ErrorCode %d received, MID %d”, this.J1587_MID,
  this.J1587_Error);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | — | — | — | — |
| Restricted To | J1587 | J1587 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
