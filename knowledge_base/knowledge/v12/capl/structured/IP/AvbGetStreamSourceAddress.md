# AvbGetStreamSourceAddress

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetStreamSourceAddress(dword listenerOrTalkerHandle, byte retStreamSourceAddress[]);
```

## Description

The function retrieves the stream’s Source Address of the Listener or Talker. This usually is a 48 bit MAC address defining the sourcing system of the stream and is part of the Stream Identifier (ID).

This address is not the source MAC address of the Ethernet layer.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
