# TestSetEcuOffline

> Category: `Test` | Type: `function`

## Syntax

```c
void testSetEcuOffline (dbNode aNode);
```

## Description

Disconnects the ECU from the bus. Messages being sent by the ECU will not be forwarded to the bus.With the testSetEcuOnline function the ECU can be reconnected to the bus.

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
