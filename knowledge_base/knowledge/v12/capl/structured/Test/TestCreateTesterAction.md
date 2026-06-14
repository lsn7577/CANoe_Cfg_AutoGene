# TestCreateTesterAction

> Category: `Test` | Type: `function`

## Syntax

```c
long TestCreateTesterAction(char[] actionText, char[] heading, char[] callback);
```

## Description

Creates a tester action. The condition is checked every time when the given trigger occurs. The check of the condition must be implemented in the given CAPL callback. The triggers have to be added with the TestAddTriggerTesterAction function.To execute the command call TestValidateTesterAction with the handle of the tester action.

## Return Values

> 0: Handle of the tester action.

## Example

```c
int CallbackTesterAction(long trigger)
{
  if (trigger == gTriggerCycle)
  {
    testStep("", "Triggered by cycle time");
  }
  else if (trigger == gTriggerSig)
  {
    testStep("", "Triggered by signal");
  }
  else if (trigger == gTriggerSV)
  {
    testStep("", "Triggered by system variable");
  }
  else if (trigger == gTriggerEV)
  {
    testStep("", "Triggered by environment variable");
  }
  else
  {
    testStep("", "Triggered before opening dialog or before closing dialog after timeout");
  }
  if(@sysVarEngineStarted == 1)
    return 1;

  return 0;
}

testcase TCTesterAction()
{
  long handle;

  handle = TestCreateTesterAction("This is the tester action text", "Tester action heading", "Resource.jpg", "Resource Caption", "CallbackTesterAction");

  gTriggerCycle = TestAddTriggerTesterAction(handle, 1000);
  gTriggerSig = TestAddTriggerTesterAction(handle, SigSigned16);
  gTriggerSV = TestAddTriggerTesterAction(handle, sysvar::sysInt);
  gTriggerEV = TestAddTriggerTesterAction(handle, EnvInt);

  TestValidateTesterAction(handle, 10000, 3);
}
```

## Availability

| Since Version |
|---|
