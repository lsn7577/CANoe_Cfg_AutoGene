# Abstract_GetConsumerId

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long Abstract_GetConsumerId(addressHandle address)
```

## Description

Returns an ID for a consumer with an abstract binding pseudo address. Through the ID, you can identify the consumer.

## Return Values

A unique ID for the consumer.

## Example

```c
id = Abstract_GetConsumerId(newConsumer.Address);
```

## Availability

| Since Version |
|---|
