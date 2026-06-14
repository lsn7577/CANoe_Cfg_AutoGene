# scopeConnect

> Category: `Scope` | Type: `function`

## Syntax

```c
long scopeConnect()
```

## Description

Performs Connect Scope action for Scope Window. This action is equivalent to connecting Scope via the GUI. The Scope Window will be opened automatically if not yet opened.

The completion of this action is reported with an internal event which can be awaited via TFS-function testWaitForScopeEvent() in CAPL programs for test modules.

## Return Values

2 (success): Connection is already established. This might be a case when connection has been established by a previous CAPL call or manually.

## Example

```c
long res;

res = scopeConnect();
if (res < 0 || res > 2)
{
   testStepFail("Initialization"," Call to scopeConnect() failed. Return code =%d", res);
   return;
}
else if (res == 1)
{ // wait till action done
   if (testWaitForScopeEvent(eScopeConnected, 8000) != 1)
   {
      testStepFail("Initialization ","Scope event eScopeConnected was not received");
      return;
   }
}
testStep("Initialization","USB connection with the scope hardware is established");
```

## Availability

| Since Version |
|---|
