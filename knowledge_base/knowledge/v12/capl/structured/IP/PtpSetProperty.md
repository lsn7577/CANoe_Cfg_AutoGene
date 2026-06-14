# PtpSetProperty

> Category: `IP` | Type: `function`

## Syntax

```c
long PtpSetProperty(char propertyName[], long value); // form 1
```

## Description

The behavior of the PTP layer can be configured using properties. You can statically configure the port role of a simulated node. This function allows for configuring properties to pre-set a configuration for the time-aware end station.

For example you can set the PortRole property to SlavePort (2) for a node in its on prestart CAPL event handler.

## Parameters

| Name | Description |
|---|---|
| Name | Description |
| PortRole | Values (Integer): 0 = Auto select (Role is selected by BMCA) (Default) 1 = MasterPort, 2 = SlavePort, 3 = PassivePort, 4 = DisabledPort Values > 0: By choosing a static PortRole the node will skip BMCA. The clock of such a node can therefore either be synchronizing other clocks (if the PortRole value is MasterPort) or be synchronized (PortRole is SlavePort) if connected to a node whose PortRole is MasterPort. |
| PortNumber | Values (Integer): 1 to 65535, Default: 1 This property affects sent Sync and Sync-follow-up messages of that node (when its PortRole is MasterPort). |
| LogSyncInterval | Values (Integer): -128 to 127, Default: -3 (equates to 0.125 s) This property modifies the time interval which is used for sending Sync (and Sync-follow-up) messages by the node. It can also be set implicitly over a Message interval request TLV (see 802.1AS-2011 10.5.4) sent out by another node on the network. In this case the actual LogSyncInterval is deduced from the payload of that gPTP Signaling message. |
| Priority1 | Values (Integer): 0 to 0xFF, Default: 0xFA Sets the Priority1 value of the System Identity. |
| ClockClass | Values (Integer): 0 to 0xFF, Default: 0xF8 Sets the ClockClass value of the System Identity. |
| ClockAccuracy | Values (Integer): 0 to 0xFF, Default: 0xFE Sets the ClockAccuracy value of the System Identity. |
| OffsetScaledLogVariance | Values (Integer): 0 to 65535, Default: 1 Sets the OffsetScaledLogVariance value of the System Identity. |
| Priority2 | Values (Integer): 0 to 0xFF, Default: 0xF8 Sets the Priority2 value of the System Identity. |
| VlanId | Values (Integer): 0 = No VLAN used (Default) 1 to 4094 = VLAN ID Sets the VLAN ID (VID) used for the gPTP communication. |
| VlanPriority | Values (Integer): 0 to 7, Default: 0 Sets the VLAN Priority (PCP – Priority Code Point) used for the gPTP communication. |
| RequestLogSyncInterval | This property cannot be set within the on preStart event handler. Values (Integer): -127 to 125 = Sync interval requested. 127 = Instructs the port that receives this TLV to stop sending time- synchronization event messages. 126 = Instructs the port that receives this TLV to reset its current LogSyncInterval to the initial value. -128 = Instructs the port that receives this TLV not to change the mean time interval between successive time- synchronization event messages. Sets the time sync interval requested from the port of the time aware system connected to this node. |
| RequestLogPdelayReqInterval | This property cannot be set within the on preStart event handler. Values (Integer): -127 to 125 = Propagation delay request interval requested. 127 = Instructs the port that receives this TLV to stop sending link delay measurement messages. 126 = Instructs the port that receives this TLV to reset its current LogPdelayReqInterval to the initial value. -128 = Instructs the port that receives this TLV not to change the mean time interval between successive propagation delay request messages. Sets the propagation delay request interval requested from the port of the time aware system connected to this node. |
| RequestLogAnnounceInterval | This property cannot be set within the on preStart event handler. Values (Integer): -127 to 125 = Announce interval requested. 127 = Instructs the port that receives this TLV to stop sending announce messages. 126 = Instructs the port that receives this TLV to reset its current LogAnnounceInterval to the initial value. -128 = Instructs the port that receives this TLV not to change the mean time interval between successive announce messages. Sets the announce interval requested from the port of the time aware system connected to this node. |
| DestinationAddress (since CANoe 11.0) | Sets the destination MAC address of PTP messages originating from the node. The function overload with the byte array type for the value parameter must be used. Set the length parameter to 6 and value parameter to the address in network byte order. If this property is not set, the default address 01:80:C2:00:00:0E will be used (Individual LAN Scope group address / Nearest Bridge group address, see IEEE 801.1AS). |
| LogPdelayReqInterval | Values (Integer): -128 to 127, Default: 0 (equates to 1 s) This property modifies the time interval which is used for sending Pdelay_Req messages by the node. It can also be set implicitly over a Message interval request TLV (see 802.1AS-2011 10.5.4) sent out by another node on the network. In this case the actual LogPdelayReqInterval is deduced from the payload of that gPTP Signaling message. |
| LogAnnounceInterval | Values (Integer): -128 to 127, Default: 0 (equates to 1 s) This property modifies the time interval which is used for sending Announce messages by the node. It can also be set implicitly over a Message interval request TLV (see 802.1AS-2011 10.5.4) sent out by another node on the network. In this case the actual LogAnnounceReqInterval is deduced from the payload of that gPTP Signaling message. |

## Return Values

0: The function succeeded.

## Availability

| Since Version |
|---|
