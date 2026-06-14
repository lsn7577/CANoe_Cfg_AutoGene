# TCIL_RemovePeerControlAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_RemovePeerControlAssignment(dword ddi, dbNode user, dword elementNumberUser,) // form 1
long TCIL_RemovePeerControlAssignment(node tc, dword ddi, dbNode user, dword elementNumberUser) // form 2
```

## Description

The function separates a setpoint value user from the setpoint value source.

If the task status and the assignment is active the TC IL sends the unassignment messages to both the setpoint value user and the assigned setpoint value source.

## Parameters

| Name | Description |
|---|---|
| ddi | This DDI of the setpoint value user that has to be separated from the setpoint value source. |
| user | Peer control capable device which acts as a setpoint value user. |
| elementNumberUser | The elementNumber of the setpoint value user that has to be separated from the setpoint value source. |

## Example

Example form 2

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP4 | 13.0 | — | — | 2.1 SP4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
