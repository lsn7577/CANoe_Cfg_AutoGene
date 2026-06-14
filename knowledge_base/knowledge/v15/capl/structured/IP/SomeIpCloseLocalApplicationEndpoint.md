# SomeIpCloseLocalApplicationEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
LONG SomeIpCloseLocalApplicationEndpoint( dword aepHandle );
```

## Description

Closes an Application Endpoint that was previously opened with SomeIpOpenLocalApplicationEndpoint.

Services and the objects assigned to the services (Eventgroups, Events, Fields, and Methods) are removed when the Application Endpoint is closed. If the Application Endpoint has to be reopened, all objects must be created again.

## Parameters

| Name | Description |
|---|---|
| aepHandle | Handle of the Application Endpoint that should be closed (see SomeIpOpenLocalApplicationEndpoint) |

## Example

```c
on key 't'
{
  DWORD aep; // Application Endpoint handle

  // open an Application Endpoint
  aep = SomeIpOpenLocalApplicationEndpoint(17, 50002);

  // ... do something here

  // close the Application Endpoint
  SomeIpCloseLocalApplicationEndpoint(aep);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
