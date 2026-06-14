# TestWaitForStringInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForStringInput (char aQuery[]); // form 1
```

## Description

It creates a dialog which displays the transferred string. The tester can enter a text in this dialog. This entry can be queried with the command TestGetStringInput after a successful call, i.e. with the return value "1". It is also possible to enter a comment in the dialog which is automatically adopted into the test report.

The first wait function without timeout waits until the confirmation by the tester. If the second wait function is used with the timeout, the dialog is automatically closed after the timeout. Whether the dialog was closed due to a timeout or by the tester, can be determined by using the return value.

The function TestGetLastWaitResult can be queried after calling the return value of the function if no other TestWaitForStringInput call occurred in the interim.

Only one dialog is open at a time, even though TestWaitForStringInput is called by different test modules.You can optionally define some default input for the dialog or a regular expression for checking the input.

## Return Values

<0: General error, e.g. by calling outside of a test sequence

## Example

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

handle = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input Timeout", "", "", 5000);
TestGetStringInput(resultStr, elcount(resultStr));

handle = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input RegEx", "^(\\d)", "", 0);
TestGetStringInput(resultStr, elcount(resultStr));
h
andle = TestWaitForStringInput("Test Text", "Test Caption", "Test String Input RegEx Timeout", "^(\\d)", "", 5000);
TestGetStringInput(resultStr, elcount(resultStr));
```

## Availability

| Since Version |
|---|
