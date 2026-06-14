# diagSetCurrentEcu

> Category: `Obsolete` | Type: `notes`

## Description

When the current diagnostic target is a physical network request description, select the given ECU as target for single physical requests.

This function is only supported for physical network requests. If a request is sent using diagSendRequest, and not diagSendNetwork, the request is sent physically to the current ECU alone.

| Deprecated Function Starting with CANoe 10.0 SP3 Physical Network Requests were deactivated and therefore this function is no longer supported. If an existing configuration uses this functionality and you cannot replace it easily (using functional requests e.g.), please contact the Vector Support. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long diagSetCurrentEcu (char[] qualifier) |  |  |  |
| Function | When the current diagnostic target is a physical network request description, select the given ECU as target for single physical requests. This function is only supported for physical network requests. If a request is sent using diagSendRequest, and not diagSendNetwork, the request is sent physically to the current ECU alone. |  |  |  |
| Parameters | qualifier ECU identifier |  |  |  |
| Return Values | Error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.0 - 10.0 SP2 | Online mode | — | • |  |
| Example // Select a physical network request description as targetdiagSetTarget( "PNR1");// Send request to all targets on the networkreq1.SendNetwork();// Collect all responses from all ECUswhile( 1 == TestWaitForDiagResponse( req1, 1000)){ diagGetCurrentEcu( current, elcount(current)); write( "Received response from %s", current);}if( current[0] != 0){ // If there was a response, chose the last ECU to send another request to diagSetCurrentEcu( current); req2.SendRequest();} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
