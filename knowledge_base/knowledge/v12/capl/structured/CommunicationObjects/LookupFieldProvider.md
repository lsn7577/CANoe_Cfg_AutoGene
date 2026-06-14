# LookupFieldProvider

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
fieldProviderRef * LookupFieldProvider(char[] path)
```

## Description

Searches for the specified field provider. The path must be complete including namespaces, endpoint and field: (Namespace::)Service[provider].field.

You can downcast the result to a concrete type, see the example.

## Return Values

The field provider. An uninitialized object if the field provider is not found, which will also be reported in the Write Window or as an error in test system (if the function is called in a test routine).

## Example

```c
fieldProviderRef MirrorAdjustment.Position positionField;
char path[200];
char service[50] = "Mirrors::MirrorAdjustment";
char provider[20] = "LeftMirror";
char fieldName[20] = "Position";

snprintf(path, elcount(path), "%s[%s].%s", service, provider, fieldName);
positionField = (fieldProviderRef MirrorAdjustment.Position) lookupFieldProvider(path);
```

## Availability

| Since Version |
|---|
