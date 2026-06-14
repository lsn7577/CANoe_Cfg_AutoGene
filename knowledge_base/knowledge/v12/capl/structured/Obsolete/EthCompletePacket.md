# EthCompletePacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthCompletePacket( long packet );
```

## Description

The function completes a packet before sending it with EthOutputPacket. It calculates the fields that are marked with CompleteProtocol in the protocol overview, e.g. checksum, lengths, etc.

## Return Values

0 or error code

## Example

```c
see example of EthInitPacket
```

## Availability

| Up to Version |
|---|
