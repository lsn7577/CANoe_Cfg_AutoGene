# TestGetStringInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetStringInput (char aAnswer[], dword aAnswerLen);
```

## Description

Returns the result of the last successful call of TestWaitForStringInput.

## Return Values

<0: General error, e.g. by calling outside of a test sequence or through no previously performed call of TestWaitForStringInput.

## Example

```c
// ask for the users name and report it in the Write Window
char answer[100];
if (1== TestWaitForStringInput("Please enter your name", 5000))
{
 TestGetStringInput(answer, 100);
   Write("name = %s", answer);
}
```

## Availability

| Since Version |
|---|
