# EthGetThisTimeNS

> Category: `Obsolete` | Type: `function`

## Syntax

```c
qword EthGetThisTimeNS();
```

## Description

The function returns the time stamp of an received Ethernet packet in nanoseconds.

It is only usable in a CAPL callback function that had been registered with EthReceiveRawPacket or EthReceivePacket. It depends on the callback function, which part of the packet data is accessed by the function:

## Return Values

time stamp in nanoseconds

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceiveRawPacket( "OnEthRawPacket");
}
void OnEthRawPacket( LONG channel, LONG dir, LONG packetLength )
{
  float t;
  t = (float)EthGetThisTimeNS();
  write("Received packet at %f [sec]”, t );
}
```

## Availability

| Up to Version |
|---|
