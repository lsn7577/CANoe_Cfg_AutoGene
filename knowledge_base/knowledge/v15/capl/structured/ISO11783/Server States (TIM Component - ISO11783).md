# Server States (TIM Component - ISO11783)

> Category: `ISO11783` | Type: `notes`

## Description

The following table contains the states of a connection from the TIM server to the TIM client. The state is used by the CAPL functions Iso11783IL_TIMConnectSysVarToState, Iso11783IL_TIMFreezeConnection and Iso11783IL_TIMContinueConnection.

TIM Component

| State | Name | Pre Condition | Action when State is Entered |
|---|---|---|---|
| 0 | Offline | Server is not activated. Server is stopped (ISO11783IL_ControlStop). | — |
| 5 | Automation unavailable | Address Claim succeeded. | — |
| 10 | Automation not ready | Server is activated (Iso11783IL_TIMActivateServer). | Waits for TIM_ConnectionVersionRequest of a client. |
| 11 | Connection Version request received | TIM_ConnectionVersionRequest is received. | Calculate the connection version which is used for the client and server connection and send TIM_ConnectionVersionResponse. |
| 12 | Connection Version response is sent | TIM_ConnectionVersionResponse is sent. | If TIM server and TIM client versions are incompatible switch to state Initialization error. Else switch to state Connection Version is valid. |
| 13 | Connection Version is valid | Valid connection version is found. | Wait for TIM_ClientStatus_Msg of the client with state Automation not ready or wait for Auth_ClientAuthenticationStatus message of the client. If one of the status notifications is received switch to state Initialization succeeded. |
| 16 | Initialization succeeded | Initialization has been finished successfully for the server. | Wait for Auth_ClientAuthenticationStatus with the (Re) Start authentication status bit set (to 1). |
| 19 | Initialization error | Initialization has been stopped due to timeout or unexpected response. | Wait for TIM_ConnectionVersionRequest to restart initialization. |
| 20 | Start authentication | Initialization succeeded. | Start sending Auth_ServerAuthenticationStatus with the (Re) Start authentication status bit set (to 1). If Auth_ClientAuthenticationStatus with the (Re) Start authentication status bit reset (to 0) is received then check if LwA is possible for this connection, calculate random challenge and reset (Re)Start authentication bit of Auth_ServerAuthenticationStatus. Switch to state Server starts authentication. |
| 21 | Server starts authentication | Auth_ClientAuthenticationStatus with reset (Re)Start authentication status bit is received. | Send Auth_ClientRandomChallengeRequest and switch to state Client Random Challenge request is sent. |
| 22 | Client Random Challenge request is sent | Auth_ClientRandomChallengeRequest is sent. | Wait for Auth_ClientRandomChallengeResponse. |
| 23 | Client Random Challenge Response is received | Auth_ClientRandomChallengeResponse is received. | If full authentication (FwA) is necessary then send Auth_ClientCertificateRequest for the testlab certificate and switch to state Client Testlab certificate request is sent. Else if lightweight authentication (LwA) is necessary switch to state Calculate CMCA over received challenge. |
| 24 | Client Testlab certificate request is sent | Auth_ClientCertificateRequest for the Testlab certificate is sent. | Wait for Auth_ClientCertificateResponse with the Testlab certificate. |
| 25 | Client Testlab certificate response is received | Auth_ClientCertificateResponse with the Testlab certificate is received. | Send Auth_ClientCertificateRequest for the manufacturer certificate. |
| 26 | Client manufacturer certificate request is sent | Auth_ClientCertificateRequest for the manufacturer certificate is sent. | Wait for Auth_ClientCertificateResponse with the manufacturer certificate. |
| 27 | Client manufacturer certificate is response received | Auth_ClientCertificateResponse with the manufacturer certificate is received. | Send Auth_ClientCertificateRequest for the manufacturer series certificate. |
| 28 | Client manufacturer series certificate request is sent | Auth_ClientCertificateRequest for the manufacturer series certificate is sent. | Wait for Auth_ClientCertificateResponse with the manufacturer series certificate. |
| 29 | Client manufacturer series certificate response is received | Auth_ClientCertificateResponse with the manufacturer series certificate is received. | Send Auth_ClientCertificateRequest for the device certificate. |
| 30 | Client device certificate request is sent | Auth_ClientCertificateRequest for the device certificate is sent. | Wait for Auth_ClientCertificateResponse with the device certificate. |
| 31 | Client device certificate response is received | Auth_ClientCertificateResponse with the device certificate is received. | Send a request for ECU Identification Information notification (PGN FDC5h). |
| 32 | Request for ISOBUS compliance certification status is sent | Request for ISOBUS compliance certification notification is sent. | Wait for ISOBUS compliance certification notification. |
| 33 | ISOBUS compliance certification message is received | ISOBUS compliance certification notification is received. | Switch to state Start validating client certificates. |
| 34 | Start validating client certificates | All certificates which are added via Iso11783IL_TIMAddCertificate are requested by the client and all stored certificates of the client are requested by this server. | Check if received client certificates are listed on CRL and if they are valid. Furthermore, check the ISO NAME in the certificates as well as the ISO Version. If all check succeeded switch to state Validation of client certificates succeeded. |
| 35 | Validation of client certificates succeeded | Check of the received client certificates succeeded. | Wait for a Auth_ClientAuthenticationStatus which signals that all certificates are valid. |
| 40 | Start key exchange | Server has successfully validated the certificates. | — |
| 41 | Start calculating common secret | Random challenge of the client is received and full authentication (FwA) is necessary. | Server calculates a common secret using ECDH, use KDF to calculate a LwA key and store the LwA key in the key table. Then switch to state Calculate CMCA over received challenge. |
| 50 | Calculate CMCA over received challenge | — | Sign received challenge and send acknowledge for challenge signed to the client. Wait for acknowledgement for challenge signed of the client. Then switch to state Start CMCA Challenge Response. |
| 51 | Start CMCA Challenge Response | Both challenges are signed. | Wait for Auth_ServerSignedChallengeRequest. |
| 52 | Client Signed Challenge Request is sent | Auth_ClientSignedChallengeRequest is sent. | Wait for Auth_ClientSignedChallengeResponse. |
| 53 | Client Signed Challenge Response is received | Auth_ClientSignedChallengeResponse is received. | Validate signed challenge response. If validation succeeded and Auth_ClientAuthenticationStatus notification with status Authenticated is received then switch to state Authentication succeeded. If validation failed, switch to state Authentication error. |
| 54 | Authentication succeeded | Authentication of server succeeded. | Stop sending Auth_ServerAuthenticationStatus after three more times. |
| 99 | Authentication error | Authentication has been stopped due to timeout or unexpected response. | — |

| Version 15© Vector Informatik GmbH |
|---|
