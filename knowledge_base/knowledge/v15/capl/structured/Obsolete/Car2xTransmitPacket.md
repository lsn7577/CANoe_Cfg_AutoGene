# Car2xTransmitPacket

> Category: `Obsolete` | Type: `notes`

## Description

void <OnC2xTransmitPacket> ( long packet )

Up to Version

See Also

| Deprecated Function Replaced by C2xRegisterCallback. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long C2xTransmitPacket( char *message, char *onC2xTransmitPacket) |  |  |  |
| Function | Registers a CAPL callback function that is invoked before transmission of a database defined packet. This allows the modification of signals and stack values before a packet is sent. The callback must have the following signature: void <OnC2xTransmitPacket> ( long packet ) |  |  |  |
| Parameters | message Name of the message for which the callback is invoked. The message needs to be configured as Tx message (with an appropriate Send Type) of this network node. |  |  |  |
| onC2xTransmitPacket Name of the CAPL callback. |  |  |  |  |
| Return Values | 0 or error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 9.0 | Car2x | — | • |  |
| Example on start{ C2xTransmitPacket("BasicSafetyMessage", "OnTxBSM") ;}void OnTxBSM(LONG packet){ C2xSetSignal("BasicSafetyMessage::blob1::_Blob_BSMblob::motion::heading", 90) ;} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
