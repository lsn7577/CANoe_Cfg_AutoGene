# Iso11783OPControlAudio

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPControlAudio( dword ecuHandle, dword activations, dword frequency, dword onTime, dword offTime );
```

## Description

The function plays an acoustic signal on the Virtual Terminal. A Control Audio Device command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| activations | Number of tones |
| frequency | Frequency in [Hz] |
| onTime | Duration of the tone in [ms] |
| offTime | Duration of the gaps between the tones |

## Return Values

0 or error code

## Example

```c
Iso11783OPControlAudio( 
 handle, 2, 2000, 100, 50 );
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
