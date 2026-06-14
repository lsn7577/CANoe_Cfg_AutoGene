# scopeDisconnect

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeDisconnect ()
```

## Description

Performs Disconnect Scope action for Scope Window. This action is equivalent to disconnecting Scope via the GUI.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Return Values

2 (success): Scope is already disconnected. This might be a case when the disconnection has been done by a previous CAPL call or manually.

## Example

```c
long res;

res = scopeDisconnect();
if (res <= 0 || res > 2)
{
   testStepFail("Initialization","Call to scopeDisconnect() failed. Return code =%d", res);
   return;
}
else if (res == 1)
{ // wait till action done
   if (testWaitForScopeEvent(eScopeDisconnected, 8000) != 1)
   {
      testStepFail("Initialization ","Scope event eScopeDisconnected was not received");
      return;
   }
}
testStep("Initialization","USB connection with the scope hardware is interrupted");
```

## Availability

| Since Version |
|---|
