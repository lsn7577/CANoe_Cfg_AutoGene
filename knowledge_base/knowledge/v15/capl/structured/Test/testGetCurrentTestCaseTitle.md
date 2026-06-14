# testGetCurrentTestCaseTitle

> Category: `Test` | Type: `function`

## Syntax

```c
testGetCurrentTestCaseTitle(char testCaseTitle[], long bufferSize);
```

## Description

Returns the name of the current test case. After your call of this function the name will be inside the character array testCaseTitle. The maximum length of the name is the length of the character array. This length will be saved in bufferSize.

## Parameters

| Name | Description |
|---|---|
| testCaseTitle | This character array contains the answer after calling the function. |
| bufferSize | This parameter saves the length of the character array. |

## Example

```c
testcase TCExample()
{
  char title[100];

  testCaseComment("Test Case:");
  testGetCurrentTestCaseTitle(title, elcount(title));
  testCasecomment(title);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
