# KLine_SetP3max

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP3max(dword P3max_us)
```

## Description

Sets the maximum time between the end of the server (ECU) response and start of a new client (tester) request. If no request is sent in this interval, the ECU can assume that the tester is no longer present.

## Return Values

0: Success

## Example

```c
on start
{
   KLine_SetP3Max(3000000); // P3max == 3 s
}
```

## Availability

| Since Version |
|---|
