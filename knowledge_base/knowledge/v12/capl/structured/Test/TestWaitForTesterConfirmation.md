# TestWaitForTesterConfirmation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForTesterConfirmation(char text[]);
```

## Description

Creates a popup window that presents the given string to the tester. The tester can acknowledge the window with Yes or No.

The window contains a field for entering a comment that is automatically adopted into the test report.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

Even when this function is called by different test modules maximum only one of these popup windows is active.

The 1st wait function has no timeout so it waits for the confirmation of the tester.The 2nd wait function has a timeout, i.e. the dialog is automatically terminated after the timeout expires.The 3rd wait function has a timeout and can show a resource, i.e. the dialog can show additional information.

## Return Values

0: Timeout occurred.

## Example

```c
// waits for the answer of the user
long result;
result = TestWaitForTesterConfirmation("Any text or question", 10000);
```

## Availability

| Since Version |
|---|
