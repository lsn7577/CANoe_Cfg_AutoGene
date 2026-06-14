# stop

> Category: `Other` | Type: `function`

## Syntax

```c
void stop();
```

## Description

Programmed interrupt of the ongoing measurement.

If the function is called in an event procedure, the event procedure will always be executed completely before the measurement is stopped.

In offline mode this function interrupts but does not end the measurement. In offline mode the measurement can only be ended with <ESC>.

## Return Values

—

## Example

Output in CANoe Write Window:

...CAPL / .NET oneCAPL / .NET twoCAPL / .NET threeSystem End of measurement 08:57:30.203 am

```c
on key 'a'
{ write ("one"); write ("two"); stop(); write ("three"); }
```

## Availability

| Since Version |
|---|
