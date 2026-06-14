# TestWaitForSignalsAvailable

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalsAvailable (dbNode aNode, dword aTimeout);
```

## Description

Tests the availability of all the send signals of a node and waits if necessary until all the send signals of the node are available. Signals that are received at least once from the bus after the measurement starts are classified as "available".

This function is useful when you want to assure that all signals are available before starting a signal-oriented test, i.e. to synchronize the tester with the bus.

## Return Values

-2: Wait state is exited due to a constraint/condition violation

## Example

```c
// waits for the availability of all tx signals of node ‘SUT’
long result;
result = TestWaitForSignalsAvailable(SUT, 2000);
```

## Availability

| Since Version |
|---|
