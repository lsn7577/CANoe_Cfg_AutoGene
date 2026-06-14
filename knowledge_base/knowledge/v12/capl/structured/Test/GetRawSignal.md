# GetRawSignal

> Category: `Test` | Type: `function`

## Syntax

```c
Int64 GetRawSignal(dbSignal aSignal); // form 1
```

## Description

Retrieves the current raw value of a signal. These functions can be used for signals with more than 32 bits length. If the signal name is statically known, you can also use $<signal>.raw64 since 7.5 Service Pack 2.

## Return Values

Form 1: the current raw value of the signal

## Availability

| Since Version |
|---|
