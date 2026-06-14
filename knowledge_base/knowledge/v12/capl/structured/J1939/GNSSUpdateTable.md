# GNSSUpdateTable

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSUpdateTable();
```

## Description

Updates the network table.

The function deletes the content of the current table and initiates the Request PGN that was used to request Address Claiming. After that, the table is restructured. If a node is forced off the network by another node with the same address, it remains intact in the network table with a NULL address. The content of the table is not deleted until this function is called. It also initiates an update of the table. Nodes reporting with the NULL address are not accepted in this process.

## Return Values

Error code

## Example

```c
GNSSUpdateTable();
```

## Availability

| Since Version |
|---|
