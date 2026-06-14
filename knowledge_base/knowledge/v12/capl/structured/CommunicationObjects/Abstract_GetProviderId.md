# Abstract_GetProviderId

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_GetProviderId(addressHandle address)
```

## Description

Returns an ID for a provider with an abstract binding pseudo address. Through the ID, you can identify the provider.

## Return Values

A unique ID for the provider.

## Example

```c
id = Abstract_GetProviderId(newProvider.Address);
```

## Availability

| Since Version |
|---|
