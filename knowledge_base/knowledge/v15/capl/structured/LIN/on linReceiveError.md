# on linReceiveError

> Category: `LIN` | Type: `event`

## Description

The event procedure on linReceiveError is called when an error occurred during a frame transmission. The exact reason of the error is specified by lin_StateReason selector.

The keyword this and the selectors can be used to access the data of the event that has just been received.

## Example

```c
linFrame MotorControl frmMotorControl;
...
   // Simulate Receive Error by setting wrong response length
if (linSetRespLength (frmMotorControl.ID, frmMotorControl.DLC) 
 != 0)
{
// from now on a receive error notified for the MotorControl frame
...
}
...
// Handle the error
on linReceiveError
{
int state, reason;
if (this.lin_ShortError != 0)
{
      // The received data was too short. No additional info is available.
...
}
else
{
      // extract identifier of LIN hardware state at the time the error has occurred
      state = this.lin_StateReason & 0x0F;
      // extract identifier of reason caused the error
      reason = this.lin_StateReason & 0xF0;
...
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

| linReceiveError |  |
|---|---|
| linReceiveError | ../Selectors/CAPLfunctionLINReceiveError.htm |
