# fieldProviderRef::GetNrOfSubscribedConsumers

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword fieldProviderRef::GetNrOfSubscribedConsumers()
```

## Description

Returns the number of currently subscribed consumers for the service field.

## Return Values

The number of currently subscribed consumers.

## Example

```c
// output all subscribed consumers
                                
dword i, nrOfConsumers;
serviceConsumerRef * consumer;
fieldProviderRef * provider;

provider = MirrorAdjustment.providerSide[LeftMirror].CurrentPosition;
nrOfConsumers = provider.GetNrOfSubscribedConsumers();
write("Nr of consumers is %d", nrOfConsumers);
for (i = 0; i < nrOfConsumers; ++i)
{
  consumer = provider.GetSubscribedConsumer(i);
  write("Consumer %d is %s", i, consumer.Name);
}
```

## Availability

| Since Version |
|---|
