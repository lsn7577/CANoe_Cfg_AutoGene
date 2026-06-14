# TestStepBegin

> Category: `Test` | Type: `function`

## Syntax

```c
TestStepBegin (dword Importance, char Identifier[], char Description[]);
```

## Description

With these functions, test steps can be logged within a test case. Such a test step is introduced with TestStepBegin, which is then completed with TestStepPass, TestStepFail or TestStepWarning. A test step is noted in the test report only with this conclusion.

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

| Since Version |
|---|
