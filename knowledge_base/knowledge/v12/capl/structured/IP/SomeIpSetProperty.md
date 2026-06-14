# SomeIpSetProperty

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetProperty( char propertyName[], int64 value); // form 1
```

## Description

The behavior of the SOME/IP IL can be configured using properties.

Properties can be set for the current bus context as well as on an object-specific basis for services, Eventgroups, and Events. The default settings for the properties can be obtained from the table below.

## Parameters

| Name | Type | Description |
|---|---|---|
| Name | Default Value | Description |
| Current bus context |  |  |
| ClientId | Random | SomeIP-ClientId. Included in every message |
| MaxUDPMessageLength | 1416 | Sets the maximum allowed size of a SOME/IP message.Maximum size: 65519 |
| SDMulticastIp | 239.192.255.251 | If SD is done per IPv4, SD sends multicasts to this IPv4 destination address |
| SDMulticastPort | 30490 | SD sends multicasts to this port and, if necessary, opens a local endpoint with this port |
| SDMulticastIPv6 | FF02::1 | If SD is done per IPv6, SD sends multicasts to this IPv6 destination address |
| VlanId | — | This property may be set in on preStart to select a VLAN which needs to be configured for the current bus context. Furthermore the IL will use the first IP address of this VLAN for ServiceDiscovery and application endpoints that are created by SomeIpOpenLocalApplicationEndpoint. |
| UseSD | 1 | May be set to zero before service instances and event groups are created which should not be registered to the service discovery. |
| ProvidedServiceInstance |  |  |
| MajorVersion | 1 | Major version of the implemented interface |
| MinorVersion | 0 | Minor version of the implemented interface |
| SDCyclicOfferDelay | 1000 | Cycle time in ms |
| SDConfigurationString | — | Transmitted as option with OfferService. |
| ConsumedServiceInstance, ConsumedEventgroup |  |  |
| SDCyclicRequestDelay | 1000 | Cycle time in ms |
| ProvidedEventgroup |  |  |
| MulticastIp | 239.192.255.251 | Events of this EventGroup are sent to this Multicast IPv4 address |
| MulticastIpv6 | — | Events of this EventGroup are sent to this Multicast IPv6 address |
| MulticastPort | 30490 | Events of this EventGroup are sent to this Multicast port |
| UnicastLimit (deprecated) | 0 | 0: only multicast. 1: the first client will be served by unicast and as soon as a second client arrives both will be served by multicast. |
| MulticastThreshold | 0 | 0: only unicast will be used. 1: the first client will be already served by multicast. 2: the first client will be served with unicast and as soon as the second client arrives both will be served by multicast. n: the n-1 first clients will be served with unicast and as soon as the nth client arrives all will be served by multicast. |
| ProvidedEvent, ProvidedField |  |  |
| CycleTimeMs | 0 | Strictly speaking, an Event is NEVER sent cyclically, but for test purposes it is sometimes practical for generating traffic. |
| AliveCounterIncrementationOn | 1 | If the value is set to 1, an Alive counter that is responsible for a message is incremented on sending this message and transmitted with this message. This property works only with manufacturer specific databases. |
| UpdateCRCAndLengthOn | 1 | If the value is set to 1, the CRC value, the length and if applicable the so-called Data-ID (see AUTOSAR E2E Library specification) are adapted on sending a message. This property works only with manufacturer specific databases. |
| ProvidedServiceInstance, ConsumedServiceInstance, ConsumedEventgroup |  |  |
| SDTTL | 300 | TimeToLive in seconds |
| SDMinInitialDelay | 10 | Minimum delay in ms before first message |
| SDMaxInitialDelay | 30 | Maximum delay in ms before first message |
| SDMaxRepetition | 3 | Number or repetitions before cyclic sending |
| SDBaseRepetitionDelay | 30 | Time in ms. Delay between repetitions is then (2^#wdh)*basedelay |
| SDMinResponseDelay | 10 | Minimum delay in ms before sending a response |
| SDMaxResponseDelay | 30 | Maximum delay in ms before sending a response |

## Return Values

0: The function was successfully executed

## Example

```c
dword appEndpointHandle;
dword serviceHandle;

appEndpointHandle = SomeIpOpenLocalApplicationEndpoint(kUDP, 30501);
serviceHandle  = SomeIpCreateConsumedServiceInstance(appEndpointHandle, 1 /*serviceId*/, 1 /*instanceId*/);
SomeIpSetProperty(serviceHandle, "MajorVersion", 2);
```

## Availability

| Since Version |
|---|
