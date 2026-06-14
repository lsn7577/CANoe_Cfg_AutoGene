# mostApRegister

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApRegister(long fblockID, long instIDDefault)
```

## Description

The first function registers the CAPL node at the Application Socket as a function block with the specified FBlockID and InstIDDefault. The function is available in the CAPL section on preStart and can be applied once per CAPL node only.

The second function re-registers a previously de-registered CAPL node.

Both functions make an entry in the device's Local FBlockList. If an FBlock with the same FBlockID and InstID has already been registered by another CAPL node the InstID of the function block to be registered is incremented until the combination {FBlockID, InstID} is unique within the simulated device.

As a result of the call of mostApRegister(), if the network status is 'ConfigOk' the device's NetBlock reports the new Local FBlockList to the NetworkMaster.

## Return Values

See error codes

## Availability

| Since Version |
|---|
