# scopeActivateTrigger

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeActivateTrigger ()
```

## Description

Performs Activate Trigger action for Scope window. This action is equivalent to activating the trigger via the GUI.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Return Values

2 (success): Trigger is already active. This might be a case when the trigger has been activated by a previous CAPL call or manually.

## Example

```c
long res;

res = scopeActivateTrigger();
if (res <= 0 || res > 2)
{
   testStepFail("Initialization","Call to scopeActivateTrigger() failed. Return code =%d", res);
   return;
}
else if (res == 1)
{ // wait till action done
   if (testWaitForScopeEvent(eScopeTriggerActivated, 8000) != 1)
   {
      testStepFail("Initialization ","Scope event eScopeTriggerActivated was not received");
      return;
   }
}
testStep("Initialization","Scope trigger activation succeeded");
```

## Availability

| Since Version |
|---|
