# KLine_Init5BaudEcuParams

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_Init5BaudEcuParams(dword 5BaudAddress, dword rate_10thBd, dword W1_us, dword W2_us, dword W3_us, dword W4_us, dword W4Min_us, dword W4Max_us, dword addressNot);
```

## Description

Initialize K-Line channel for reception of the 5 baud pattern.

Must be called in on prestart handler after KLine_CreateECURepresentation.

## Return Values

On success 0, otherwise a value less than 0.

## Availability

| Since Version |
|---|
