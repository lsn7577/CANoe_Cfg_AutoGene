# Client States (TIM Component - ISO11783)

> Category: `ISO11783` | Type: `notes`

## Description

The following table contains the states of a connection from the TIM client to the TIM server. The state is used by the CAPL functions Iso11783IL_TIMConnectSysVarToState, Iso11783IL_TIMFreezeConnection and Iso11783IL_TIMContinueConnection.

TIM Component

| State | Name | Pre Condition | Action when State is Entered |
|---|---|---|---|
| 0 | Offline | Client is not started. Client is stopped (ISO11783IL_ControlStop). | — |
| 10 | Automation Unavailable | Address Claim succeeded. Iso11783IL_TIMConnectToServer is called to connect client a server. | Wait for TIM_ServerStatus_Msg of a server. If received switches to state Tim Server Status is received. |
| 11 | Tim Server Status is received | TIM_ServerStatus_Msg is received. | Send TIM_ConnectionVersionRequest to the server and switch to state Connection Version request is sent. |
| 12 | Connection Version request is sent | TIM_ConnectionVersionRequest is sent. | Wait for the TIM_ConnectionVersionResponse of the server. If the response is received validate content and switch to state Connection Version is valid or Initialization error. |
| 13 | Connection Version is valid | Check of the connection version succeeded. | Start sending cyclic TIM_ClientStatus_Msg. Send TIM_FunctionsSupportRequest to server and switch to state Supported functions request is sent. |
| 14 | Supported functions request is sent | TIM_FunctionsSupportRequest is sent to server. | Wait for TIM_FunctionsSupportResponse of the server. If response is received then switch to state Supported functions response is received if the required functions are supported else switch to state Initialization error. |
| 15 | Supported functions response is received | TIM_FunctionsSupportRequest is received. | If response contains the desired functions switch to state Automation not ready else switch to state Initialization error. |
| 16 | Initialization succeeded (equivalent to state ‘Automation not ready’ of the standard) | Initialization succeeded. | Switch to state Start authentication. |
| 19 | Initialization error | Initialization has been stopped due to timeout or unexpected response. | No action. You can switch to state Automation Unavailable by calling Iso11783IL_TIMConnectToServer. |
| 20 | Start authentication | Initialization succeeded. ISO1783IL_TIMRestartAuthentication Authentication is called after an authentication error. | Send Auth_ClientAuthenticationStatus with (Re)Start authentication bit. If Auth_ServerAuthenticationStatus with (Re)Start authentication Status bit set (to 1) is received then check if LwA is possible, calculate random challenge and reset (Re)Start authentication bit of Auth_ClientAuthenticationStatus. |
| 21 | Server starts authentication | Auth_ServerAuthenticationStatus with (Re)Start authentication Status bit set is received. | Send Auth_ServerRandomChallengeRequest and switch to state Server Random Challenge request is sent. |
| 22 | Server Random Challenge request is sent | Auth_ServerRandomChallengeRequest is sent. | Wait for Auth_ServerRandomChallengeResponse. |
| 23 | Server Random Challenge response is received | Auth_SererRandomChallengeResponse is received. | If full authentication (FwA) is necessary then send Auth_ServerCertificateRequest to the server to request the testlab certificate and switch to state Server testlab certificate request is sent. Else if lightweight authentication (LwA) is possible switch to state Calculate CMCA over received challenge. |
| 24 | Server testlab certificate request is sent | Auth_ServerCertificateRequest for testlab certificate is sent to the server. | Wait for the Auth_ServerCertificateResponse of the server. If the response is received and the authentication type, the certification format as well as the certification type is valid then the store the testlab certificate and switch to state Server testlab certificate response is received is received. Otherwise switch to state Authentication error. |
| 25 | Server testlab certificate response is received | Auth_ServerCertificateResponse with a testlab certificate is received | Send Auth_ServerCertificateRequest to the server to request the stored manufacturer certificate. Switch to state Server manufacturer certificate request sent. |
| 26 | Server manufacturer certificate request is sent | Auth_ServerCertificateRequest for manufacturer certificate is sent to the server. | Wait for the Auth_ServerCertificateResponse of the server. If the response is received and the authentication type, the certification format as well as the certification type is valid then the store the manufacturer certificate and switch to state Server manufacturer certificate response is received is received. Otherwise switch to state Authentication error. |
| 27 | Server manufacturer certificate response is received | Auth_ServerCertificateResponse with a manufacturer certificate is received. | Send Auth_ServerCertificateRequest to the server to request the stored manufacturer series certificate. Switch to state Server manufacturer series certificate request sent. |
| 28 | Server manufacturer series certificate request is sent | Auth_ServerCertificateRequest for manufacturer series certificate is sent to the server. | Wait for the Auth_ServerCertificateResponse of the server. If the response is received and the authentication type, the certification format as well as the certification type is valid then the store the manufacturer series certificate and switch to state Server manufacturer series certificate response is received is received. Otherwise switch to state Authentication error. |
| 29 | Server manufacturer series certificate response is received | Auth_ServerCertificateResponse with a manufacturer series certificate is received. | Send Auth_ServerCertificateRequest to the server to request the stored device certificate. Switch to state Server device certificate request sent. |
| 30 | Server device certificate request is sent | Auth_ServerCertificateRequest for device is sent to the server. | Wait for the Auth_ServerCertificateResponse of the server. If the response is received and the authentication type, the certification format as well as the certification type is valid then the store the device certificate and switch to state Server device certificate response is received is received. Otherwise switch to state Authentication error. |
| 31 | Server device certificate response is received | Auth_ServerCertificateResponse with a device certificate is received. | Send a request for the ISOBUS compliance certification notification (PGN FD42h) and switch to state Request for ISOBUS compliance certification is sent. |
| 32 | Request for ISOBUS compliance certification status is sent | Request for ISOBUS compliance certification notification is sent. | Wait for ISOBUS compliance certification notification. |
| 33 | ISOBUS compliance certification message is received | ISOBUS compliance certification notification is received. | Switch to state Start validating client certificates. |
| 34 | Start validating server certificates | All stored certificates of the server are requested by this client and all certificates which are added via Iso11783IL_TIMAddCertificate are requested by the server. | Check if received server certificates are listed on CRL and if they are valid. Furthermore, check the ISO NAME in the certificates as well as the ISO Version. If all check succeeded switch to state Authentication succeeded. Else switch to state Authentication Error. |
| 35 | Validation of server certificates succeeded | Check of the received server certificates succeeded. | Wait for a Auth_ServerAuthenticationStatus which signals that all certificates are valid. |
| 40 | Start key exchange | Server has successfully validated the certificates. | Switch to state Start calculating common secret. |
| 41 | Start calculating common secret | Random challenge of the server is received and full authentication (FwA) is necessary. | Client calculates a common secret using ECDH, use KDF to calculate a LwA key and store the LwA key in the key table. Then switch to state Calculate CMCA over received challenge. |
| 50 | Calculate CMCA over received challenge | — | Sign received challenge and send acknowledge for challenge signed to the server. Wait for acknowledgement for challenge signed of the server. Then switch to state Start CMCA Challenge Response. |
| 51 | Start CMAC challenge response | Both challenges are signed. | Send Auth_ServerSignedChallengeRequest to the server and switch to state Server Signed Challenge request is sent. |
| 52 | Server Signed Challenge request is sent | Auth_ServerSignedChallengeRequest is sent. | Wait for Auth_ServerSignedChallengeResponse. |
| 53 | Server Signed Challenge response is received | Auth_ServerSignedChallengeResponse is sent. | Wait for Auth_ClientSignedChallengeRequest. |
| 54 | Authentication succeeded | Authentication of client succeeded. | Stop sending Auth_ClientAuthenticationStatus after three more times. |
| 60 | Automation enabled | First TIM_FunctionsAssignmentResponse with status 1 (is assigned to requesting TIM client) and reason 0 (all clear/no reason) is received. | Send TIM_ClientStatus_Msg with State Automation Enable. Send TIM function request with value Ready to Control. |
| 70 | Automation active | First TIM function status with function automation status 5 (active, not limited), 6 (active, limited high) or 7 (active, limited low) is received. | — |
| 99 | Authentication error | Authentication Status notification with an error code is received. No Authentication Status notification is received for more than 3 seconds. | Depends on post condition. |

| Version 15© Vector Informatik GmbH |
|---|
