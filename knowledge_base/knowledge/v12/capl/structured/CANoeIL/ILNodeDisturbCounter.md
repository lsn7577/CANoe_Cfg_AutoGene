# ILNodeDisturbCounter

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbCounter(dbMessage aMessage, char aSigGroupName[], long counterType, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); // form 1
```

## Description

This function modifies the counter. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error

## Example

```c
// Disturbs the PDU counter, disturbance pattern: 100x random value,
// after the disturbance the counters next value bases on
// the last value before the disturbance has started.

variables {
  long countertype =0;
  long disturbanceMode= 2;  // A random value is transmitted as counter.
  long disturbanceCoun=100;
  long disturbanceValue=0;  // value will be ignored due to disturbance mode
  long continueMode=1;      // The counters next value bases on the last value
                            // before the disturbance has started.
}

on key 'a'{
  ILNodeDisturbCounter("PDU_A", counterType, disturbanceMode, disturbanceCount, disturbanceValue, continueMode);
}
```

## Availability

| Since Version |
|---|
