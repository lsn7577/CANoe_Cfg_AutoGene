# testWaitScopeSetConfiguration

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeSetConfiguration (char deviceName[], char configurationName[]);
```

## Description

Configures the appropriate oscilloscope with the specified configuration.

Hint: The possible device names and configurations names can be requested with the function testWaitScopeGetConfigurationInformation

## Parameters

| Name | Description |
|---|---|
| deviceName | The name of the scope device. |
| configurationNames | The specific configuration should be used for the scope device. |

## Example

```c
void SetScopeConfiguration()
{
  long res;

  res = testWaitScopeSetConfiguration(“Scope_1”, “MyConfiguration”);

  if (res != 1)
  {
    testStepFail("SetConfiguration","Set configuration MyConfiguration of Scope_1 was not possible. Result = %d", res);
  }

  else

  {
    testStepPass("SetConfiguration", "Configuration of Scope_1 is set to MyConfiguration”);
  }

}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | Scope | Scope | — | — | Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
