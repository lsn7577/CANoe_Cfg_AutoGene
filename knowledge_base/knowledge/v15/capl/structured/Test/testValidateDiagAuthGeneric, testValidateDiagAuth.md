# testValidateDiagAuthGeneric, testValidateDiagAuth

> Category: `Test` | Type: `function`

## Syntax

```c
long testValidateDiagAuthGeneric( const char ecuQualifier, const char genericString); // form 1
long testValidateDiagAuth( const char ecuQualifier, const char jobQualifier); // form 2
```

## Description

Initiates the diagnostics authentication process and waits until this process has (generic) completed. The test step is then evaluated as passed or failed, depending on the result, and documented in the report.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| genericString | Generic parameters to select and configure the security source runtime implementation. |
| jobQualifier | Diagnostic job to be executed. Should be defined in the diagnostic description. |

## Return Values

On success 0, otherwise error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
