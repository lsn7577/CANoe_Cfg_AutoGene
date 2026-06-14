# AvbListen

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbListen(dword listenerHandle, char onListenCallback[]);
```

## Description

The function causes the Listener to listen for incoming connection requests, which will be provided in the CAPL callback OnAvbListen passed to this function.

The function simultaneously listens for incoming connection requests for streams propagated via the following transport protocols:

Incoming connection requests can be accepted with AvbAccept from inside the provided callback function OnAvbListen.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
