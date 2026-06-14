# Abstract_ReleaseAddress

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void Abstract_ReleaseAddress(addressHandle address)
```

## Description

Releases a pseudo address for abstract binding. You should call this for addresses which you do not need any more (because the endpoint will be removed) so that resources are freed.

## Return Values

—

## Example

```c
Abstract_ReleaseAddress(newProvider.Address);
```

## Availability

| Since Version |
|---|
