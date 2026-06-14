# SCC_SLAC_GetReservedField

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_GetReservedField ( dword Index, byte Data[], dword& DataSize )
```

## Description

Queries one of the reserved fields of the message. For a valid message, these fields must contain only zeroes.

## Return Values

Data and length of the reserved field.

## Availability

| Since Version |
|---|
