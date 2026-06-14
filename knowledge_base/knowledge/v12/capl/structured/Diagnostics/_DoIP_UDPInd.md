# _DoIP_UDPInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_UDPInd( char IPaddress[], WORD port, BYTE data[]);
```

## Description

An UDP packet was received. All packets are forwarded to this callback function, and it can decide whether processing of the packet stops, or is continued.

The sender IP address and source port is given as first arguments.

This callback is called for every packet before any other processing is per-formed. If only packets unknown to the DoIP implementation shall be processed, use _DoIP_UDPDataInd.

## Return Values

0: Continue normal processing of the packet.

## Example

```c
// If packet with payload type 0xF000 is received, answer with a 0xF001 packet
// and stop processing. Otherwise process the packet normally.
long _DoIP_UDPInd( char IPaddress[], WORD port, BYTE data[])
{
  WORD payloadType;
  BYTE response[2] = { 0x12, 0x34 };
  if( elcount(data) < 8)
    return 0;
  payloadType = (data[2] << 8) + data[3];
  if( payloadType != 0xF000)
    return 0;

  DoIP_UDPSendPort( IPaddress, port, 0xF001, response, elcount( response));
  return -1; // we process this frame
}
```

## Availability

| Since Version |
|---|
