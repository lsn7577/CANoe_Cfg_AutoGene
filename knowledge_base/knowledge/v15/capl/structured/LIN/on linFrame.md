# on linFrame

> Category: `LIN` | Type: `event`

## Description

The event procedure on linFrame is called on the receipt of a valid LIN frame.

The keyword this and the selectors (see LIN: linFrame selectors) can be used to access the data of the frame that has just been received.

CAPL nodes are by default not transparent to LIN frames. This means that a CAPL node in the evaluation branch of the Measurement Setup will block the data flow to its right side. To propagate the received frame to a next node in a chain a call to output(this) can be used. However, please note that such a call from a CANoe's simulation setup node may lead to a recursion.

## Example

Display in Write Window the transmission time for a frame from the database

Display in Write Window the header transmission time for a frame ID=0x33

```c
on linFrame MotorControl
{
writeLineEx(1, 1, "Entire frame transmission time: %d bit times", this.LIN_Fulltime);
}
on linFrame 0x33
{
writeLineEx(1, 1, "Frame header transmission time: %d bit times", this.LIN_HeaderTime);
}
// Warning: This code causes recursion when called 
 from CANoe Simulation Setup node
on linFrame *
{
this.RTR=1;
output(this); 
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | — | 2.2 |
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

| linFrame |  |
|---|---|
| linFrame | ../Selectors/CAPLfunctionLINMessage.htm |
