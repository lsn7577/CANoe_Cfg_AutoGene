# TestWaitForvFlashInitialized , TestWaitForvFlashDeinitialized

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long TestWaitForvFlashInitialized();
long TestWaitForvFlashDeinitialized();
```

## Description

Waits until the vFlash library is initialized/deinitialized. A call to TestWaitForvFlashDeinitialized is mandatory if any other call to a function of the vFlash API is made.

## Return Values

other: please refer to enum vFlashStatusCode in Reusable\CAPL_Includes\vFlash\Utilities.cin

## Example

```c
  // ...
  // Prepare flashing on FlexRay
  vFlashActivateNetwork();
}
void vFlashActivateNetworkCompleted(long vFlashStatusCode)
{
  write("FlexRay network management was activated");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 + DLL 3.5.100 | — | — | — | 2.2 SP2 + DLL 3.5.100 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
