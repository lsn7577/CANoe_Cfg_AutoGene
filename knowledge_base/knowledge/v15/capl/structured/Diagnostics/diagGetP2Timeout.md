# diagGetP2Timeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetP2Timeout (); // form 1: deprecated. Is equivalent to form 2 with source value 2.
long diagGetP2Timeout ( dword source ); // form 2
long diagGetP2Timeout (char ecuQualifier[], dword bIsTester, dword source ); // form 3
```

## Description

Returns the time P2 in milliseconds, from the given source.

If an ECU qualifier is given, the build-in communications channel for this target is accessed.

P2: Time between sending of the request and the start of the arrival of the first response.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Currently active value, i.e. the value originally set or last set from CAPL |
| 1 | Value stored at the selected interface in the description's document |
| 2 | Value configured in the configuration dialog for the description |
| other | reserved |
| Note Basic diagnostic devices do not have an interface defined in a description, therefore source=1 will return the value set at the configuration (source=2). |  |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| Value | Description |
| 0 | Get value for ECU side |
| 1 | Get value for tester side |
| other | reserved |

## Return Values

Error code or time in ms.

## Example

```c
diagSetTarget( "ECU1");
write( "Current P2 = %d", diagGetP2Timeout(0));
write( "Configured P2 = %d", diagGetP2Timeout(2));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 8.0 SP3: form 1 replaced by form 2 | 5.1 8.0 SP3: form 1 replaced by form 2 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
