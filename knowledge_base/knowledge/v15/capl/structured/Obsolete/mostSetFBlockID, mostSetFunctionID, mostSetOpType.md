# mostSetFBlockID, mostSetFunctionID, mostSetOpType

> Category: `Obsolete` | Type: `notes`

## Description

Database Support - Message-ID

| Deprecated Function The following functions are deprecated! Please use the mostMessage and mostAMSMessage selectors FBlockID, FunctionID and OpType instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void mostSetFBlockID(mostMessage msg, long value) |  |  |  |
| void mostSetFBlockID(mostAMSMessage msg, long value) |  |  |  |  |
| void mostSetFunctionID(mostMessage msg, long value) |  |  |  |  |
| void mostSetFunctionID(mostAMSMessage msg, long value) |  |  |  |  |
| void mostSetOpType(mostMessage msg, long value) |  |  |  |  |
| void mostSetOpType(mostAMSMessage msg, long value) |  |  |  |  |
| Function | Set the FBlockID, FunctionID or OpType of the message. Note Since the FBlockID, FunctionID and OpType are part of the message ID these functions change the ID as well. | Note Since the FBlockID, FunctionID and OpType are part of the message ID these functions change the ID as well. |  |  |
| Note Since the FBlockID, FunctionID and OpType are part of the message ID these functions change the ID as well. |  |  |  |  |
| Parameters | msg Variable of type mostMessage or mostAMSMessage. value Value to be set for FBlockID, FunctionID or OpType. |  |  |  |
| Return Values | — |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.2 | MOST | • | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
