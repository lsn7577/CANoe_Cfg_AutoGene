# TestAddTriggerTesterAction

> Category: `Test` | Type: `function`

## Syntax

```c
long TestAddTriggerTesterAction(long handle, Signal callbackTrigger);
long TestAddTriggerTesterAction(long handle, sysVar callbackTrigger);
long TestAddTriggerTesterAction(long handle, EnvVarName callbackTrigger);
long TestAddTriggerTesterAction(long handle, long callbackCycle);
```

## Description

Adds a trigger to a tester action previously created with TestCreateTesterAction. Every trigger triggers the call of the CAPL callback of its tester action cyclically or when the value of the signal, system variable, environment variable updates.

## Parameters

| Name | Description |
|---|---|
| handle | The handle of the tester action to add the trigger. |
| callbackTrigger | The trigger when the condition has to be checked. It will always be checked when the value of the signal, system variable or environment variable updates. |
| callbackCycle | Cycle time to check the condition. |

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
