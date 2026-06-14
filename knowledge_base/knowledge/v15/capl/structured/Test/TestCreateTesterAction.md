# TestCreateTesterAction

> Category: `Test` | Type: `function`

## Syntax

```c
long TestCreateTesterAction(char[] actionText, char[] heading, char[] callback);
long TestCreateTesterAction(char[] actionText, char[] heading, char[] resourceFile, char[] resourceCaption, char[] callback);
```

## Description

Creates a tester action. The condition is checked every time when the given trigger occurs. The check of the condition must be implemented in the given CAPL callback. The triggers have to be added with the TestAddTriggerTesterAction function.To execute the command call TestValidateTesterAction with the handle of the tester action.

## Parameters

| Name | Description |
|---|---|
| actionText | Tester instruction of the popup window. |
| heading | Heading of the popup window. |
| callback | CAPL callback which is called every time to check the condition when the trigger occurs. The callback is also automatically called once before the popup opens and once before the popup closes after timeout occurs.Callback function must have the following signature: int mycallback(long trigger); The parameter trigger is the handle of the trigger which triggers the callback. The return value describes the result of the condition: 0: condition is not fulfilled. Continue waiting ≠0: condition is fulfilled. Stop waiting and end command |
| resourceFile | The path of the resource image to show on the popup window. |
| resourceCaption | The caption to show below the resource image. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | 14 | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
