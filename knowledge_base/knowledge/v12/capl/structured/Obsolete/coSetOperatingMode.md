# coSetOperatingMode

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetOperatingMode( dword msgTriggered, dword cycleTime, dword errCode[] );
```

## Description

The function sets the work mode of the node. As default setting the node operates at a cycle time of 5 ms not triggered by messages. This means it is processed in a fixed grid. In extreme cases, 5 ms occur until an SDO request of another node is answered. If the node is set to message-triggered mode using this function now, it reacts as fast as possible to the messages sent to it. The indicated cycle time specifies in which time interval the node is executed. For example, this determines how fast given commands are processed or how occurring events (boot-up of a node) are reported to the application. This function allows the behavior of real ECUs to be better simulated because a fixed cycle time is often used here for the communication section of the software.

A short cycle time can be used simultaneously with message-triggered mode in order to obtain the fastest possible reaction of the node.

The real reaction time in message-triggered mode depends on multiple factors, for example, on the number of simulated nodes, the processor load, and the general performance of the PC.

## Return Values

—

## Example

```c
dword errCode[1];

// enable faster reaction times for messages
coSetOperatingMode( 1, 1, errCode );
if (errCode[0] == 0) {
  write( "Message triggered mode successfully set" );
}
```

## Availability

| Up to Version |
|---|
