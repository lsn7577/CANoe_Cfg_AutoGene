# ChkQuery_EventNodeName

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventNodeName (dword CheckId, char buffer[], dword bufferlen);
check.QueryEventNodeName (char buffer[], dword bufferlen);
```

## Description

Stores the name of the node, for which the event has been sent, in the buffer and returns the length of the name, or 0 if specified for a range of nodes.

## Return Values

< 0: Refers the query error codes

## Availability

| Since Version |
|---|
