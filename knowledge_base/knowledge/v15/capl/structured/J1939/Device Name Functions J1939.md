# Device Name Functions J1939

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestMakeName( char deviceName[8], long aac, long ig, long vsi, long vs, long fct, long fcti, long ecui, long mc, long in );
long J1939TestGetAAC( char deviceName[8] )long J1939TestSetAAC( char deviceName[8], long aac )
long J1939TestGetIG( char deviceName[8] )long J1939TestSetIG( char deviceName[8], long ig )
long J1939TestGetVSInstance( char deviceName[8] )long J1939TestSetVSInstance( char deviceName[8], long vsi )
long J1939TestGetVS( char deviceName[8] )long J1939TestSetVS( char deviceName[8], long vs )
long J1939TestGetFct( char deviceName[8] )long J1939TestSetFct( char deviceName[8], long fct )
long J1939TestGetFctInstance( char deviceName[8] )long J1939TestSetFctInstance( char deviceName[8], long fcti )
long J1939TestGetECUInstance( char deviceName[8] )long J1939TestSetECUInstance( char deviceName[8], long ecui )
long J1939TestGetMC( char deviceName[8] )long J1939TestSetMC( char deviceName[8], long mc )
long J1939TestGetIN( char deviceName[8] )long J1939TestSetIN( char deviceName[8], long in )
```

## Description

The function can be implemented in your CAPL program. The J1939 Test Service Library calls this function if the NMT table changes. The CAPL program can react on this changes.

## Parameters

| Name | Description |
|---|---|
| deviceName | byte array with 8 byte (64 Bit) |
| aac | Arbitrary Address Capable, 0..1 |
| ig | Industry Group, 0..7 |
| vsi | Vehicle System Instance, 0..15 |
| vs | Vehicle System, 0..127 |
| fct | Function, 0..255 |
| fcti | Function Instance, 0..31 |
| ecui | ECU Instance, 0..7 |
| mc | Manufacturer Code, 0..2047 |
| in | Identity Number, 0.. 209715 |

## Example

```c
CHAR deviceName[8]

J1939TestMakeName( deviceName, 0,0,0,1,2,0,0,2047,1001 )
if (J1939TestGetFct( deviceName ) == 2) {
  write( "Function = 2" );
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
