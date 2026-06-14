# TCIL_RequestValueCommand

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RequestValueCommand(dbNode client, dword ddi, dword elementNumber); // form 1
```

## Description

This function sends the Request Value command to the client.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = TCIL_RequestValueCommand(TC, Sprayer, 6, 3);
if (result != 0)
{
  TestStepFail("RequestValue", "Failed to request value of data entity (DDI 6 , element number 1). Error %i", result);
}
```

## Availability

| Since Version |
|---|
