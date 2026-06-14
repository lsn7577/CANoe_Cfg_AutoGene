# mostGetFBlockID, mostGetFunctionID, mostGetOpType

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Please use the mostMessage and mostAMSMessage selectors FBlockID, FunctionID and OpType instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long mostGetFBlockID(mostMessage msg) |  |  |  |
| long mostGetFBlockID(mostAMSMessage msg) |  |  |  |  |
| long mostGetFunctionID(mostMessage msg) |  |  |  |  |
| long mostGetFunctionID(mostAMSMessage msg) |  |  |  |  |
| long mostGetOpType(mostMessage msg) |  |  |  |  |
| long mostGetOpType(mostAMSMessage msg) |  |  |  |  |
| Function | These functions return the FBlockID, FunctionID or OpType of the message. |  |  |  |
| Parameters | msg Message variable of type mostMessage or mostAMSMessage |  |  |  |
| Return Values | FblockId, FunctionId, OpType Note These values are determined independent of the message type and if applicable independent of the TelId. The Values are only valid if the message is out of the function catalog. | Note These values are determined independent of the message type and if applicable independent of the TelId. The Values are only valid if the message is out of the function catalog. |  |  |
| Note These values are determined independent of the message type and if applicable independent of the TelId. The Values are only valid if the message is out of the function catalog. |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.2 | MOST | • | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
