# Diagnostics: Using Diagnostic Functions in Test Cases

> Category: `Diagnostics` | Type: `notes`

## Description

Waiting for diagnostic events is only possible in test modules! Conventional CAPL nodes continue to operate, but only by the event-driven principle.

After basic configuration of a diagnostic test module has been completed (the Target ECU can be selected in the MainTest function, for example), waiting for diagnostic events may be executed within the test module.

After a request has been sent the following phases are run through:

CANoe assumes the automatic handling of "Response Pending" (negative response with error code 0x78) responses of the ECU, i.e. this function does not return until another negative or positive response arrives, or until the timeout expires.

The return values of these functions conform to the following pattern:

To evaluate the ECU’s response the request can be used to access the last received response:

Finally, there are yet other functions that simplify the development of test cases for diagnostics:

The following test case shows the values of all possible states that may occur after a request is sent.

TestCase Test1(){ // Send Request and react to all possible cases. diagRequest Door.EcuIdentification_Read idReq; diagSendRequest( idReq); switch( TestWaitForDiagResponse( idReq, 200)) { case 0: // Timeout: The ECU did not respond within 200 ms. write("No answer from ECU!"); TestStepFail("Read ID", "No answer from ECU!"); break; case 1: // response received TestReportWriteDiagResponse(idReq); // write response to report if( diagGetLastResponseCode(idReq) == -1) { // A positive response was received write("ECU Diagnostics Identification: %d", (long)diagGetRespParameter(idReq,"Diagnostic_Identification")); TestStepPass("Read ID", "Positiv response received!"); } else // A negative response was received { write( "ECU Diagnostics Identification failed: 0x%x", diagGetLastResponseCode( idReq)); TestStepFail("Read ID", "Negative response received"); } break; default: // internal or setup error TestStepFail("Read ID", "Error in TestCase! Verdict unreliable."); }}

| Note Waiting for diagnostic events is only possible in test modules! Conventional CAPL nodes continue to operate, but only by the event-driven principle. |
|---|

| Note CANoe assumes the automatic handling of "Response Pending" (negative response with error code 0x78) responses of the ECU, i.e. this function does not return until another negative or positive response arrives, or until the timeout expires. |
|---|

| Example Test Case The following test case shows the values of all possible states that may occur after a request is sent. TestCase Test1(){ // Send Request and react to all possible cases. diagRequest Door.EcuIdentification_Read idReq; diagSendRequest( idReq); switch( TestWaitForDiagResponse( idReq, 200)) { case 0: // Timeout: The ECU did not respond within 200 ms. write("No answer from ECU!"); TestStepFail("Read ID", "No answer from ECU!"); break; case 1: // response received TestReportWriteDiagResponse(idReq); // write response to report if( diagGetLastResponseCode(idReq) == -1) { // A positive response was received write("ECU Diagnostics Identification: %d", (long)diagGetRespParameter(idReq,"Diagnostic_Identification")); TestStepPass("Read ID", "Positiv response received!"); } else // A negative response was received { write( "ECU Diagnostics Identification failed: 0x%x", diagGetLastResponseCode( idReq)); TestStepFail("Read ID", "Negative response received"); } break; default: // internal or setup error TestStepFail("Read ID", "Error in TestCase! Verdict unreliable."); }} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
