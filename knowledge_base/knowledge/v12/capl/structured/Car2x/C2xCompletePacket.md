# C2xCompletePacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xCompletePacket( long packet );
```

## Description

This function completes a packet before sending it with C2xOutputPacket. It calculates the fields that are marked with CompleteProtocol in the protocol overview, e.g. checksum, lengths, etc.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
