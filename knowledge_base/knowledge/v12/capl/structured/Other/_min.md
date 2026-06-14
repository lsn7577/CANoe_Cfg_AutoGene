# _min

> Category: `Other` | Type: `function`

## Syntax

```c
long _min(long x, long y); // form 1
```

## Description

Returns the minimum of the parameters.

## Return Values

y < x ? y : x

## Example

```c
float result;
result = _min(1.0, _min(-3.0, 5.2)); // result == -3.0
```

## Availability

| Since Version |
|---|
