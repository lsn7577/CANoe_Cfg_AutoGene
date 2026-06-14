# Iso11783OPOnKeyActivation

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnKeyActivation( dword ecuHandle, dword objectID, dword parentID, dword keyCode, dword activation );
```

## Description

The function is called by the node layer, if the user presses a soft key or button.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |
| objectID | Object ID of a soft key or button object |
| parentID | Object ID of the mask object |
| keyCode | Code of the soft key or button |
| activation | Activation code 0: Key is release 1: Key is pressed 2: Key is held 3: Press is canceled |

## Return Values

—

## Example

```c
void Iso11783OPOnKeyActivation( dword handle, dword object ID, dword parentID, dword keyCode, 
 dword activation )
{
  if (activation == 1) {
    switch(keyCode) {
    case 1: DoSometing1(); break;
    case 2: DoSometing2(); break;
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
