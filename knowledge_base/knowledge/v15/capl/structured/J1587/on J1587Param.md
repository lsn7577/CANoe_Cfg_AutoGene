# on J1587Param

> Category: `J1587` | Type: `event`

## Description

Defines the event handler for a valid J1587 parameter, the this pointer is of type J1587Param.

## Example

```c
on J1587Param TextMessageAcknowledged
{
  if (this.MID == gECU_MID)
  {
    if (this.MessageDisplayed == 1)
    {
      gDisplayState = kDisplayed;
    }
    else
    {
      gDisplayState = kTimeout;
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | — |
| Restricted To | J1587 | J1587 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
