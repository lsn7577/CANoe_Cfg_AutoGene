# Abstract_GetDisplayName

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_GetDisplayName(addressHandle address, char[] buffer)
```

## Description

Retrieves an display name for an endpoint with an abstract binding pseudo address. The name may have been set with Abstract_CreateAddress.

## Return Values

0: success

## Example

```c
ret = Abstract_GetDisplayName(newProvider.Address, buffer);
```

## Availability

| Since Version |
|---|
