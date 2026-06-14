# DoIP_InitAsTester

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_InitAsTester();
```

## Description

Per default the DoIP.DLL will operate as ECU simulation. In order to use this DLL as tester, e.g. in a test module, the operation mode has to be changed by calling this function in on preStart. It is NOT necessary to call this function when the built-in diagnostics channel is used, i.e. if the DoIP.DLL is not configured in the tester.

## Return Values

—

## Example

```c
on preStart
{
  // Make sure the DoIP.DLL does not act as vehicle
  DoIP_InitAsTester();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
