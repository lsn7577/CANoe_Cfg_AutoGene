# TestWaitForValueInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForValueInput (char aQuery []); // form 1
```

## Description

It creates a dialog which displays the transferred string. The tester can enter a number in this dialog. The number can be entered in decimal as well as hexadecimal form. Only characters allowed for numeric values are allowed. Upon closing the dialog, an additional check of the number entered is performed. If the entry cannot be converted to a valid number, an error message is generated and the dialog is exited. The entry can be queried after a successful call with the commands TestGetValueInput (number value) and TestGetStringInput (entry as String). It is also possible to enter a comment in the dialog which is automatically adopted into the test report.

The first wait function without timeout waits until the confirmation by the tester. If the second wait function is used with the timeout, the dialog is automatically closed after the timeout. Whether the dialog was closed due to a timeout or by the tester, can be determined by using the return value.

The function TestGetLastWaitResult can be queried after calling the return value of the function if no other TestWaitForValueInput call occurred in the interim.

Only one dialog is open at a time, even though TestWaitForValueInput is called by different test modules.

You can optionally define some default input for the dialog.

## Return Values

<0: General error, e.g. by calling outside of a test sequence

## Example

Example 1

Example 2

```c
// ask for the test ID and report it in the Write Window
TestWaitForValueInput("Please enter the test ID", 5000);
Write("Test ID = %f", TestGetValueInput());
handle = TestWaitForValueInput(1252, "Test Text", "Test Caption", "Test Value Input", 0);
write("Result: %f", TestGetValueInput());

handle = TestWaitForValueInput(1252, "Test Text", "Test Caption", "Test Value Input Timeout", 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| Since Version |
|---|
