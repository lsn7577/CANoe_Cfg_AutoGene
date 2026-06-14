# canGetErrorRate

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long canGetErrorRate(long channel)
```

## Description

Returns the current rate of CAN error messages of the specified channel.

## Parameters

| Name | Description |
|---|---|
| Vector API driver | Values 1 ... 32 |
| Softing API driver | Values 1, 2 |

## Return Values

Current Rate of CAN error messages on the specified channel in messages per second.

## Availability

| Up to Version |
|---|
