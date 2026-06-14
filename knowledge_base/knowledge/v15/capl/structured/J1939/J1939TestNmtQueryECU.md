# J1939TestNmtQueryECU

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestNmtQueryECU( dword address );
long J1939TestNmtQueryECU( char deviceName[8] );
long J1939TestNmtQueryECU( char deviceName[8], dword componentMask );
```

## Description

The function queries for an ECU handle.

## Parameters

| Name | Description |
|---|---|
| address | address of the ECU |
| deviceName | device name of the ECU is copied to this buffer |
| componentMask | Bit field with the valid components of the Device Name: 0x001: Arbitrary Address Capable 0x002: Industry Group 0x004: Vehicle System Instance 0x008: Vehicle System 0x010: Function 0x020: Function Instance 0x040: ECU Instance 0x080: Manufacturer Code 0x100: Identity Number |

## Return Values

—

## Example

```c
LONG ecuHandle;

J1939TestNmtRefresh( 250 );
ecuHandle = J1939TestNmtQueryECU( 1 );

if (ecuHandle > 0) {
  address = J1939TestNmtQueryAddress( ecuHandle );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
