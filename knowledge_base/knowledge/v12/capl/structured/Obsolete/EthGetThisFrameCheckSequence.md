# EthGetThisFrameCheckSequence

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword EthGetThisFrameCheckSequence();
```

## Description

The function returns the frame check sequence (fcs) of a received Ethernet packet.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  BYTE emptyMacId[6] = { 0x00,0x00,0x00,0x00,0x00, 0x00};
  EthReceiveRawPacket( 0x7, emptyMacId, emptyMacId, 0x0000, "OnEthRawPacket");
}
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength)
{
dword fcs;
fcs = EthGetThisFrameCheckSequence();
write("Received packet with fcs %d", fcs );
}
```

## Availability

| Up to Version |
|---|
