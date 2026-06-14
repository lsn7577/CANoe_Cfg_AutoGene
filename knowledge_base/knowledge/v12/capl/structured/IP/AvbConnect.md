# AvbConnect

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbConnect(dword talkerHandle, byte remoteMacAddress[], char onConnectCallback[]); // form 1
```

## Description

The function establishes a connection with the specified location. If the connect operation does not complete immediately the operation is performed asynchronously and the function will return 460609. In this case the passed CAPL callback OnAvbConnect will be called on completion (successful or not).

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
