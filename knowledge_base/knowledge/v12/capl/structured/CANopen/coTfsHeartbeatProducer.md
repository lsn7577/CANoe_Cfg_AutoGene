# coTfsHeartbeatProducer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsHeartbeatProducer( dword duration, dword producerTime, dword tolerance );
```

## Description

This function activates the heartbeat producer of the DUT Device Under Test. For this the object 0x1017 with producerTime is described via a SDO write access. After this, the regularity of the heartbeat message is checked and then the heartbeat producer is switched off again (0x1017 = 0). The test duration must be greater than the permitted time deviation.

At least two heartbeat messages of the DUT are awaited, even if the test duration is set shorter.

## Return Values

Error code

## Example

```c
if (coTfsHeartbeatProducer( 3000, 500, 10) != 1) { // duration, producerTime, tolerance
  write("heartbeat producer test failed");
}
```
