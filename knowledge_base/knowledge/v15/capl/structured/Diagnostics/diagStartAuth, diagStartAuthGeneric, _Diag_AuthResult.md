# diagStartAuth, diagStartAuthGeneric, _Diag_AuthResult

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartAuth(char ecuQualifier[], char jobQualifier[]); // form 1
long diagStartAuthGeneric(char ecuQualifier[], char genericString[]); // form 2
void _Diag_AuthResult(long result); // form 3
```

## Description

Starts the diagnostics authentication process. The result is indicated to the callback function _Diag_AuthResult.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| genericString | Generic parameters to select and configure the security source runtime implementation. |
| jobQualifier | Diagnostic job to be executed. Should be defined in the diagnostic description. |
| result | Result of the authentication process - see error code. |

## Return Values

0 on success otherwise error code

## Example

```c
on key 'a'
{
  result = diagStartAuth("Ecu", "Developer");
  write("Start 'diagStartAuth' for %s with result = %ld", gEcu, result);
}

void _Diag_AuthResult(long result)
{
  write("On '_Diag_AuthResult' for %s with result = %d", gEcu, result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP2 | 11.0 SP2 | — | — | — | 3.0 SP2 |
| Restricted To | Online mode | Online mode Simulation Nodes | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
