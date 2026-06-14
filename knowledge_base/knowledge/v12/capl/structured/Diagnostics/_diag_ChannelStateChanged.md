# _diag_ChannelStateChanged

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
_diag_ChannelStateChanged(long newState)
```

## Description

Indicates the state of the diagnostic channel.

## Parameters

| Name | Description |
|---|---|
| 0 | ClosedChannel not opened yet or already closed. |
| 1 | OpenedChannel opened but no request successfully send yet or the attempt to send a request failed. |
| 2 | ConnectedRequest successfully send, no response received yet or expected response missed. |
| 3 | OnlineRequest and response successfully send and received. |
| 4 | ClosePendingClose requested but still pending, state Closed will follow. |
| 5 | ConnectPendingStartCommunication requested but still pending, if succeed state Connected will follow, otherwise state Opened. |

## Return Values

—

## Example

```c
_diag_ChannelStateChanged(long newState)
{
   gCurrentChannelState = newState;
}
```

## Availability

| Since Version |
|---|
