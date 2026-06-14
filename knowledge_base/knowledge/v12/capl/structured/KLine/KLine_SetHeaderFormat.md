# KLine_SetHeaderFormat

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetHeaderFormat(long useAddresses, long forceLengthByte)
```

## Description

Configures the used header format.

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
KLine_SetHeaderFormat(0, 0); // A one byte header will be sent.
KLine_SetHeaderFormat(0, 1); // A two byte header will be sent.
KLine_SetHeaderFormat(1, 0); // A three byte header will be sent.
KLine_SetHeaderFormat(1, 1); // A four byte header will be sent.
```

## Availability

| Since Version |
|---|
