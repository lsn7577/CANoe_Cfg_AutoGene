# J1939DestroyECU

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939DestroyECU( dword ecuHandle );
```

## Description

This function deletes a logical node that was generated with J1939CreateECU() from the network.

You should therefore avoid allowing this function to be called within a CAPL callback function, since otherwise data consistency of the node layer could be violated.

## Return Values

0 on success or error code

## Example

```c
J1939DestroyECU(ecuHandle);
```

## Availability

| Since Version |
|---|
