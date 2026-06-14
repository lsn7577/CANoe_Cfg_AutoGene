# SCC_GetChargingProfileData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetChargingProfileData ( long Index, dword& Start, float& MaxPower, long& MaxNumberOfPhases )
```

## Description

Get the content of a charging profile within a ChargeParameterDiscoveryReq message.

## Return Values

Content of the ChargingProfile with the specified index via references.
Start: Start time of charging, in seconds from the time the request is sent.
MaxPower: Maximum line power of charging profile
MaxNumberOfPhases: Maximum number of phases of charging profile

## Availability

| Since Version |
|---|
