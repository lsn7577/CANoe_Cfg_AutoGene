# diagStopTesterPresent

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStopTesterPresent (char ecuQualifier[])
```

## Description

Stops sending autonomous/cyclical Tester Present requests from CANoe to the specified or current ECU.

## Parameters

| Name | Description |
|---|---|
| Note This function will only stop the Tester Present service if in the calling CAPL node no CAPL Callback interface for diagnostics is used. |  |

## Return Values

Error code

## Availability

| Since Version |
|---|
