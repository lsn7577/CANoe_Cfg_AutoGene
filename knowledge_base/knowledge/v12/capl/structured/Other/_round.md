# _round

> Category: `Other` | Type: `function`

## Syntax

```c
long _round(double x);
```

## Description

Rounds x to the nearest integral number. The rounding method used is symmetric arithmetic rounding.

## Return Values

Nearest integral number.
For very large numbers, you should use _round64, which returns a 64 bit integer.

## Example

```c
long result;
result = _round(2.4); // result == 2
result = _round(2.5); // result == 3
result = _round(-3.5); // result == -4
```

## Availability

| Since Version |
|---|
