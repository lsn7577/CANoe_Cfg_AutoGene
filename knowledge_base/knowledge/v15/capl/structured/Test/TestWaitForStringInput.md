# TestWaitForStringInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForStringInput (char aQuery[]); // form 1
long TestWaitForStringInput (char aQuery[], dword aTimeout); // form 2
long TestWaitForStringInput(char text[], char caption[], char info[], char[] default[]); // form 3
long TestWaitForStringInput(char text[], char caption[], char info[] char default[], dword timeout); // form 4
long TestWaitForStringInput(char text[], char caption[], char info[], char default[], char regEx[]); // form 5
long TestWaitForStringInput(char text[], char caption[], char info[], char default[], char regEx[], dword timeout); // form 6
```

## Description

It creates a dialog which displays the transferred string. The tester can enter a text in this dialog. This entry can be queried with the command TestGetStringInput after a successful call, i.e. with the return value "1". It is also possible to enter a comment in the dialog which is automatically adopted into the test report.

The first wait function without timeout waits until the confirmation by the tester. If the second wait function is used with the timeout, the dialog is automatically closed after the timeout. Whether the dialog was closed due to a timeout or by the tester, can be determined by using the return value.

The function TestGetLastWaitResult can be queried after calling the return value of the function if no other TestWaitForStringInput call occurred in the interim.

Only one dialog is open at a time, even though TestWaitForStringInput is called by different test modules.You can optionally define some default input for the dialog or a regular expression for checking the input.

## Parameters

| Name | Description |
|---|---|
| aQuery | Text to be displayed in the entry dialog. Up to 255 characters can be displayed in the dialog. |
| aTimeOut | Time in milliseconds after which the dialog is to be cancelled automatically. |
| Text | Text to be displayed in the entry dialog. |
| Caption | The title of the dialog. |
| Info | Further information to be shown. |
| Default | The default value for the input. |
| regEx | Optional regular expression for the input. |
| Timeout | Optional timeout for the dialog in ms. |

## Example

Example 1

Example 2

```c
// ask for the users name and report it in the Write Window
char answer[100];
if (1== TestWaitForStringInput("Please enter your name", 5000))
{
   TestGetStringInput(answer, 100);
   Write("name = %s", answer);
}

handle = TestWaitForStringInput("Test Text", "Test Caption", "TestString Input", "");
TestGetStringInput(resultStr, elcount(resultStr));

return = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input Timeout", "", "", 5000);
TestGetStringInput(resultStr, elcount(resultStr));

return = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input RegEx", "^(\\d)", "", 0);
TestGetStringInput(resultStr, elcount(resultStr));

return = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input RegEx Timeout", "^(\\d)", "", 5000);
TestGetStringInput(resultStr, elcount(resultStr));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0: from 1-2: form 1 11.0: form 3-6 | 13.0 | — | 14 | 1.0: form 1-2 3.0: form 3-6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
