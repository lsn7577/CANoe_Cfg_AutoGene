# Device Name Functions J1939

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestMakeName( char deviceName[8], long aac, long ig, long vsi, long vs, long fct, long fcti, long ecui, long mc, long in );
```

## Description

The function can be implemented in your CAPL program. The J1939 Test Service Library calls this function if the NMT table changes. The CAPL program can react on this changes.

## Example

```c
CHAR deviceName[8]

J1939TestMakeName( deviceName, 0,0,0,1,2,0,0,2047,1001 )
if (J1939TestGetFct( deviceName ) == 2) {
  write( "Function = 2" );
}
```

## Availability

| Since Version |
|---|
