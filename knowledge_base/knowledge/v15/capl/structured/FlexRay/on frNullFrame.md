# on frNullFrame

> Category: `FlexRay` | Type: `event`

## Description

The event procedure is called if a Null Frame is received in the specified slot and cycle.

If two Null Frames are received in the corresponding slot (on Channel A and on B), then the event procedure is called twice (once for each frame).

An optional channel parameter for event filtering can be assigned to all handlers:

An optional qualifier can be used to assign the handler to a specific network:

## Example

The following program reacts on Null Frames and prints them in the Write Window.

```c
variables
{
   const int cWriteTextSize = 512;
   char writeTxt[cWriteTextSize];
}
float getTime (float time)
{
   return time / 1000000000.0;
}
void myprint(char text[])
{
   write("%s", text);
}
on frNullFrame *
{
   snprintf(writeTxt, cWriteTextSize, "%10.6f: on FRNullFrame in slot %2d in cycle %2d on channel %2d with mask %d with Type %2d, Flags 0x%02x, Status 0x%02x, Simulated %d.", getTime(messageTimeNS(this)), this.FR_SlotID, this.FR_Cycle, (int)this.MsgChannel, this.FR_ChannelMask, this.Type, this.FR_Flags, this.FR_Status, this.Simulated);
   myprint(writeTxt);
   output(this); // only required in Measurement Setup
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 SP2 | 6.0 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| on frFrame | CAPLfunctionOnFRFrame.htm |
|---|---|
