# CANstressOnIdle

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressOnIdle( char fnctCallback[] );
```

## Description

Registers a CAPL function as callback that is called if CANstress is switched into the state Idle.

## Parameters

| Name | Description |
|---|---|
| Note The callback functions must correspond to the following syntax: long FunctionName( dword ); Should the CAPL function used as callback not longer be called when CANstress changes into the Idle condition, an empty string must be passed as parameter to CANstressOnPending. // delete or switch off present callback CANstressOnIdle( " " ); |  |

## Return Values

0: On successful call.

## Availability

| Since Version |
|---|
