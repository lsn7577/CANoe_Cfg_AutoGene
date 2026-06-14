# J1939TestChkCreate_SignalRangeViolation

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_SignalRangeViolation( dword sourceAddr, dword destAddr, dbMessage msg, dbSignal signal, float minSignalValue, float maxSignalValue, char callback[] )
```

## Description

Checks the value of a signal. The given interval (inclusive the limits) should be never left. An event will be generated, if the physical signal value lies outside the given value interval.

## Example

```c
long signalCheck;
signalCheck = J1939TestChkCreate_SignalRangeViolation( 1, 2, EngineData, EngineData::Speed, 0.0, 2000.0,"SignalCallback" );
J1939TestChkControl_Start(signalCheck);
```

## Availability

| Since Version |
|---|
