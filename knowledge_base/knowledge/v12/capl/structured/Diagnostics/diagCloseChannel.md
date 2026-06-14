# diagCloseChannel

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCloseChannel(); // form 1
```

## Description

Closes a diagnostic channel. State of the channel is Closed afterwards.

The channel the function refers to is set with the last call of diagSetTarget.

## Return Values

On success 0, otherwise error code.

## Availability

| Since Version |
|---|
