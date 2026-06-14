# ARILFaultInjectionDisturbUpdateBit

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbUpdateBit dbSignal, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Disturbs the Update Bit of a signal or signal group (see Update Bit).

The function without the parameter for the signal group will only disturb update bits of signals.

The function with the parameter for the signal group will only disturb update bits of signal groups.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
