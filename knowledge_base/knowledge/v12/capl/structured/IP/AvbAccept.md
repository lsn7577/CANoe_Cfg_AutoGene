# AvbAccept

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbAccept(dword listenerHandle);
```

## Description

The function accepts an incoming connection request on the specified Listener resulting in a new Listener. If the operation fails, the function will return 0.

## Return Values

0: The function failed. Call AvbGetLastError to get a more specific error code.

## Availability

| Since Version |
|---|
