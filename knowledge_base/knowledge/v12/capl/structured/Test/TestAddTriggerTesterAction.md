# TestAddTriggerTesterAction

> Category: `Test` | Type: `function`

## Syntax

```c
long TestAddTriggerTesterAction(long handle, Signal callbackTrigger);
```

## Description

Adds a trigger to a tester action previously created with TestCreateTesterAction. Every trigger triggers the call of the CAPL callback of its tester action cyclically or when the value of the signal, system variable, environment variable updates.

## Return Values

> 0: Handle of the trigger.

## Example

```c
int CallbackTesterAction(int trigger)
{
  if (trigger == gTriggerCycle)
  {
    testStep("", "Triggered by cycle time”);
  }
  else if (trigger == gTriggerSig)
  {
    testStep("", "Triggered by signal”);
  }
  else if (trigger == gTriggerSV)
  {
    testStep("", "Triggered by system variable”);
  }
  else if (trigger == gTriggerEV)
  {
    testStep("", "Triggered by environment variable”);
  }
  else
  {
    testStep("", "Triggered before opening dialog or before closing dialog after timeout”);
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
