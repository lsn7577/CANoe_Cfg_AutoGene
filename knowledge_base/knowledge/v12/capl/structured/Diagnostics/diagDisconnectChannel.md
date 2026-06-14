# diagDisconnectChannel

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagDisconnectChannel(); // form 1
```

## Description

Disconnects a channel. State of the channel is Opened afterwards.

The channel the function refers to is set with the last call of diagSetTarget.

## Return Values

On success 0, otherwise error code.

## Availability

| Since Version |
|---|
