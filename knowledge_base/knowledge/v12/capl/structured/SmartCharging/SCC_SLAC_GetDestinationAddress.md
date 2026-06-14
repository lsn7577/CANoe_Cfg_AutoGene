# SCC_SLAC_GetDestinationAddress

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_GetDestinationAddress ( byte[] MACAddress )
```

## Description

Returns the destination MAC address of a SLAC message, to the output buffer

The destination address may differ from the simulation node’s address when the node is in passive mode. This function is intended to allow filtering for the node’s address in this case.

## Return Values

—

## Availability

| Since Version |
|---|
