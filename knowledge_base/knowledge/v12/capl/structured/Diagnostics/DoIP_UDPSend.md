# DoIP_UDPSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_UDPSend(byte data[], dword length);
```

## Description

Sends given raw data to peer(s) as UDP frame.

## Return Values

Error code

## Example

```c
// Send an invalid identification request to a specific vehicle
// that must ignore it
BYTE rawData[8] = { 0x02,0xFF /* wrong! */, 0x00,0x01, 0x00,0x00,0x00,0x00};
DoIP_UDPSend( "169.254.123.45", rawData, elcount( rawData));
```

## Availability

| Since Version |
|---|
