# GetPDUsTPIPv4DstAddr

> Category: `Other` | Type: `function`

## Syntax

```c
long GetPDUsTPIPv4DstAddr(this, dword &IPv4DestinationAddress);
```

## Description

This function can only be used within a on PDU handler. If the PDU was received via IPv4, with this function the IPv4 destination address can be requested.

## Return Values

0: Data access successful.

## Availability

| Since Version |
|---|
