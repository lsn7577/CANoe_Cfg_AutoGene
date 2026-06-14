# TCIL_ValueAndAckCommand, TCIL_ValueAndAckCommandRaw, TCIL_ValueAndAckCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ValueAndAckCommand(dbNode client, dword ddi, dword elementNumber); // form 1
```

## Description

Form (1) and (2) send the current value of the specified data entity to the client with Set Value and Acknowledge command. It can be used to send to the client the previously set Compressed State DDIs DDIs (using TCIL_SetValueRaw or TCIL_SetValuePhysical).

Form (3)-(6) set the value to the specified data entity and send the value to the client with Set Value and Acknowledge command.

Form (3)-(6) set the value to the specified data entity (if exists) and sends the value to the client with Value command.

## Return Values

0: Function has been executed successfully

## Example

```c
void SendSetpointMassPerAreaApplicationRate(double value)
{
  long result;
  result = TCIL_ValueAndAckCommandPhysical(TC, Sprayer, 6, 1, value);
  switch (result)
  {
    case     0: TestStepPass(); break;
    case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
    case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
    case -2210: TestStepFail("Failed to send Value command!"); break;
    default:    TestStepFail("Unexpected error"); break;
  }
}
```

## Availability

| Since Version |
|---|
