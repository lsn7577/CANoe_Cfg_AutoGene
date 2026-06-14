# linStartScheduler

> Category: `LIN` | Type: `function`

## Syntax

```c
void linStartScheduler()
```

## Description

This function starts the internal scheduler, which begins a cyclical traversal of a last configured schedule table.

If this is the first time the scheduler started the first found schedule table, i.e. the schedule table with index 0, is used.

Calling this function before the measurement start is not necessary, since the scheduler is started automatically.

## Return Values

—

## Availability

| Since Version |
|---|
