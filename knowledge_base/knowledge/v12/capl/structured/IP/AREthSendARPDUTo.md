# AREthSendARPDUTo

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSendARPDUTo( dword aep, dword dstIPv4Addr, dword dstPort, dword bufferLength, char buffer[], dword headerID ); // form 1
```

## Description

Transmits data as AUTOSAR PDU via an Ethernet connection with activated Header option. Before transmitting each AUTOSAR PDU gets an Header that contains an ID and length.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
