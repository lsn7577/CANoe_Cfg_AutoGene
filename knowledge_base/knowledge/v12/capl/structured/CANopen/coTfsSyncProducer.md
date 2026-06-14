# coTfsSyncProducer

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSyncProducer( void );
```

## Description

The call of this function starts a sync test that lasts 5 s. The sync producer in the DUT Device Under Test generates a sync message every 100 ms. The tolerance is ±10 ms. At the end of the test, the successful switch-off of the sync producer is checked.

This test does not support devices, which use the sync counter. Use the function coTfsSyncProducerDetail instead.

## Return Values

Error code

## Example

```c
coTfsSyncProducer();
```
