# TCIL_RequestVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RequestVersion(dbNode client); // form 1
```

## Description

This function requests the Version message from the client.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_RequestVersion(TC, Sprayer);
switch (result)
{
  case     0: TestStepPass(); break;
  case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
  case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
  case -2210: TestStepFail("Failed to send Request Version message!"); break;
  default:    TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
