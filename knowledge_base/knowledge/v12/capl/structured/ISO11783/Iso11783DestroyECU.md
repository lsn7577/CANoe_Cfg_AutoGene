# Iso11783DestroyECU

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783DestroyECU( dword ecuHandle );
```

## Description

This function deletes a logical node that was generated with Iso11783CreateECU() from the network.

You should therefore avoid allowing this function to be called within a CAPL callback function, since otherwise data consistency of the node layer could be violated.

## Example

```c
Iso11783DestroyECU(ecuHandle);
```

## Availability

| Since Version |
|---|
