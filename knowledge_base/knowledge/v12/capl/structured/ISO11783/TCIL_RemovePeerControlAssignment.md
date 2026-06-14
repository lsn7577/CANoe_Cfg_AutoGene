# TCIL_RemovePeerControlAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RemovePeerControlAssignment(dword ddi, dbNode user, dword elementNumberUser,) // form 1
```

## Description

The function separates a setpoint value user from the setpoint value source.

If the task status and the assignment is active the TC IL sends the unassignment messages to both the setpoint value user and the assigned setpoint value source.

## Return Values

0: Function has been executed successfully

## Example

```c
// Trigger the simulated node ‘TC’ to disconnect the assignment of
// the setpoint value user with ddi=6 and elementNumber=2, belongs to the node ‘Bailer’,
// to the previously assigned setpoint value source
result = TCIL_RemovePeerControlAssignment(TC, 6, Bailer, 2);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2204: TestStepFail("Node 'Bailer' is no client device!"); break;
  case -2207: TestStepFail("The process variables is not available"); break;
  default : TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
