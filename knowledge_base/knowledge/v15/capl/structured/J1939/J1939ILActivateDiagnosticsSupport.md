# J1939ILActivateDiagnosticsSupport

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILActivateDiagnosticsSupport(byte enable); // form 1
long J1939ILActivateDiagnosticsSupport(dbNode node, byte enable); // form 2
```

## Description

This function activates or deactivates the support of J1939 diagnostics by the IL.

If diagnostics support is activated the node:

If diagnostics support is activated then diagnostics message which are in the Tx list of the node are disabled and therefor not used by the IL.

## Parameters

| Name | Description |
|---|---|
| enable | Enables or disables support of J1939 diagnostics: 0: Disable support of J1939 diagnostics 1: Enable support of J1939 diagnostics |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
