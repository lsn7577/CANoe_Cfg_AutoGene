# J1939ECUGoOffline

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939ECUGoOffline( dword ecuHandle );
```

## Description

The function switches the state of the node to offline. It does not send a cannot claim address parameter group.

After calling this function the node cannot send any parameter groups, but it is responding to requests for address claim.

Use the function J1939ECUGoOnline to start the node again.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |

## Return Values

0 on success or error code

## Example

```c
J1939ECUGoOffline(ecuHdl);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
