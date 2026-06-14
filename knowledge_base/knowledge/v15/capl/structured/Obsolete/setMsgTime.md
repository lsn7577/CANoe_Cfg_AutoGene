# setMsgTime

> Category: `Obsolete` | Type: `notes`

| Deprecated Function No replacement. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void setMsgTime(message m, NOW); |  |  |  |
| void setMsgTime(message m1, message m2); |  |  |  |  |
| Function | Assigns to one message the capture time of another message or the current time. This function is deprecated and only serves to establish compatibility with older versions. |  |  |  |
| Parameters | Variable of type "message" or "now". |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| — | • | • |  |  |
| Example setMsgTime(m100, this); // CANalyzer 1.xx & 2.xxm100.time = this.time; // CANalyzer 2.xxsetMsgTime (m101, now); |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
