# on linCsError

> Category: `LIN` | Type: `event`

## Description

The event procedure on linCsError is called when a frame was transmitted without a failure, but with an incorrect checksum.

The keyword this and the selectors can be used to access the data of the event that has just been received.

## Example

Simulate checksum error and check how it is handled.

```c
on key 'c'
{
int index;
byte checksum;
linFrame MotorControl frmMotorControl;
   // set data byte values and calculate resulting checksum
   for (index=0; index < frmMotorControl.DLC; ++index)
{
frmMotorControl.byte(index) = 0xFF;
}
   // Set permanent CS error for the current frame
   linSetChecksumError(frmMotorControl.id, 
 1);
   // update response data
   frmMotorControl.RTR=0;
output(frmMotorControl);  
   // apply frame's header on the bus
   frmMotorControl.RTR=1;
output(frmMotorControl);
}
...
on linCsError
{
int index;
linFrame MotorControl frmMotorControl;
// compare correct checksum and the received one
   if (this.ID == frmMotorControl.ID)
{
// set data byte values and calculate correct checksum
      for (index=0; index < frmMotorControl.DLC; ++index)
{
frmMotorControl.byte(index) = this.byte(index);
}
      WriteLineEx(0,0,"received 
 checksum=%d", getChecksum(this));
      WriteLineEx(0,0,"correct checksum=%d", getChecksum(frmMotorControl));
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

| linCsError |  |
|---|---|
| linCsError | ../Selectors/CAPLfunctionLINCSError.htm |
