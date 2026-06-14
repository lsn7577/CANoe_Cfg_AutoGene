# Iso11783IL_PDDOnStateChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_PDDOnStateChanged( dword state );
```

## Description

Is called up when the interaction layer changes its state.

## Parameters

| Name | Description |
|---|---|
| state | task state: 0: not initialized 1: initialized 2: start up delay (6 seconds) 3: wait for task controller status 4: query information 5: transfer object pool 6: object pool activation 7: online 8: task active |

## Return Values

—

## Example

```c
void Iso11783IL_PDDOnStateChanged( dword state )
{
  switch(state) {
  case 0: // Uninitialized
    break;
  case 1: // Initialized
    break;
  case 2: // StartUpDelay
    break;
  case 3: // Wait For Task Controller 
 Status
    break;
  case 4: // Query Info
    break;
  case 5: // Transfer Object Pool
    break;
  case 6: // Activate Object Pool
    break;
  case 7: // Online
    break;
  case 8: // Task active
    break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
