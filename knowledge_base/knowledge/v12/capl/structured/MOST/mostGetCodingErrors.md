# mostGetCodingErrors

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetCodingErrors (long channel)
```

## Description

Returns the number of coding errors since measurement start or the last time this function was called.

Calling this function resets the counter in the hardware! The total number of coding errors during measurement is displayed in Bus Statistics Window.

## Return Values

>= 0: Number of coding errors.

## Availability

| Since Version |
|---|
