# AvbSetProperty

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbSetProperty(char propertyName[], long value); //form 1
```

## Description

The behavior of the AVB IL can be configured using properties.

Properties can be set for the current bus context (form 1-2) as well as on an object-specific basis for talkers (form 3-4). The default settings for the properties can be obtained from the table below.

## Parameters

| Name | Type | Description |
|---|---|---|
| Name | Default Value | Description |
| Current bus context |  |  |
| StreamReservation | 1 | Stream Reservation is not supported. Set this property to 0. |
| Listener/Talker |  |  |
| VlanId | 2 | The VLAN ID to be used for sending or receiving AVB packets. |
| Listener |  |  |
| RtpPort | 1024 | Local client port used for RTP via UDP. RTP is always used in conjunction with RTCP. The RTCP UDP port number is one higher than the RTP port number. |
| RtspAddress | Not set/0 | Remote server address used for RT(S)P via TCP. If not set, no connection attempt to an RTSP server is made when AvbListen is called. |
| Talker |  |  |
| FramesPerPacket | Deduced from SR class and frame rate (if possible). | Constant number of frames per AVTPDU. |
| VlanPriority | 2 | The VLAN Priority to be used for sending AVB packets. |

## Return Values

0: The function was successfully executed.

## Example

```c
dword talkerHandle;

talkerHandle = AvbOpenTalker();
AvbSetProperty(talkerHandle, "FramesPerPacket", 64);
```

## Availability

| Since Version |
|---|
