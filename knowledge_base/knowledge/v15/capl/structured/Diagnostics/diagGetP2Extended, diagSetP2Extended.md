# diagGetP2Extended, diagSetP2Extended

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetP2Extended (); // form 1: deprecated. Is equivalent to form 2 with source value 2.
long diagGetP2Extended (dword source); // form 2
long diagSetP2Extended (long timeout); // form 3
long DiagGetP2Extended(char ecuQualifier[], long isTester, dword source); // form 4
```

## Description

Returns the P2 extended timeout from the selected source, or sets it to the specified value.

## Parameters

| Name | Description |
|---|---|
| -1 | Deactivates "Response Pending" handling. |
| 0 | Resets P2ex to its preset value. |
| >0 | Sets P2ex to the value (in ms). |
| Note If "Response Pending" handling is deactivated, CANoe forwards these responses to CAPL as negative responses. Otherwise the P2ex timer is automatically started and the final response or a timeout is reported. |  |
| Value | Description |
| 0 | Currently active value, i.e. the value originally set or last set from CAPL. |
| 1 | Value stored at the selected interface in the description's document. |
| 2 | Value configured in the configuration dialog for the description. |
| other | reserved |
| Note Basic diagnostic devices do not have an interface defined in a description, therefore source=1 will return the value set at the configuration (source=2). |  |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| Value | Description |
| 0 | The node asking for the communication parameter is an ECU simulation. |
| 1 | The node asking for the communication parameter is a tester. |
| other | reserved |

## Return Values

Error code or time in ms for DiagGetP2Extended.

## Example

```c
diagSetTarget( "ECU1");
write( "Current P2 = %d", diagGetP2Extended(0));
write( "Original value at interface = %d", diagGetP2Extended(1));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 8.0 SP3: form 1 replaced by form 2 9.0 SP3: from 4 | 5.1 8.0 SP3: form 1 replaced by form 2 9.0 SP3: form 4 | — | — | — | 1.0: form 2, 3 2.1 SP3: form 4 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
