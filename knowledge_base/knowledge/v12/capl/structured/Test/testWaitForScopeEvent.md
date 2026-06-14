# testWaitForScopeEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForScopeEvent(dword aTimeout);
```

## Description

Waits for the occurrence of CANoe Scope event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

1: Resume due to event occurred

## Example

```c
long res;

res = scopeTriggerNow();
if (res != 1)
{
   testStepFail("Initialization","Call to scopeTriggerNow() failed. Return code =%d", res);
   return;
}

// wait till action done
if (testWaitForScopeEvent(eScopeTriggered, 8000) != 1)
{
   testStepFail("Initialization ","Scope event eScopeTriggered was not received");
   return;
}
testStep("Initialization","Scope hardware triggered successefully");
```

## Availability

| Since Version |
|---|
