# on linMessage

> Category: `Obsolete` | Type: `event`

## Description

The event procedure on linMessage is called on the receipt of a valid LIN frame.

The keyword this and the selectors (see LIN: linMessage selectors) can be used to access the data of the frame that has just been received.

CAPL nodes are by default not transparent to LIN frames. This means that a CAPL node in the evaluation branch of the Measurement Setup will block the data flow to its right side. To propagate the received frame to a next node in a chain a call to output(this) can be used. However, please note that such a call from a CANoe's simulation setup node may lead to a recursion.

If for example a CAPL program contains the event procedures on linMessage 12 and on linMessage *, the procedure on linMessage 12 will be called up, when a frame with the identifier 12 is received. For all other frames the procedure on linMessage * will be called up.

## Example

Display in Write Window the transmission time for a frame from the database

Display in Write Window the header transmission time for a frame ID=0x33

Propagate all frames to a next chain node

```c
on linMessage MotorControl
{
writeLineEx(1, 1, "Entire frame transmission time: %d bit times", this.LIN_Fulltime);
}
on linMessage 0x33
{
writeLineEx(1, 1, "Frame header transmission time: %d bit times", this.LIN_HeaderTime);
}
// Warning: This code causes recursion when called 
 from CANoe Simulation Setup node
on linMessage *
{
this.RTR=1;
output(this); 
}
```

## Availability

| Since Version |
|---|

## Selectors

| linMessage | ../../LIN/Selectors/CAPLfunctionLINMessage.htm |
|---|---|
