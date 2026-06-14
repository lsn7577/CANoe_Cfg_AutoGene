# GetJ1939Address

> Category: `Test` | Type: `function`

## Syntax

```c
long GetJ1939Address (Node aNode);
```

## Description

Gets the current address of a J1939 node even the address has been changed by the J1939 network management.

## Return Values

Current address of the node

## Example

```c
dword address;
address = GetJ1939Address (N1);
Write("Address of node N1 is = %d", address );
```

## Availability

| Since Version |
|---|
