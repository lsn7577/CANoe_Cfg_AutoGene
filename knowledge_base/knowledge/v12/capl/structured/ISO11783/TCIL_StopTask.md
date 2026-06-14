# TCIL_StopTask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_StopTask( ); // form 1
```

## Description

This function stops a task.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_StopTask(TC);
switch (result)
{
  case     0: TestStepPass(); break;
  case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
  case -2208: TestStepFail("Cannot stop task in the current state of the TC IL!"); break;
  default:    TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
