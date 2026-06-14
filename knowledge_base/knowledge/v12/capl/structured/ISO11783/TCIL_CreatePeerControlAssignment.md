# TCIL_CreatePeerControlAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_CreatePeerControlAssignment(dword ddi, dbNode user, dword elementNumberUser, dbNode source, dword elementNumberSource) // form 1
```

## Description

The function creates an assignment of a settable process data object (setpoint value user) to a setpoint value source.

On each change of task status from inactive to active, the TC IL initiates assignment messages to both the setpoint value user and the setpoint value source.

The function fails if the Device Process Data (DPD) object of the setpoint value user does not have the property Settable or if the DPD object of the setpoint value user does not have the property Setpoint Source.

## Return Values

0: Function has been executed successfully

## Example

```c
// Trigger the simulated node ‘TC’ to arrange
// the Device Process Data object with ddi=6 and elementNumber=2 belongs to the  Bailer
// to receive the Value commands
// from the Device Process Data object with ddi=6 and elementNumber=8 belongs to the Sensor
result = TCIL_CreatePeerControlAssignment(TC, 6, Bailer, 2, Sensor, 8);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2204: TestStepFail("Either node 'Sensor' or node 'Bailer' is no client device!"); break;
  case -2207: TestStepFail("A process variables is not available"); break;
  case -2212: TestStepFail("The setpoint value user data variable is not settable"); break;
  case -2213: TestStepFail("The setpoint value source variable doesn’t have the ‘control source’ property"); break;
  default : TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
