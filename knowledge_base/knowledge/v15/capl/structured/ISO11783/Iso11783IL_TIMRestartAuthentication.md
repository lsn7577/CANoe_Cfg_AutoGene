# Iso11783IL_TIMRestartAuthentication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMRestartAuthentication(dbNode server); // form 1
long Iso11783IL_TIMRestartAuthentication(byte serverAddress); // form 2
long Iso11783IL_TIMRestartAuthentication(dbNode client, dbNode server); // form 3
long Iso11783IL_TIMRestartAuthentication(dbNode client, byte serverAddress); // form 4
```

## Description

This function restarts the authentication process of a client/server communication.

The client restarts the authentication by setting the (Re)Start authentication status bit of the Auth_ClientAuthenticationStatusClient message.

This function only succeeds if the authentication process is currently active (especially if current state is Authentication error).

## Parameters

| Name | Description |
|---|---|
| server | The CAPL function restarts authentication for the connection to this server. |
| serverAddress | The CAPL function restarts authentication for the connection to the server with this address. |
| client | TIM client node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0: form 1, 3 11.0 SP2: form 2, 4 | 13.0 | — | — | 3.0: form 3 3.0 SP2: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
