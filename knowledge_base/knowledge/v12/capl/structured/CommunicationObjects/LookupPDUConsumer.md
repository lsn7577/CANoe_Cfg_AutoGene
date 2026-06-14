# LookupPDUConsumer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
pduConsumerRef * LookupPDUConsumer(char[] path)
```

## Description

Searches for the specified PDU consumer. The path must be complete including namespaces, endpoint and PDU: (Namespace::)+Service[consumer].PDU.

You can downcast the result to a concrete type, see the example.

## Return Values

The PDU consumer. An uninitialized object if the PDU consumer is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
pduConsumerRef MirrorAdjustment.Status statusPDU;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char pduName[20] = "Status";

snprintf(path, elcount(path), "%s[%s].%s", service, consumer, pduName);
statusPDU = (pduConsumerRef MirrorAdjustment.Status) lookupPDUConsumer(path);
```

## Availability

| Since Version |
|---|
