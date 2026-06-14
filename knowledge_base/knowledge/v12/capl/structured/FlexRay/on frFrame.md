# on frFrame

> Category: `FlexRay` | Type: `event`

## Syntax

```c
on frFrame *
```

## Description

This event procedure is called after a valid data frame has been received in the specified slot and cycle.

If two valid data frames are received in the according slot (on channel A and on B) then the event procedure is called up twice (once for each frame).

An optional channel parameter for event filtering can be assigned to all handlers:

In this example, the event procedure is only called for frames whose application channel is 2 and its ID is 5.

on frFrame MsgChannel2.(5,0,1)

An optional qualifier can be used to assign the handler to a specific network:

In this example, the event procedure is only called for specific frames from the application channel that is named "network" in the Simulation Setup (only available for CANoe).

on frFrame network.<frame name>

## Example

The following program reacts on received frames and prints them in the Write Window.

```c
variables
{
   const int cWriteTextSize = 512;
   char writeTxt[cWriteTextSize];
}
float getTime (float time)
{
   // convert NS to SEC:
   return time / 1000000000.0;
}
void myprint(char text[])
{
  write("%s", text);
}
on frFrame *
{
   snprintf(writeTxt, cWriteTextSize, "%10.6f: on FRFrame in slot %2d in cycle %2d on channel %2d with mask %d with Type %2d, Flags 0x%02x, Status 0x%02x, Simulated %d.", getTime(messageTimeNS(this)), this.FR_SlotID, this.FR_Cycle, (int)this.MsgChannel, this.FR_ChannelMask, this.Type, this.FR_Flags, this.FR_Status, this.Simulated);
   myprint(writeTxt);
   output(this); // only required in Measurement Setup
}
```

## Availability

| Since Version |
|---|

## Selectors

| Note The Time selector is not available when executing CAPL programs directly on an interface hardware (CAPL-on-Board). |
|---|
