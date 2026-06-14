# diagStartTesterPresent

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartTesterPresent(char ecuQualifier[])
```

## Description

Starts sending autonomous/cyclical Tester Present requests from CANoe to the specified or current ECU.

## Parameters

| Name | Description |
|---|---|
| Note This function will only start the Tester Present service if in the calling CAPL node no CAPL Callback interface for diagnostics is used. |  |

## Return Values

Error code

## Availability

| Since Version |
|---|
