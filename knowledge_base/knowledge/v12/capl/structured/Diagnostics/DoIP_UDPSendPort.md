# DoIP_UDPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_UDPSendPort(char IPaddress[], word port, byte data[], dword length);
```

## Description

Send given raw data to peer(s) as UDP frame.

## Return Values

Error code

## Example

```c
// Send an invalid identification request to a non-standard port of a 
// specific vehicle that must ignore it
BYTE rawData[8] = { 0x02,0xFF /*wrong!*/, 0x00,0x01, 0x00,0x00,0x00,0x00};
DoIP_UDPSendPort( "169.254.123.45", 13401 /* non standard */, rawData, elcount( rawData));
```

## Availability

| Since Version |
|---|
