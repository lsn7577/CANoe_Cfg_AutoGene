# pduProviderRef::GetSubscribedConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
serviceConsumerRef * pduProviderRef::GetSubscribedConsumer(dword index)
```

## Description

Returns the subscribed consumer with the specified index.

## Return Values

The specified service consumer. An uninitialized object if the index is invalid.

## Example

```c
// output all subscribed consumers
                                
dword i, nrOfConsumers;
serviceConsumerRef * consumer;
pduProviderRef * provider;

provider = MirrorAdjustment.providerSide[LeftMirror].StatusPdu;
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
