# Iso11783TableTime

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783TableTime( char busName[] );
```

## Description

The function returns the time stamp of the last received "Request for Address Claim". Use this function to determine, if the network table is up to data.

## Parameters

| Name | Description |
|---|---|
| busName | Bus name or "default" |

## Return Values

Time stamp of the last received Request for Address Claim in 10µs

## Example

```c
dword time;
time = Iso11783TableTime( "default" 
 );

if (time + 25000 < timeNow()) 
 {
write( "Last Request for ACL is older than 250ms" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
