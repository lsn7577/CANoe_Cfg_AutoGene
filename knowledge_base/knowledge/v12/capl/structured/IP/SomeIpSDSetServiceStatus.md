# SomeIpSDSetServiceStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSDSetServiceStatus( dword psiHandle, long up );
```

## Description

The status of the Provided Service Instance is set at the node (producer).

## Return Values

0: The function was successfully executed

## Example

```c
dword appEndpointHandle;
dword serviceHandle;

appEndpointHandle = SomeIpOpenLocalApplicationEndpoint(kUDP, 30501);
serviceHandle  = SomeIpCreateConsumedServiceInstance(appEndpointHandle, 1 /*serviceId*/, 1 /*instanceId*/);
SomeIpSDSetServiceStatus(serviceHandle, 0); //do not offer this service
```

## Availability

| Since Version |
|---|
