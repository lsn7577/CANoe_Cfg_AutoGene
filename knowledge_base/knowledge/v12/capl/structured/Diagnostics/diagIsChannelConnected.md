# diagIsChannelConnected

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsChannelConnected(); // form 1
```

## Description

Checks if a channel is already in state Connected.

The channel the function refers to is set with the last call of diagSetTarget.

## Return Values

1 if channel is connected, 0 if channel is not connected, otherwise error code.

## Availability

| Since Version |
|---|
