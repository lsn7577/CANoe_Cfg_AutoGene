# _max

> Category: `Other` | Type: `function`

## Syntax

```c
long _max(long x, long y); // form 1
```

## Description

Returns the maximum of the parameters.

## Return Values

y > x ? y : x

## Example

```c
float result;
result = _max(1.0, _max(-3.0, 5.2)); // result == 5.2
```

## Availability

| Since Version |
|---|
