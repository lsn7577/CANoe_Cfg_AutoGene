# TestFRILCalculateChecksum

> Category: `Test` | Type: `function`

## Syntax

```c
long TestFRILCalculateChecksum (char pduNamme[], long type, BYTE payload[], long payloadLength, BYTE crc []);
```

## Description

Calculates the corresponding CRC checksum based on the payload. The correct offset is calculated from the database using the PDU name.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
