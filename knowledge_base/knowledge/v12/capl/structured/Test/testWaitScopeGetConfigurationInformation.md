# testWaitScopeGetConfigurationInformation

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetConfigurationInformation (char deviceNames[][], dword deviceCount, char configurationNames[][], dword configurationCount);
```

## Description

Returns the available oscilloscopes and possible configurations.

The returned device names and function can be used with the function testWaitScopeSetConfiguration.

## Return Values

1 - Successful

## Availability

| Since Version |
|---|
