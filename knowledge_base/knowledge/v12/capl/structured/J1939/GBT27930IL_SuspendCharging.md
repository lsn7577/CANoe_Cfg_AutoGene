# GBT27930IL_SuspendCharging

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SuspendCharging( ); // form 1
```

## Description

Node suspends the charging. This function is only effective if the simulated node is in the Charging state. The Charger node stops sending the CCS message and starts sending the CST message. The BMS node stops sending the BCL, BCS and MSM messages and starts sending the BST message.

## Example

```c
—
```

## Availability

| Since Version |
|---|
