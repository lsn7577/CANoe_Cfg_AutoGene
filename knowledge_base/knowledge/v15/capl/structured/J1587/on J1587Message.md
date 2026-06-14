# on J1587Message

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for a valid J1708 message, the thispointer is of type J1587Message.

For passing this message to other node, output(this) must be called inside the event handler.

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  J1587Param 0 param;
  if (GetParameterByPID(this, 30, param) == 0)
  {
    output(this);
  }
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
