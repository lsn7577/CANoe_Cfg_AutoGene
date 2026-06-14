# FrSendMsg

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use function FRUpdateStatFrame or FROutputDynFrame instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | FrSendMsg ( class VIMessage* const message, unsigned int channel, unsigned char dataBytes[] ) |  |  |  |
| Function | This function generates a FlexRay frame and places it in the appropriate Tx register of the xModule/PC104. The xModule/PC104 sends the frame at the next possible transmission time. |  |  |  |
| Parameters | message Database message to be transmitted. |  |  |  |
| channel Channel over which transmission should occur. |  |  |  |  |
| dataBytes [] Data bytes that should be sent. |  |  |  |  |
| Return Values |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| FlexRay | — | • |  |  |
| Example variables{ message Identifier_01 msg_01; int gChannel_2 = 2 ;int gId_02 = 2 ;int gMux = 1 ;int gNoSync = 0 ;int gLen_Id2 = 4; Byte gData2a[12] = {0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c};Byte gData1a[12] = {0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c};}on key 'z'{ FrSendFrame(gId_02, gNoMux, gChannel_2, gNoSync, gLen_Id2, gData2a, -1 ); FrSendMsg (msg_01, gChannel_2, gData1a );} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
