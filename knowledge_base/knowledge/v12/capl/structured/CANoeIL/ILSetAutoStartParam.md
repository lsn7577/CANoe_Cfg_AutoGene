# ILSetAutoStartParam

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILSetAutoStartParam(dword autoStartParam)
```

## Description

Defines the behavior of the interaction layer at measurement start.

If used at all, the function must be called within the on preStart event handler of a CAPL program.

## Parameters

| Name | Description |
|---|---|
| Note The default behavior (i.e. when ILSetAutoStartParam is omitted) is analogous to ILSetAutoStartParam(2). |  |

## Return Values

0: No error

## Availability

| Since Version |
|---|
