# AvbReceive

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbReceive(dword listenerHandle, int buffer[], dword& length, char onReceiveCallback[]); // form 1
```

## Description

The function receives data into the specified buffer.

If the receive operation completes immediately the function returns the number of received elements in the length parameter and the passed CAPL callback OnAvbReceive will not be called.

If the receive operation does not complete immediately the operation is performed asynchronously and the function will return 460609.

In this case the CAPL callback OnAvbReceive will be called on completion (successful or not).

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
