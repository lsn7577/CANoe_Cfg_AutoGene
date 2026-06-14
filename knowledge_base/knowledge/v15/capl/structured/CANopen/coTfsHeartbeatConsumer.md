# coTfsHeartbeatConsumer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsHeartbeatConsumer( dword virtProducerId, dword consumerTime, dword tolerance );
```

## Description

A heartbeat consumer is configured on the DUT Device Under Test (object 0x1016, sub index 1). The tester then sends a single heartbeat message as heartbeat producer. Thus a heartbeat event should be triggered for the heartbeat consumer. The tester now waits for an emergency message with the error code 0x8130. The DUT is now reset with a NMT reset command. The test waits for the coming boot-up message.

After this test, the device is in the pre-operational state.

## Parameters

| Name | Description |
|---|---|
| virtProducerId | This "virtual" node emulates the necessary heartbeat producer, this node number may not be assigned in the system to be tested. |
| consumerTime | Heartbeat consumer time in ms. |
| tolerance | Permissible tolerance (x - (tolerance/2) <= x <= x + (tolerance/2)) for the receipt of the emergency message. |

## Return Values

Error code

## Example

```c
if (coTfsHeartbeatConsumer( 122, 500, 100) != 1) { // virtProducerId, consumerTime, tolerance
  write( "hb consumer failed");
}
//after a successful test, the test node is in pre-operational state
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
