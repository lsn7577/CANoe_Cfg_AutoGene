# DoIP_SendPowerModeInformationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SendPowerModeInformationRequest();
```

## Description

Sends power mode information request as limited broadcast or to the given address.

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

| Since Version |
|---|
