# SetRawSignal

> Category: `Test` | Type: `function`

## Syntax

```c
void SetRawSignal(dbSignal aSignal, int64 value); // form 1
```

## Description

Sets the raw value of a signal. These functions can be used for signals with more than 32 bits length. If the signal name is statically known, you can also use $<signal>.raw64 since 7.5 Service Pack 2.

## Return Values

Form 2: 0 on success, -1 on error

## Availability

| Since Version |
|---|
