# coTfsHeartbeatConsumer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsHeartbeatConsumer( dword virtProducerId, dword consumerTime, dword tolerance );
```

## Description

A heartbeat consumer is configured on the DUT Device Under Test (object 0x1016, sub index 1). The tester then sends a single heartbeat message as heartbeat producer. Thus a heartbeat event should be triggered for the heartbeat consumer. The tester now waits for an emergency message with the error code 0x8130. The DUT is now reset with a NMT reset command. The test waits for the coming boot-up message.

After this test, the device is in the pre-operational state.

## Return Values

Error code

## Example

```c
if (coTfsHeartbeatConsumer( 122, 500, 100) != 1) { // virtProducerId, consumerTime, tolerance
  write( "hb consumer failed");
}
//after a successful test, the test node is in pre-operational state
```
