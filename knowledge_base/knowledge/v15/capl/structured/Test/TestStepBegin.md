# TestStepBegin

> Category: `Test` | Type: `function`

## Syntax

```c
TestStepBegin (dword Importance, char Identifier[], char Description[]);
TestStepBegin (char Identifier[], char Description[]);
```

## Description

With these functions, test steps can be logged within a test case. Such a test step is introduced with TestStepBegin, which is then completed with TestStepPass, TestStepFail or TestStepWarning. A test step is noted in the test report only with this conclusion.

## Parameters

| Name | Description |
|---|---|
| Importance | It is possible to identify with a number how important this test step is. In the test report, it is possible that only test steps up to a certain importance will be displayed. 0 means "very important", higher numbers indicate lower degrees of importance. Without an explicit specification, the importance 0 is assumed. |
| Identifier (e.g. a test step number) of the test step |  |
| Description of the test step | A possibly-specified descriptive text in the concluding TestStepPass, TestStepFail or TestStepWarning is added to this descriptive text. To obtain line breaks (in form of <br /> tags) in the test report, "\n" may be inserted at any place. The required replacement takes place during the transformation of the XML test report into an HTML file by means of an XSLT style sheet, where it can also be deactivated (see CANoe Test:Tips & Tricks). |

## Return Values

—

## Example

```c
TestStepBegin (0, „3.1“, „Receipt of response message“);
if (result == 1)
   TestStepPass ();
else
   TestStepFail („failed because of Timeout“);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
