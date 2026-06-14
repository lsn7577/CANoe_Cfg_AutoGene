# SomeIpSDSetServiceStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSDSetServiceStatus( dword psiHandle, long up );
```

## Description

The status of the Provided Service Instance is set at the node (producer).

## Parameters

| Name | Description |
|---|---|
| psiHandle | Handle of the required Consumed Service Instance (see SomeIpCreateProvidedServiceInstance). |
| up | 1: The status is changed to up. The sending of OfferServices is started. 0: The status is changed to down. A StopOfferService message is sent if the service was previously in up status. |

## Example

```c
dword appEndpointHandle;
dword serviceHandle;

appEndpointHandle = SomeIpOpenLocalApplicationEndpoint(kUDP, 30501);
serviceHandle  = SomeIpCreateConsumedServiceInstance(appEndpointHandle, 1 /*serviceId*/, 1 /*instanceId*/);
SomeIpSDSetServiceStatus(serviceHandle, 0); //do not offer this service
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
