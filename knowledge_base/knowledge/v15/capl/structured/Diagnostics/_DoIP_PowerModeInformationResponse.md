# _DoIP_PowerModeInformationResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_PowerModeInformationResponse(char IPaddress[], BYTE value);
```

## Description

The tester received a response for a Power Mode Information Request. The vehicle's IP address is given as first argument, in text form.

## Parameters

| Name | Description |
|---|---|
| IPaddress | Address in text form, e.g. “169.254.32.1” (IPv4) or “2001::1” (IPv6). |
| value | Power mode information returned by the vehicle. |

## Return Values

—

## Example

See DoIP_SendPowerModeInformationRequest

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
