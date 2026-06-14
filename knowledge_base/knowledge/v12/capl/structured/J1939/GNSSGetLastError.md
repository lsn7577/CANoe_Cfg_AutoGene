# GNSSGetLastError

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSGetLastError();
```

## Description

This function returns the error status of the last GNSS function of a node to be performed. The individual error states are described here.

## Return Values

Error state of the last performed function

## Example

```c
GNSSStartSimulation( 0 );
if (GNSSGetLastError() != 0) {
  write(„Start of simulation failed“);
}
```

## Availability

| Since Version |
|---|
