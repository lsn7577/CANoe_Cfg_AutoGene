# frSetAutoIncrement

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetAutoIncrement (int channel, int slotId, int channelMask, int cycleStart, int cycleRepetition, dword flags, int increment_size, int increment_offset);
```

## Description

Part of the payload of a frame will be incremented automatically on each transmission.The number of bytes used can be set to 1, 2 or 4.

The byte offset can also be set. The only format supported is Intel (Little Endian).

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

| Since Version |
|---|
