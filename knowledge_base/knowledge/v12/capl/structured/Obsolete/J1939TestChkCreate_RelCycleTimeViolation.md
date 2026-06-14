# J1939TestChkCreate_RelCycleTimeViolation

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_RelCycleTimeViolation(dword sourceAddr, dword destAddr, dbMessage dbMsg, double minCycleTime, double maxCycleTime, [char callback[]] )
```

## Description

Cycle time check for a J1939 parameter group. The message attribute GenMsgCycleTime must be defined for the message. The minimum and maximum cycle time is a relative factor to the cycle time from the database.

## Example

```c
long check;
check = J1939TestChkCreate_RelCycleTimeViolation( EMS, EEC1, 0.95, 1.05 );
J1939TestChkControl_Start( check );
```

## Availability

| Up to Version |
|---|
