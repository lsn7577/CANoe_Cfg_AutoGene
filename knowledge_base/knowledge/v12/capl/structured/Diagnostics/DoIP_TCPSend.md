# DoIP_TCPSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_TCPSend(dword payloadType, byte payload[], dword payloadLen);
```

## Description

Sends a DoIP PDU with valid layout on the open TCP connection.

## Return Values

Error code, e.g. connection not established yet.

## Example

```c
// When a vehicle is connected, send a non-standard frame to the peer
On key '1'
{
  BYTE payload[3] = { 0x11, 0x22, 0x33 };
  // the frame type 0xF222 is manufacturer-specific
  DoIP_TCPSend( 0xF222, payload, elcount( payload));
}
```

## Availability

| Since Version |
|---|
