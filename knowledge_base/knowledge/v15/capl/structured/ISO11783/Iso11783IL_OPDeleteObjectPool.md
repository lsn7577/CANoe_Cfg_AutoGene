# Iso11783IL_OPDeleteObjectPool

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPDeleteObjectPool(); // form 1
long Iso11783IL_OPDeleteObjectPool(dbNode implement); // form 2
```

## Description

The function sends the Delete Object Pool message to the connected Virtual Terminal.

The simulated node neither clears the loaded Object Pool nor stops to send the Working Set Maintenance message to the Virtual Terminal.

For simultaneous clearing of the loaded Object Pool and stopping the Working Set Maintenance message, call the Iso11783IL_OPDeactivate() instead.

## Parameters

| Name | Description |
|---|---|
| implement | Simulation node to apply the function. |

## Example

Example Form 2

```c
long result;
result = Iso11783IL_OPDeleteObjectPool(Sprayer);
if (result < 0)
{
  TestStepFail("Failed to send the Delete Object Pool mesage");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
