# SCC_SetSchema

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetSchema ( char Namespace[] )
```

## Description

Sets the preferred schema version, corresponding to <SchemaNamespace> and optionally a specific version, in the XML configuration file.

The configured schema will be used unless a different one is derived from the SupportedAppProtocol handshake, and it will be prioritized during the handshake. If unspecified, the latest schema will have the highest priority.

When no version numbers are specified, depending on the context, it will mean any or latest version.

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
