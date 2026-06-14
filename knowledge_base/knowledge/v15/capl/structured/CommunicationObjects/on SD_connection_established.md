# on SD_connection_established

> Category: `CommunicationObjects` | Type: `event`

## Description

The event procedure is called when a connection is established between a consumer and a provider.

If you specify a single endpoint, the procedure is called for all connections of that endpoint and the other endpoint can be identified through the service selector of the this variable. If you specify both endpoints, the procedure is only called for the specific pair of consumer and provider and there is no this variable.

## Example

```c
on SD_connection_established Mirrors::MirrorAdjustment.consumerSide[CANoe]
{
  // subscribe event
  Abstract_SubscribeEvent(MirrorAdjustment.consumerSide[CANoe, this.service.ProviderIndex].CurrentPosition);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |

## Selectors

| service | Object representing the logical connection (the type is consumedServiceRef *) on consumer side and providedServiceRef * on provider side). |
|---|---|
