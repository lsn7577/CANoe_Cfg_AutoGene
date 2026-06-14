# SCC_GetAppProtocolData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetAppProtocolData ( long Index, char ProtocolNamespace[], long& VersionMajor, long& VersionMinor, long& SchemaID, long& Priority )
```

## Description

Gets the content of an AppProtocol element of a SupportedAppProtocolReq message.

## Return Values

Protocol namespace string (100 characters) and all other parameters contained in the AppProtocol element with the specified list index.

## Availability

| Since Version |
|---|
