# mostConfigureBusloadCtrl

> Category: `MOST` | Type: `function`

## Syntax

```c
mostConfigureBusloadCtrl(rate, msg);
```

## Description

The function configures the bus load generator for the control channel. Load generation can be started with the mostGenerateBusloadCtrl() function.

Form 1:

With the specified rate the generator tries to send messages on the control channel.Due to repeated transmissions or arbitration delays, the bus load actually generated can deviate from the specified rate.As an option, the messages can be supplied with a sequence counter.

Form 2:

For OptoLyzer G2 3150o and OptoLyzer MOCCA compact 150c, rate specifies the delay between two messages in 1 ms steps and hence it is not possible to specify number of messages sent per second.

Bus load can also be generated without CAPL programming using the MOST Stress Window.

Repeated transmissions on the control channel can be eliminated by setting the OS8104 transmit retry register (XRTY) to 1 (mostWriteReq()).

A sequence counter and the stress pattern can be configured with mostSetStressNodeParameter.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected MOST hardware. |

## Return Values

<= 0: See error codes

## Example

Configure and start bus load stress on keyboard event.

```c
on key 's'
{
   long channel, rate;
   mostmessage NetBlock.DeviceInfo.Get msg;

   channel = 1;
   rate = 50; // msgs/s

   // set counter type: 1-byte
   mostSetStressNodeParameter(channel, 16, 1);

   // set counter in byte6 (first user data byte)
   mostSetStressNodeParameter(channel, 17, 6);

   // configure stress pattern
   msg.MsgChannel = channel;
   msg.DA = 0x100;
   mostConfigureBusloadCtrl(rate, msg);

   // start stress: send 10 messages
   mostGenerateBusloadCtrl(channel, 10);
}
```

## Availability

| Since Version |
|---|
