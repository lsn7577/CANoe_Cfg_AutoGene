# TCIL_ResetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ResetResponseContent(dbNode client, dword command, dword subcommand); // form 1
long TCIL_ResetResponseContent(dword addressClient, dword command, dword subcommand); // form 2
long TCIL_ResetResponseContent(dbNode tc, dbNode client, dword command, dword subcommand); // form 3
long TCIL_ResetResponseContent(dbNode tc, dword addressClient, dword command, dword subcommand); // form 4
```

## Description

The function resets the modification of TCIL_SetResponseContent. The TC IL returns to the default response behavior.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function. |
| client | Task Controller client which is the originator of the command and receiver of the response message. |
| addressClient | Address of the Task Controller client which is the originator of the command and receiver of the response message. |
| command | Refers to the response with this command value, 0..15. |
| subcommand | Refers to the response with this subcommand value (is only used if command is 0 or 1), 0..15. |

## Example

Example form 3

```c
long result;
result = TCIL_ResetResponseContent(TC, Sprayer, 168);
if (result < 0)
{
  TestStepFail("Failed to reset fault injection");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1: form 2 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
