# Iso11783IL_TIMDeactivateServer

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMDeactivateServer( ); // form 1
```

## Description

Deactivates the TIM server.

For a graceful shutdown the TIM server gracefully releases all TIM functions being in automation. Then it sends three times in a row the Heartbeat counter value Graceful shutdown. And at the end it stops sending any messages (including TIM_ServerStatus_Msg).

For a none graceful shutdown of the TIM server stops sending any message at once including TIM_ServerStatus_Msg).

## Parameters

| Name | Type | Description |
|---|---|---|
| Option | Value | Description |
| Graceful shutdown | 01h | Server is gracefully shutdown |

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
