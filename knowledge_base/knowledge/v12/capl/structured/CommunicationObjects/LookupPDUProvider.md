# LookupPDUProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
pduProviderRef * LookupPDUProvider(char[] path)
```

## Description

Searches for the specified PDU provider. The path must be complete including namespaces, endpoint and PDU: (Namespace::)+Service[provider].PDU.

You can downcast the result to a concrete type, see the example.

## Return Values

The PDU provider. An uninitialized object if the PDU provider is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
pduProviderRef MirrorAdjustment.Status statusPDU;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char provider[20] = "LeftMirror";
char pduName[20] = "Status";

snprintf(path, elcount(path), "%s[%s].%s", service, provider, pduName);
statusPDU = (pduProviderRef MirrorAdjustment.Status) lookupPDUProvider(path);
```

## Availability

| Since Version |
|---|
