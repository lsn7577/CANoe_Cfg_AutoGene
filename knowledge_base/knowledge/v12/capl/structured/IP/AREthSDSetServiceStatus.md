# AREthSDSetServiceStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSDSetServiceStatus( dword psiHandle, long up );
```

## Description

The status of the Provided Service Instance is set at the node (producer).

## Return Values

0: The function was successfully executed

## Example

```c
dword appEndpointHandle;
dword serviceHandle;

appEndpointHandle = AREthOpenLocalApplicationEndpoint(kUDP, 30501);
serviceHandle  = AREthCreateConsumedServiceInstance(appEndpointHandle, 1 /*serviceId*/, 1 /*instanceId*/);
AREthSDSetServiceStatus(serviceHandle, 0); //do not offer this service
```

## Availability

| Since Version |
|---|
