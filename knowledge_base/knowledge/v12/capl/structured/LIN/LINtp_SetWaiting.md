# LINtp_SetWaiting

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_SetWaiting(long isWaiting);
```

## Description

Sets ISO TP waiting state for the node. When waiting has been activated the node will send FlowControl.Wait frames instead of ConsecutiveFrames, if sending of FlowControl frames has been activated.

## Return Values

—

## Availability

| Since Version |
|---|
