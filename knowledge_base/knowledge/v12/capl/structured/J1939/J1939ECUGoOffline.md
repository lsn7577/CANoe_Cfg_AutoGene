# J1939ECUGoOffline

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939ECUGoOffline( dword ecuHandle );
```

## Description

The function switches the state of the node to offline. It does not send a cannot claim address parameter group.

After calling this function the node cannot send any parameter groups, but it is responding to requests for address claim.

Use the function J1939ECUGoOnline to start the node again.

## Return Values

0 on success or error code

## Example

```c
J1939ECUGoOffline(ecuHdl);
```

## Availability

| Since Version |
|---|
