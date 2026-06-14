# GetNrOfCOProviders

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword GetNrOfCOProviders(communicationObject co);
```

## Description

Returns the current number of provider endpoints at a (service-oriented) communication object. Note the number of endpoints may vary over time for some objects. The function is particularly useful to iterate over all providers.

## Parameters

| Name | Description |
|---|---|
| co | Communication object |

## Return Values

The current number of provider endpoints.

## Example

```c
for (i = 0; i < GetNrOfCOProviders(MirrorAdjustment); ++i)
{
  svc = MirrorAdjustment.consumerSide[CANoe,i];
  // ...
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
