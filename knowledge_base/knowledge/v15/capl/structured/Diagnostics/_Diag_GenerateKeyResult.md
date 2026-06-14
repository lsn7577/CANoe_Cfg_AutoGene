# _Diag_GenerateKeyResult

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_GenerateKeyResult(long result, BYTE computedKey[]);
```

## Description

Indicates the result of the security key computation which was started with DiagStartGenerateKeyFromSeed.

## Parameters

| Name | Description |
|---|---|
| result | 0: Successother: Error code |
| computedKey | Key as returned by the Seed & Key DLL, if any. |

## Return Values

—

## Example

See: DiagStartGenerateKeyFromSeed

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP2 | 8.2 SP2 | — | — | — | 1.1 SP2 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
