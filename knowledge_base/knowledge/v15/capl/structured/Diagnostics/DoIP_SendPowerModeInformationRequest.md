# DoIP_SendPowerModeInformationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SendPowerModeInformationRequest();
void DoIP_SendPowerModeInformationRequest(char IPaddress[]);
```

## Description

Sends power mode information request as limited broadcast or to the given address.

## Parameters

| Name | Description |
|---|---|
| IPaddress | Address to send to, i.e. not a limited broadcast. May be a directed broadcast address. |

## Return Values

—

## Example

```c
void _DoIP_PowerModeInformationResponse( char IPaddress[], BYTE value)
{
  write( "DoIP_PowerModeInformationResponse from '%s': %d", IPaddress, value);
  testSupplyTextEvent( cTE_PowerModeRespInd);
}
// Send a power mode information request and wait for the first response
Testcase TC_PowerMode()
{
  DoIP_SendPowerModeInformationRequest();
  testWaitForTextEvent( cTE_PowerModeRespInd, 500);
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
