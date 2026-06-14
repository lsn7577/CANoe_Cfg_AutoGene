# TestCaseFail

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseFail ();
```

## Description

You can set the verdict of the current test case to fail. This function can only be used within a test case. It is not possible to set the verdict of this test case back to pass.

## Return Values

—

## Example

```c
// checks if the value of the signal is in the given range
testcase CheckSignalValue()
{
   long result;
   result = checkSignalInRange(Node_SUT::Velocity, 60, 100);
   if (result != 1)
   TestCaseFail();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
