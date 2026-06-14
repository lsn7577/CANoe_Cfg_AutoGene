# Iso11783IL_TIMSetClientHeartbeatCounter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetClientHeartbeatCounter(dbNode server, byte hearbeatCounter); // form 1
```

## Description

Sets the heartbeat counter of message TIM_ClientStatus_Msg. The next status message uses the new heartbeat counter value.

If the new value is less than 251, then the counter is incremented as usual (after reaching the value 250 the counter restarts with value 0 again).

If the new value is 251 (0xFB), then after a single transmission of the status message with the value 251 the counter is reset to value 0 and incremented as usual.

If the new value of the counter is 252 or greater, then the status message is always sent with the same heartbeat counter value.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
