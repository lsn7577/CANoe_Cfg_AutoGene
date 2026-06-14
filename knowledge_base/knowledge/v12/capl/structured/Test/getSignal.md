# getSignal

> Category: `Test` | Type: `function`

## Syntax

```c
float getSignal(Signal aSignal);
```

## Description

Gets the value of a signal.

## Return Values

If the signal is available (already appeared on the bus), this function returns the current signal value.

## Example

You have to use at minimum one more object to identify the signal uniquely. It could be any object from the list of possible objects, see hints for resolving signal ambiguities.

```c
float value;
value = getSignal(OnOff);
```

## Availability

| Since Version |
|---|
