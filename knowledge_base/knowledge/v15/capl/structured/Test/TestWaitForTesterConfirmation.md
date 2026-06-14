# TestWaitForTesterConfirmation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForTesterConfirmation(char text[]);
long TestWaitForTesterConfirmation(char[] text, unsigned long timeout);
long TestWaitForTesterConfirmation(char[] text, unsigned long timeout, char[] heading, char[] resource, char[] resourceCaption);
```

## Description

Creates a popup window that presents the given string to the tester. The tester can acknowledge the window with Yes or No.

The window contains a field for entering a comment that is automatically adopted into the test report.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

Even when this function is called by different test modules maximum only one of these popup windows is active.

The 1st wait function has no timeout so it waits for the confirmation of the tester.The 2nd wait function has a timeout, i.e. the dialog is automatically terminated after the timeout expires.The 3rd wait function has a timeout and can show a resource, i.e. the dialog can show additional information.

## Parameters

| Name | Description |
|---|---|
| text | This is shown in the popup window. The maximum length of the string is limited (4096 characters). |
| timeout | Time in milliseconds after which the dialog is automatically ended. |
| heading | A heading above the dialog text. The maximum length of the string is limited (256 characters). |
| resource | A URL or file path. The maximum length of the string is limited (512 characters).Pictures are shown in the dialog itself, for other resources a link is shown. Supported picture types are: bmp, jpg, png, gif. For arbitrary files, the application registered for that file type on the computer is used to open it when the user clicks the link. Relative file paths are based on the configuration or test setup which contains the test module. |
| resourceCaption | A caption respectively a description for the resource. The maximum length of the string is limited (256 characters). |

## Example

```c
// waits for the answer of the user
long result;
result = TestWaitForTesterConfirmation("Any text or question", 10000);
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
