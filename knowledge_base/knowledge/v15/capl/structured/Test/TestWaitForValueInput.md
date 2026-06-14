# TestWaitForValueInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForValueInput (char aQuery []); // form 1
long TestWaitForValueInput (char aQuery [], dword aTimeout); // form 2
long TestWaitForValueInput(char text[], char caption[], char info[]); // form 3
long TestWaitForValueInput(char text[], char caption[], char info[], dword timeout); // form 4
```

## Description

It creates a dialog which displays the transferred string. The tester can enter a number in this dialog. The number can be entered in decimal as well as hexadecimal form. Only characters allowed for numeric values are allowed. Upon closing the dialog, an additional check of the number entered is performed. If the entry cannot be converted to a valid number, an error message is generated and the dialog is exited. The entry can be queried after a successful call with the commands TestGetValueInput (number value) and TestGetStringInput (entry as String). It is also possible to enter a comment in the dialog which is automatically adopted into the test report.

The first wait function without timeout waits until the confirmation by the tester. If the second wait function is used with the timeout, the dialog is automatically closed after the timeout. Whether the dialog was closed due to a timeout or by the tester, can be determined by using the return value.

The function TestGetLastWaitResult can be queried after calling the return value of the function if no other TestWaitForValueInput call occurred in the interim.

Only one dialog is open at a time, even though TestWaitForValueInput is called by different test modules.

You can optionally define some default input for the dialog.

## Parameters

| Name | Description |
|---|---|
| aQuery | Text to be displayed in the entry dialog |
| aTimeOut | Time in milliseconds after which the dialog is to be cancelled. |
| Text | Text to be displayed in the entry dialog. |
| Caption | The title of the dialog. |
| Info | Further information to be shown. |
| Timeout | Optional timeout for the dialog in ms. |

## Example

Example 1

Example 2

```c
// ask for the test ID and report it in the Write Window
TestWaitForValueInput("Please enter the test ID", 5000);
Write("Test ID = %f", TestGetValueInput());
return = TestWaitForValueInput("Test Text", "Test Caption", "Test Value Input", 0);
write("Result: %f", TestGetValueInput());

return = TestWaitForValueInput("Test Text", "Test Caption", "Test Value Input Timeout", 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0: form 1-2 11.0: form 3-4 | 13.0 | — | 14 | 1.0: form 1-2 3.0: form 3-4 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
