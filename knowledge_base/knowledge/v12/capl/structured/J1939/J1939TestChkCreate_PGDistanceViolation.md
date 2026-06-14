# J1939TestChkCreate_PGDistanceViolation

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_PGDistanceViolation(dword refSource, dword refDest, dword refPgn, dword obsrvSource, dword obsrvDest, dword obsrvPgn, dword aMinDistance, dword aMaxDistance, char callback[] )
```

## Description

An event is generated if the time interval that starts on receipt of the reference message and ends with the receipt of the observed message is smaller than aMinDistance or is larger than aMaxDistance.

## Example

```c
long distCheck ;
distCheck = J1939TestChkCreate_PGDistanceViolation( 1, 2, 0xf100, 2, 1, 0xf101, 80, 120, "PGDistanceCallback" );J1939TestChkControl_Start( distCheck );
```

## Availability

| Since Version |
|---|
