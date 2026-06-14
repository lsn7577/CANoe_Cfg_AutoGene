# TestValidateTesterConfirmation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestValidateTesterConfirmation(char question[], char heading[], long passedButton); // form 1
```

## Description

Creates a popup window that presents the given string to the tester. The tester can acknowledge the window with Yes, No or Unclear (form (3)).

The window contains a field for entering a comment that is automatically adopted into the test report.

The result of the command is reported.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

## Return Values

0: Timeout occurred.

## Availability

| Since Version |
|---|
