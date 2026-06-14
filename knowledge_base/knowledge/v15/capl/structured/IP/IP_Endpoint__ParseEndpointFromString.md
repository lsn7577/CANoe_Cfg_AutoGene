# IP_Endpoint::ParseEndpointFromString

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Endpoint::ParseEndpointFromString(char endpoint[]);
```

## Description

Converts the character string to an endpoint and sets this endpoint to the IP endpoint value.

## Parameters

| Name | Description |
|---|---|
| endpoint | A character string representing an IP endpoint. |

## Example

```c
variables
{
  ip_Endpoint ipEndpoint;
}

on sysvar_update sysvar::Endpoint
{
  char endpointText[60];
  sysGetVariableString(this, endpointText, elcount(endpointText));
  ipEndpoint.ParseEndpointFromString(endpointText);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
