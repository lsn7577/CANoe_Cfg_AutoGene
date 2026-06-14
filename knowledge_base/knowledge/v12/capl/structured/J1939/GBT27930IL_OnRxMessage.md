# GBT27930IL_OnRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_OnRxMessage( pg * rxPG )
```

## Description

This callback function is called from the GBT27930 IL if the GBT27930 IL receives the parameter group, namely before the parameter group is processed by the GBT27930 IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Availability

| Since Version |
|---|
