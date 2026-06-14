# scopeDeactivateTrigger

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeDeactivateTrigger()
```

## Description

Performs Deactivate Trigger action for Scope Window. This action is equivalent to deactivating the trigger via the GUI.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Return Values

2 (success): Trigger is already inactive. This might be a case when the trigger has been deactivated by a previous CAPL call or manually.

## Example

```c
long res;

res = scopeDeactivateTrigger();
if (res <= 0 || res > 2)
{
   testStepFail("Initialization","Call to scopeDeactivateTrigger() failed. Return code =%d", res);
   return;
}
else if (res == 1)
{ // wait till action done
   if (testWaitForScopeEvent(eScopeTriggerDeactivated, 8000) != 1)
   {
      testStepFail("Initialization ","Scope event eScopeTriggerDeactivated was not received");
      return;
   }
}
testStep("Initialization","Scope trigger deactivation succeeded");
```

## Availability

| Since Version |
|---|
