# scopeTriggerNow

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeTriggerNow()
```

## Description

Performs Trigger Now action for Scope Window. This action is equivalent to immediate triggering via the GUI.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Return Values

1 (success): Trigger signal has been generated. On trigger completion an internal Scope event will be generated (see above). Failure can be recognized implicitly by not receiving the corresponding Scope event during certain timeout, e.g. during one second.

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
if (testWaitForScopeEvent(eScopeTriggered, 50000) != 1)
{
   testStepFail("Initialization ","Scope event eScopeTriggered was not received");
   return;
}
testStep("Initialization","Scope hardware triggered successfully");
```

## Availability

| Since Version |
|---|
