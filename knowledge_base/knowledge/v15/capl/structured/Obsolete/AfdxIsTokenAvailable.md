# AfdxIsTokenAvailable

> Category: `Obsolete` | Type: `notes`

## Description

This function is deprecated.

See Also

| Deprecated Function This function is deprecated. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long AfdxIsTokenAvailable( long packet, char protocolDesignator[], char tokenDesignator[] ); |  |  |  |
| Function | This function checks, if the specified token is part of the packet. |  |  |  |
| Parameters | packet handle of the message that has been created with AfdxInitPacket |  |  |  |
| protocolDesignator name of the protocol |  |  |  |  |
| tokenDesignator name of the token |  |  |  |  |
| Return Values | 1: token is part of the packet 0: token is not part of the packet |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.0 SP2 | AFDX | — | • |  |
| Example long packet;byte seqNo = 0;packet = AfdxInitPacket(0x0a022600, 0xe0e01a0f, 11121, 0x1a0f, 640);//check if Sequence number is available alreadyif (!AfdxIsTokenAvailable(packet, "afdx","seqNo")){ write("error! SeqNo is not available in AFDX-packet");}else{ // set SeqNo to specific value if (AfdxSetTokenInt(packet, "afdx", "SeqNo", 0, 1, 1, seqNo) != 0) { write("error! AfdxSetTokenInt failed"); }} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
