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

| Since Version |
|---|

## Selectors

| linCsError | ../Selectors/CAPLfunctionLINCSError.htm |
|---|---|
