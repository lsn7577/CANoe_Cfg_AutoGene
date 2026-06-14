# EthGetAdapterStatus

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetAdapterStatus();
```

## Description

This function reads the state of the Ethernet interface.

## Example

```c
switch (EthGetAdapterStatus())
{
  case 0: write("Adapter status unknown"); break;
  case 1: write("Adapter is not connected”); break;
  case 2: write("Adapter is connected”); break;
}
```

## Availability

| Up to Version |
|---|
