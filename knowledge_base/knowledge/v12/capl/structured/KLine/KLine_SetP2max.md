# KLine_SetP2max

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP2max(dword P2max_us)
```

## Description

Sets the maximum time between the client (tester) request and the server (ECU) response, or between 2 server (ECU) responses.

## Return Values

0: Success

## Example

```c
on start
{
   KLine_SetP2Max(10000000); // P2max == 10 s
}
```

## Availability

| Since Version |
|---|
