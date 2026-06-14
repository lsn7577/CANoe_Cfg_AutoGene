# DoIP_SetNextDiagnosticMessageNACKCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetNextDiagnosticMessageNACKCode(long NACKCode);
```

## Description

Sets the next return code sent in the acknowledgment for a diagnostic message received. The code is reset to 0 (positive) after usage.

## Parameters

| Name | Description |
|---|---|
| NACKCode | ISO 13400 defines these values (amongst others): 0: Positive (default)2: Invalid source address3: Unknown target address |

## Return Values

—

## Example

```c
on key 'n' {
  write( “The next diagnostics message will get a negative ack”);
  DoIP_SetNextDiagnosticMessageNACKCode(3);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
