# ILCalculateChecksum

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILCalculateChecksum (char pduNamme[], long type, BYTE payload[], long payloadLength, BYTE crc [])
```

## Description

Calculates the corresponding CRC checksum based on the payload. The correct offset is calculated from the database using the PDU name.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
