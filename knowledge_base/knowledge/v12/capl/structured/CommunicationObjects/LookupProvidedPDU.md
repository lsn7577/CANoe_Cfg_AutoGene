# LookupProvidedPDU

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
providedPDURef * LookupProvidedPDU(char[] path)
```

## Description

Searches for the specified provided PDU. The path must be complete including namespaces and both endpoints: (Namespace::)+Service.providerSide[consumer,provider].PDU.

You can downcast the result to a concrete type, see the example.

## Return Values

The provided PDU. An uninitialized object if the PDU is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
providedPduRef MirrorAdjustment.Status statusPDU;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char consumer[20] = "CANoe";
char provider[20] = "LeftMirror";
char pduName[20] = "Status";

snprintf(path, elcount(path), "%s.providerSide[%s,%s].%s", service, consumer, provider, pduName);
statusPDU = (providedPDURef MirrorAdjustment.Status) lookupProvidedPDU(path);
```

## Availability

| Since Version |
|---|
