# SCC_GetMeterInfoData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetMeterInfoData ( char MeterID, float& MeterReading, byte SigMeterReading, long& MeterStatus, long& TMeter )
```

## Description

Gets data from MeterInfo.

## Return Values

Returns Data assigned to the meter: ID (32 characters), current meter reading in [Wh], signature, status and timestamp in UNIX format Length of signature is dependent on the encryption algorithm.

## Availability

| Since Version |
|---|
