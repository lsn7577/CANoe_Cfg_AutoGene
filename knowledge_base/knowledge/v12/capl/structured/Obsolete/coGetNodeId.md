# coGetNodeId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coGetNodeId( dword errCode[] );
```

## Description

The function returns the node-ID. If the function coStartUp was not executed yet, the function returns 0.

## Return Values

Node-ID

## Example

```c
dword errCode[1];
dword nodeId;

nodeId = coGetNodeId( errCode );
```

## Availability

| Up to Version |
|---|
