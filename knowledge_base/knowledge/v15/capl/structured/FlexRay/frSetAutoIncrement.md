# frSetAutoIncrement

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetAutoIncrement (int channel, int slotId, int channelMask, int cycleStart, int cycleRepetition, dword flags, int increment_size, int increment_offset);
```

## Description

Part of the payload of a frame will be incremented automatically on each transmission.

The number of bytes used can be set to 1, 2 or 4.

The byte offset can also be set. The only format supported is Intel (Little Endian).

## Parameters

| Name | Description |
|---|---|
| channel | Channel number (or cluster number) |
| slotId | Slot number of the frame used. |
| 1 | Channel A |
| 2 | Channel B |
| 3 | Channel A+B |
| cycleStart, cycleRepetition | Cycle multiplexing parameter |
| flags | 1: Payload increment is switched on. All other values are reserved and must not be used. |
| increment_size | Number of bits used for the increment.8, 16 and 32 are valid values. |
| increment_size | increment_offset |
| 8 | 0,1,2,3... |
| 16 | 0,2,4,6,... |
| 32 | 0,4,8,... |

## Return Values

—

## Example

This example sends automatically a frame each second cycle in slot 30 with automatically incrementing a message counter:

```c
variables
{
   // The gMsg2 message for the static segment
   // that is sent on channel A only.
   frFrame ( 30, 0, 2) gMsg2;
   const BYTE gMsg2Flags    = 0;  // state-driven for repeated transmission
   const BYTE gMsg2Channel  = %CHANNEL%; // send on network the CAPL node is assigned to
   const BYTE gMsg2ChanMask = 1;  // send on FlexRay channel A
   const BYTE gMsg2Len      = 32; // 32 byte user data
   const int gMsg2IncSize   = 16; // 16 bit message counter
   const int gMsg2IncOffset = 0;  // Byte 0 is first byte of message counter
}
on preStart
{
   // Optionally prepare buffer for message gMsg2:
   gMsg2.MsgChannel = gMsg2Channel;
   gMsg2.FR_ChannelMask = gMsg2ChanMask;
   gMsg2.FR_Flags = gMsg2Flags;
   frSetPayloadLengthInByte(gMsg2, gMsg2Len);
   frSetSendFrame( gMsg2 );
   // Define the automatic icrementing message counter:
   frSetAutoIncrement(gMsg2.MsgChannel, gMsg2.FR_SlotID, gMsg2.FR_ChannelMask, gMsg2.FR_CycleOffset, gMsg2.FR_CycleRepetition, 1, gMsg2IncSize, gMsg2IncOffset);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
