# Iso11783ECUGoOffline

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783ECUGoOffline( dword ecuHandle );
```

## Description

The function switches the state of the node to offline. It does not send a cannot claim address parameter group.

After calling this function the node cannot send any parameter groups, but it is responding to requests for address claim.

Use the function Iso11783ECUGoOnline to start the node again.

## Example

```c
Iso11783ECUGoOffline(ecuHdl);
```

## Availability

| Since Version |
|---|
