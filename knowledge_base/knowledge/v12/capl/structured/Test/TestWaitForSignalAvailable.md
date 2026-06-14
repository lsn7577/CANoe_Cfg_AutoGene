# TestWaitForSignalAvailable

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalAvailable (Signal aSignal, dword aTimeout); // form 1
```

## Description

Tests the availability of a specific signal and waits if necessary until its availability. A signal that is received at least once from the bus after the measurement starts is classified as "available".

This function is useful when you want to assure that single signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Wait state is exited due to a constraint/condition violation

## Example

```c
// waits for the occurrence of signal ‚EngineRunning’
long result;
result = TestWaitForSignalAvailable(EngineRunning, 2000);
```

## Availability

| Since Version |
|---|
