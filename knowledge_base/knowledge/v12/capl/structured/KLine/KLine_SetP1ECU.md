# KLine_SetP1ECU

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP1ECU(dword P1_us)
```

## Description

Sets the interbyte time of a response.

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on start
{
   KLine_SetP1ECU(10000); // P1 == 10 ms
}
```

## Availability

| Since Version |
|---|
