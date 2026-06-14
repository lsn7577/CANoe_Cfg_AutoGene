# TCIL_StartTask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_StartTask( ); // form 1
```

## Description

This function starts a task.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_StartTask(TC);
switch (result)
{
  case     0: TestStepPass(); break;
  case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
  case -2207: TestStepFail("Cannot start task in the current state of the TC IL!"); break;
  default:    TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
