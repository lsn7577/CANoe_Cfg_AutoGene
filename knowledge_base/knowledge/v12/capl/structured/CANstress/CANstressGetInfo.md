# CANstressGetInfo

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressGetInfo( char softwareVersion[], long swVersionBufLen, char firmwareVersion[], long fwVersionBufLen, char serialNumber[], long snBufLen, char canInterface1[], long if1BufLen, char canInterface2[], long if2BufLen );
```

## Description

Delivers information about CANstress software and the connected CAN hardware.

## Return Values

0: On successful call.

## Availability

| Since Version |
|---|
