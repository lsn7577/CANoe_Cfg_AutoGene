# TestSetEcuOnline

> Category: `Test` | Type: `function`

## Syntax

```c
void testSetEcuOnline (dbNode aNode);
```

## Description

Connects the ECU to the bus.After calling the testSetEcuOffline() function the ECU can be reconnected to the bus by using the testSetEcuOnline() function. Messages being sent by the ECU will be forwarded to the bus.

This function interferes with the CAPL program and possible Nodelayer DLLs.

## Return Values

—

## Example

```c
// cuts the node ‚SUT’ 5000 ms from the bus
TestSetEcuOffline(SUT);
TestWaitForTimeout(5000);
TestSetEcuOnline(SUT)
```

## Availability

| Since Version |
|---|
