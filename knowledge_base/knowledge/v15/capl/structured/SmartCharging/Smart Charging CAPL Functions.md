# Smart Charging CAPL Functions

> Category: `SmartCharging` | Type: `notes`

## Description

SCC_CertChainVerificationInd

The callback is called when a received certificate chain (e.g. ContractSignatureCertChain) is verified.

SCC_CreateSessionStopRes_ISO

Shared Functions

SCC_CreateCM_Amp_Map_Cnf

Creates a CM_Amp_Map.Cnf message.

SCC_CreateCM_Amp_Map_Req

Creates a CM_Amp_Map.Req message.

Creates a CM_Validate.Cnf message.

Creates a CM_Validate.Req message.

Creates a VS_Nw_Info.Req message.

Creates a VS_PL_Lnk_Status.Cnf message.

Creates a VS_PL_Lnk_Status.Req message.

Creates a SECC Discovery Response.

Creates a SupportedAppProtocol Request.

Creates a SupportedAppProtocol Response.

SCC_GetCertChainVerificationError

SCC_GetCertChainVerificationErrorCount

SCC_GetMinVoltage

SCC_GetPMaxScheduleID

Gets the ID of a PMaxSchedule (DIN 70121).

Gets the ID of an SAScheduleTuple entry within a ChargeParameterDiscoveryRes message.

SCC_SetSelectedService

SCC_SetServiceDetailRequest

SCC_SetWeldingDetectionCount

SCC_Shutdown

SCC_StartCertificateInstallation

Enables or disables the payment option ExternalPayment.

Sets the power spectral density for Amplitude Map Exchange.

SCC_SLAC_GetRandomValue

| SMART CHARGING Only available with option .SmartCharging. To use the CAPL functions, the node layer SCC_Vehicle.dll and/or SCC_ChargePoint.dll must be included. You can include the node layer by using the configuration dialog of the node on page Components. All response callbacks with ResponseCode parameter contain a Boolean parameter in their signatures that specifies the type of response code. |
|---|

| Shared | Vehicle only | Charge Point only |  |
|---|---|---|---|
| Callback Functions | EV/EVSE | EV | EVSE |
| V2G test functions (ISO 15118 messages) | EV/EVSE | — | — |
| V2G test functions (DIN messages) | EV/EVSE | — | — |
| SLAC test functions (messages) | EV/EVSE | — | — |
| V2G test functions (schema independent) | EV/EVSE | — | — |
| General functions | EV/EVSE | — | — |
| V2G data queries (only during callback) | EV/EVSE | EV | EVSE |
| V2G simulation data (read) | EV/EVSE | EV | EVSE |
| Test Functions (general) | EV/EVSE | — | — |
| Simulation control | EV/EVSE | EV | — |
| V2G simulation data (write) | EV/EVSE | — | — |
| V2G simulation control | EV/EVSE | EV | EVSE |
| SLAC simulation | EV/EVSE | — | EVSE |
| SLAC data queries (only during callback) | EV/EVSE | EV | EVSE |

| Shared Callback Functions | Short Description |
|---|---|
| SCC_CertChainVerificationInd | The callback is called when a received certificate chain (e.g. ContractSignatureCertChain) is verified. |
| SCC_CM_Amp_Map_Cnf | The callback is called as soon as a CM_Amp_Map.Cnf message is received. |
| SCC_CM_Amp_Map_Req | The callback is called as soon as a CM_Amp_Map.Req message is received. |
| SCC_CM_Set_Key_Cnf | This callback is called as soon as a CM_Set_Key.Cnf message is received. |
| SCC_ConnectionTimeoutInd | This callback is called when a connection is closed due to inactivity. |
| SCC_InvalidMessageInd | The callback is called when a SDP or V2G message is received with an invalid content (i.e. it is rejected by the session layer). |
| SCC_LinkStatusChangeInd | This callback is called each time the internally stored link status changes by means of link status polling. |
| SCC_MessageRxInd | The callback is called each time a Vehicle2Grid, SECC Discovery or SLAC message is received by the simulation DLL. |
| SCC_MessageTxInd | This callback is called each time a Vehicle2Grid, SECC Discovery or SLAC message is sent by the simulation DLL. |
| SCC_ProtocolFinishedInd | This callback is called when a protocol run has been successfully finished. |
| SCC_SignaturePreSendInd | This callback is called when a signature for a message has been created. |
| SCC_SignatureVerificationInd | This callback is called when a signed V2G message is verified with the ECDSA algorithm. |
| SCC_SLACFinishedInd | This callback is called when a SLAC run has been completed. |
| SCC_StateTransitionInd | This callback is called each time the internal state machine switches its state, i.e. usually when a new message is received. |
| SCC_TCPConnectInd | This callback is called when a TCP connection is opened. |
| SCC_TCPShutdownInd | This callback is called when a TCP connection is closed. |
| SCC_TLSHandshakeInd | This callback is called when a TLS handshake has been attempted after the SECC Discovery procedure. |
| SCC_VS_Nw_Info_Cnf | This callback is called as soon as a VS_Nw_Info.Cnf message is received. |
| SCC_VS_PL_Lnk_Status_Cnf | This callback is called as soon as a VS_PL_Lnk_Status.Cnf message is received. |
| EV Callback Functions [▲ back] | Short Description |
| SCC_AuthorizationRes | This callback is called as soon as a Authorization Response is received. |
| SCC_CableCheckRes | This callback is called as soon as a Cable Check Response is received. |
| SCC_CertificateInstallationRes | This callback is called as soon as a Certificate Installation Response is received. |
| SCC_CertificateUpdateRes | This callback is called as soon as a Certificate Installation Response is received. |
| SCC_ChargeParameterDiscoveryRes | This callback is called as soon as a Charge Parameter Discovery Response is received. |
| SCC_ChargingStatusRes | This callback is called as soon as a Charging Status Response is received. |
| SCC_CM_SLAC_Parm_Cnf | This callback is called as soon as a CM_SLAC_Parm.Cnf message is received. |
| SCC_CM_Atten_Char_Ind | This callback is called as soon as a CM_Atten_Char.Ind message is received. |
| SCC_CM_Validate_Cnf | This callback is called as soon as a CM_Validate.Cnf message is received. |
| SCC_CM_SLAC_Match_Cnf | This callback is called as soon as a CM_SLAC_Match.Cnf message is received. |
| SCC_ContractAuthenticationRes | This callback is called as soon as a Contract Authentication Response is received. |
| SCC_CurrentDemandRes | This callback is called as soon as a Current Demand Response is received. |
| SCC_ErrorStateInd | This callback is called as soon as the node enters or exits the error state. |
| SCC_MeteringReceiptRes | This callback is called as soon as a Metering Receipt Response is received. |
| SCC_PaymentDetailsRes | This callback is called as soon as a Service Payment Selection Response is received. |
| SCC_PaymentServiceSelectionRes | This callback is called as soon as a Service Payment Selection Response is received. |
| SCC_PowerDeliveryRes | This callback is called as soon as a Power Delivery Response is received. |
| SCC_PreChargeRes | This callback is called as soon as a PreCharge Response is received. |
| SCC_RestartInd | This callback is called as soon as the vehicle restarts the protocol after a disconnection. |
| SCC_SECCDiscoveryRes | This callback is called as soon as an SECC Discovery Response is received. |
| SCC_ServiceDetailRes | This callback is called as soon as a Service Detail Response is received. |
| SCC_ServiceDiscoveryRes | This callback is called as soon as a Service Discovery Response is received. |
| SCC_ServicePaymentSelectionRes | This callback is called as soon as a Service Payment Selection Response is received. |
| SCC_SessionSetupRes | This callback is called as soon as a Session Setup Response is received. |
| SCC_SessionStopRes | This callback is called as soon as a Session Stop Response is received. |
| SCC_SupportedAppProtocolRes | This callback is called as soon as a Supported App Protocol Response is received. |
| SCC_V2G_EVCC_Msg_TimeoutInd | This callback is called as soon as an V2G_EVCC_Msg_Timeout occurs. |
| SCC_V2G_EVCC_PreCharge_TimeoutInd | This callback is called as soon as an V2G_EVCC_PreCharge_Timeout occurs. |
| SCC_V2G_EVCC_CableCheck_TimeoutInd | This callback is called as soon as an V2G_EVCC_CableCheck_Timeout occurs. |
| SCC_WeldingDetectionRes | This callback is called as soon as a Welding Detection Response is received. |
| EVSE Callback Function [▲ back] | Short Description |
| SCC_AuthorizationReq | This callback is called as soon as an Authorization Request is received. |
| SCC_CableCheckReq | This callback is called as soon as a Cable Check Request is received. |
| SCC_ChargeParameterDiscoveryReqAC | This callback is called as soon as a Charge Parameter Discovery Request is received. |
| SCC_ChargeParameterDiscoveryReqDC | This callback is called as soon as a Charge Parameter Discovery Request is received. |
| SCC_ChargingStatusReq | This callback is called as soon as a Charging Status Request is received. |
| SCC_CertificateInstallationReq | This callback is called as soon as a Certificate Installation Request is received. |
| SCC_CertificateUpdateReq | This callback is called as soon as a Certificate Installation Request is received. |
| SCC_CM_Slac_Parm_Req | This callback is called as soon as a CM_Slac_Parm.Req message is received. |
| SCC_CM_Start_Atten_Char_Ind | This callback is called as soon as a CM_Start_Atten_Char.Ind message is received. |
| SCC_CM_MNBC_Sound_Ind | This callback is called as soon as a CM_MNBC_Sound.Ind message is received. |
| SCC_CM_Atten_Profile_Ind | This callback is called as soon as a CM_Atten_Profile.Ind message is received. |
| SCC_CM_Atten_Char_Rsp | This callback is called as soon as a CM_Atten_Char.Rsp message is received. |
| SCC_CM_Validate_Req | This callback is called as soon as a CM_Validate.Req message is received. |
| SCC_CM_SLAC_Match_Req | This callback is called as soon as a CM_SLAC_Match.Req message is received. |
| SCC_ContractAuthenticationReq | This callback is called as soon as a Contract Authentication Request is received. |
| SCC_CurrentDemandReq | This callback is called as soon as a Current Demand Request is received. |
| SCC_MeteringReceiptReq | This callback is called as soon as a Metering Receipt Request is received. |
| SCC_PaymentDetailsReq | This callback is called as soon as a Payment Details Request is received. |
| SCC_PaymentServiceSelectionReq | This callback is called as soon as a Payment Service Selection Request is received. |
| SCC_PowerDeliveryReq | This callback is called as soon as a Power Delivery Request is received. |
| SCC_PreChargeReq | This callback is called as soon as a PreCharge Request is received. |
| SCC_PreSendInd | This callback is called in active mode before a response message is sent. |
| SCC_SchemaSelectionInd | Indicates that a schema has been chosen via the SupportedAppProtocol handshake. |
| SCC_SECCDiscoveryReq | This callback is called as soon as a SECC Discovery Request is received. |
| SCC_ServiceDetailReq | This callback is called as soon as a Service Detail Request is received. |
| SCC_ServiceDiscoveryReq | This callback is called as soon as a Service Discovery Request is received. |
| SCC_ServicePaymentSelectionReq | This callback is called as soon as a Service Payment Selection Request is received. |
| SCC_SessionSetupReq | This callback is called as soon as a Session Setup Request is received. |
| SCC_SessionStopReq | This callback is called as soon as a Session Stop Request is received. |
| SCC_SupportedAppProtocolReq | This callback is called as soon as a SupportedAppProtocol Request is received. |
| SCC_WeldingDetectionReq | This callback is called as soon as a Welding Detection Request is received. |

| Shared Functions | Short Description |
|---|---|
| SCC_CreateAuthorizationReq_ISO | Creates a Contract Authentication Request. |
| SCC_CreateAuthorizationRes_ISO | Creates a Contract Authentication Response. |
| SCC_CreateCableCheckReq_ISO | Creates a Cable Check Request. |
| SCC_CreateCableCheckRes_ISO | Creates a Cable Check Response. |
| SCC_CreateCertificateInstallationReq_ISO | Creates a Certificate Installation Request. |
| SCC_CreateCertificateInstallationRes_ISO | Creates a Certificate Installation Response. |
| SCC_CreateCertificateUpdateReq_ISO | Creates a Certificate Installation Request. |
| SCC_CreateCertificateUpdateRes_ISO | Creates a Certificate Installation Response. |
| SCC_CreateChargeParameterDiscoveryReqAC_ISO | Creates a Charge Parameter Discovery Request (AC syntax). |
| SCC_CreateChargeParameterDiscoveryReqDC_ISO | Creates a Charge Parameter Discovery Request (DC syntax). |
| SCC_CreateChargeParameterDiscoveryResAC_ISO | Creates a Charge Parameter Discovery Response (AC syntax). |
| SCC_CreateChargeParameterDiscoveryResDC_ISO | Creates a Charge Parameter Discovery Response (DC syntax). |
| SCC_CreateChargingStatusReq_ISO | Creates a Charging Status Request. |
| SCC_CreateChargingStatusRes_ISO | Creates a Charging Status Response. |
| SCC_CreateCurrentDemandReq_ISO | Creates a Current Demand Request. |
| SCC_CreateCurrentDemandRes_ISO | Creates a Current Demand Response. |
| SCC_CreateMeteringReceiptReq_ISO | Creates a Metering Receipt Request. |
| SCC_CreateMeteringReceiptResAC_ISO | Creates a Metering Receipt Response (AC variant). |
| SCC_CreateMeteringReceiptResDC_ISO | Creates a Metering Receipt Response (DC variant). |
| SCC_CreatePaymentDetailsReq_ISO | Creates a Payment Details Request. |
| SCC_CreatePaymentDetailsRes_ISO | Creates a Payment Details Response. |
| SCC_CreatePaymentServiceSelectionReq_ISO | Creates a Service Payment Selection Request with a user defined SelectedServiceList. |
| SCC_CreatePaymentServiceSelectionRes_ISO | Creates a Service Payment Selection Response. |
| SCC_CreatePowerDeliveryReqAC_ISO | Creates a Power Delivery Request (AC syntax). |
| SCC_CreatePowerDeliveryReqDC_ISO | Creates a Power Delivery Request (DC syntax). |
| SCC_CreatePowerDeliveryResAC_ISO | Creates a Power Delivery Response (AC syntax). |
| SCC_CreatePowerDeliveryResDC_ISO | Creates a Power Delivery Response (DC syntax). |
| SCC_CreatePreChargeReq_ISO | Creates a PreCharge Request. |
| SCC_CreatePreChargeRes_ISO | Creates a PreCharge Response. |
| SCC_CreateServiceDetailReq_ISO | Creates a Service Detail Request. |
| SCC_CreateServiceDetailRes_ISO | Creates a Service Detail Response. |
| SCC_CreateServiceDiscoveryReq_ISO | Creates a Service Discovery Request. |
| SCC_CreateServiceDiscoveryRes_ISO | Creates a Service Discovery Response. |
| SCC_CreateSessionSetupReq_ISO | Creates a Session Setup Request. |
| SCC_CreateSessionSetupRes_ISO | Creates a Session Setup Response. |
| SCC_CreateSessionStopReq_ISO | Creates a Session Stop Request. |
| SCC_CreateSessionStopRes_ISO | Creates a Session Stop Response. |
| SCC_CreateWeldingDetectionReq_ISO | Creates a Welding Detection Request. |
| SCC_CreateWeldingDetectionRes_ISO | Creates a Welding Detection Response. |

| Shared Functions | Short Description |
|---|---|
| SCC_CreateCableCheckReq_DIN | Creates a Cable Check Request. |
| SCC_CreateCableCheckRes_DIN | Creates a Cable Check Response. |
| SCC_CreateCertificateInstallationReq_DIN | Creates a Certificate Installation Request. |
| SCC_CreateCertificateInstallationRes_DIN | Creates a Certificate Installation Response. |
| SCC_CreateCertificateUpdateReq_DIN | Creates a Certificate Installation Request. |
| SCC_CreateCertificateUpdateRes_DIN | Creates a Certificate Installation Response. |
| SCC_CreateChargeParameterDiscoveryReqAC_DIN | Creates a Charge Parameter Discovery Request (AC syntax). |
| SCC_CreateChargeParameterDiscoveryReqDC_DIN | Creates a Charge Parameter Discovery Request (DC syntax). |
| SCC_CreateChargeParameterDiscoveryResAC_DIN | Creates a Charge Parameter Discovery Response (AC syntax). |
| SCC_CreateChargeParameterDiscoveryResDC_DIN | Creates a Charge Parameter Discovery Response (DC syntax). |
| SCC_CreateChargingStatusReq_DIN | Creates a Charging Status Request. |
| SCC_CreateChargingStatusRes_DIN | Creates a Charging Status Response. |
| SCC_CreateContractAuthenticationReq_DIN | Creates a Contract Authentication Request. |
| SCC_CreateContractAuthenticationRes_DIN | Creates a Contract Authentication Response. |
| SCC_CreateCurrentDemandReq_DIN | Creates a Current Demand Request. |
| SCC_CreateCurrentDemandRes_DIN | Creates a Current Demand Response. |
| SCC_CreateMeteringReceiptReq_DIN | Creates a Metering Receipt Request. |
| SCC_CreateMeteringReceiptResAC_DIN | Creates a Metering Receipt Response (AC variant). |
| SCC_CreatePaymentDetailsReq_DIN | Creates a Payment Details Request. |
| SCC_CreatePaymentDetailsRes_DIN | Creates a Payment Details Response. |
| SCC_CreatePowerDeliveryReqAC_DIN | Creates a Power Delivery Request (AC syntax). |
| SCC_CreatePowerDeliveryReqDC_DIN | Creates a Power Delivery Request (DC syntax). |
| SCC_CreatePowerDeliveryResAC_DIN | Creates a Power Delivery Response (AC syntax). |
| SCC_CreatePowerDeliveryResDC_DIN | Creates a Power Delivery Response (DC syntax). |
| SCC_CreatePreChargeReq_DIN | Creates a PreCharge Request. |
| SCC_CreatePreChargeRes_DIN | Creates a PreCharge Response. |
| SCC_CreateServiceDetailReq_DIN | Creates a Service Detail Request. |
| SCC_CreateServiceDetailRes_DIN | Creates a Service Detail Response. |
| SCC_CreateServiceDiscoveryReq_DIN | Creates a Service Discovery Request. |
| SCC_CreateServiceDiscoveryRes_DIN | Creates a Service Discovery Response. |
| SCC_CreateServicePaymentSelectionReq_DIN | Creates a Service Payment Selection Request with a user defined SelectedServiceList. |
| SCC_CreateServicePaymentSelectionRes_DIN | Creates a Service Payment Selection Response. |
| SCC_CreateSessionSetupReq_DIN | Creates a Session Setup Request. |
| SCC_CreateSessionSetupRes_DIN | Creates a Session Setup Response. |
| SCC_CreateSessionStopReq_DIN | Creates a Session Stop Request. |
| SCC_CreateSessionStopRes_DIN | Creates a Session Stop Response. |
| SCC_CreateWeldingDetectionReq_DIN | Creates a Welding Detection Request. |
| SCC_CreateWeldingDetectionRes_DIN | Creates a Welding Detection Response. |

| Shared Functions | Short Description |
|---|---|
| SCC_CreateCM_Amp_Map_Cnf | Creates a CM_Amp_Map.Cnf message. |
| SCC_CreateCM_Amp_Map_Req | Creates a CM_Amp_Map.Req message. |
| SCC_CreateCM_Atten_Char_Ind | Creates a CM_Atten_Char.Ind message. |
| SCC_CreateCM_Atten_Char_Rsp | Creates a CM_Atten_Char.Rsp message. |
| SCC_CreateCM_Atten_Profile_Ind | Creates a CM_Atten_Profile.Ind message. |
| SCC_CreateCM_MNBC_Sound_Ind | Creates a CM_MNBC_Sound.Ind message. |
| SCC_CreateCM_SLAC_Match_Cnf | Creates a CM_SLAC_Match.Cnf message. |
| SCC_CreateCM_SLAC_Match_Req | Creates a CM_SLAC_Match.Req message. |
| SCC_CreateCM_SLAC_Parm_Cnf | Creates a CM_SLAC_Parm.Cnf message. |
| SCC_CreateCM_SLAC_Parm_Req | Creates a CM_Slac_Parm.Req message. |
| SCC_CreateCM_Set_Key_Cnf | Creates a CM_Set_Key.Cnf message. |
| SCC_CreateCM_Set_Key_Req | Creates a CM_Set_Key.Req message. |
| SCC_CreateCM_Start_Atten_Char_Ind | Creates a CM_Start_Atten_Char.Ind message. |
| SCC_CreateCM_Validate_Cnf | Creates a CM_Validate.Cnf message. |
| SCC_CreateCM_Validate_Req | Creates a CM_Validate.Req message. |
| SCC_CreateVS_Nw_Info_Req | Creates a VS_Nw_Info.Req message. |
| SCC_CreateVS_PL_Lnk_Status_Cnf | Creates a VS_PL_Lnk_Status.Cnf message. |
| SCC_CreateVS_PL_Lnk_Status_Req | Creates a VS_PL_Lnk_Status.Req message. |

| Shared Functions | Short Description |
|---|---|
| SCC_CreateSECCDiscoveryReq | Creates a SECC Discovery Request. |
| SCC_CreateSECCDiscoveryRes | Creates a SECC Discovery Response. |
| SCC_CreateSupportedAppProtocolReq | Creates a SupportedAppProtocol Request. |
| SCC_CreateSupportedAppProtocolRes | Creates a SupportedAppProtocol Response. |

| Shared Functions | Short Description |
|---|---|
| SCC_GenerateRandomData | Fills an array with random numbers. |
| SCC_GetCertChainVerificationError | Returns the number of verification errors from the last certificate chain verification. |
| SCC_GetCertChainVerificationErrorCount | Returns the number of verification errors from the last certificate chain verification. |
| SCC_GetDLLInfo | Retrieves additional information about DLL and settings. |
| SCC_GetEthernetSettings | Returns the SCC nodes's IP/Ethernet configuration. |
| SCC_GetStateName | Gets a string representation of a state enum value. |
| SCC_SetVerbosity | Sets DLL verbosity. |

| Shared Functions | Short Description |
|---|---|
| SCC_GetCertificateChainCertificate | Gets a certificate from the ContractSignatureCertChain, where index 0 denotes the top level certificate, and higher value denote subcertificates. |
| SCC_GetCertificateChainData | Gets the ID and the number of sub certificates of a certificate chain. |
| SCC_GetDHPublicKey | Gets the Diffie-Hellman parameter (DHPublicKey or DHParams). |
| SCC_GetEnergyTransferType | Gets the energy transfer type (DIN 70121) resp. -mode (ISO 15118) from various messages. |
| SCC_GetFaultNotification | Returns the fault code and fault message (optional) of the V2G message header. |
| SCC_GetGenChallenge | Gets the challenge string. |
| SCC_GetHeaderData | Returns the SDP or V2G message header (to the output buffer). |
| SCC_GetMaxCurrent | Vehicle: Gets the charge point's maximum current. Charge Point: Gets the vehicle's maximum current. |
| SCC_GetMaxPower | Vehicle: Gets the charge point's maximum power. Charge Point: Gets the vehicle's maximum power. |
| SCC_GetMaxVoltage | Vehicle: Gets the charge point's maximum voltage. Charge Point: Gets the vehicle's maximum voltage. |
| SCC_GetMessageRxTime | Returns the CANoe simulation time at the point of message receipt. |
| SCC_GetMeterInfoData | Gets data from MeterInfo. |
| SCC_GetMinCurrent | Vehicle: Gets the charge point's minimum current. Charge Point: Gets the vehicle's minimum current. |
| SCC_GetTimestamp | Gets a timestamp value from a message (e.g. DateTimeNow) |
| SCC_GetVerificationStatus | Returns the state of the received message regarding the validity of its signature (0 = invalid, 1 = valid, 2 = not verified) |
| EV Functions [▲ back] | Short Description |
| SCC_GetConsumptionCostData | Gets the start value and the number of Cost subelements of the ConsumptionCost element with the selected indices. |
| SCC_GetCostData | Gets the kind, amount and multiplier (range [-3..3]) values of the Cost element with the selected indices. |
| SCC_GetCurrentRegulationTolerance | Get current regulation tolerance of a ChargeParameterDiscoveryRes message. |
| SCC_GetEMAIDIdAttr | Gets the ID attribute of a (signable) eMAID. |
| SCC_GetEVSEIP | Gets the EVSE IP address of a SECCDiscoveryRes message. |
| SCC_GetEVSEIsolationStatus | Returns the isolations status from DC_EVSEStatus. |
| SCC_GetEVSENotification | Returns the EVSENotification and its maximum delay, if present, from the EVSE status. |
| SCC_GetEVSEPort | Gets the EVSE port of a SECCDiscoveryRes message. |
| SCC_GetEVSEStatusCode | Gets the EVSEStatusCode of a received message (DC mode). |
| SCC_GetEncryptedPrivateKey | Gets the encrypted private key of the new contract certificate. |
| SCC_GetEnergyToBeDelivered | Gets maximum phases of a ChargeParameterDiscoveryRes message. |
| SCC_GetEnergyTransferMode | Gets EnergyTransferMode with the target index (ISO 15118). |
| SCC_GetEnergyTransferModeCount | Get the number of Supported EnergyTransferModes. |
| SCC_GetMinVoltage | Gets the charge point's minimum voltage. |
| SCC_GetNominalVoltage | Gets the charge point's nominal voltage from a ChargeParameterDiscoveryRes message. |
| SCC_GetPMaxScheduleEntryCount | Get the number of entries in the PMaxSchedule. |
| SCC_GetPMaxScheduleEntryData | Get various data of a PMaxScheduleEntry. |
| SCC_GetPMaxScheduleID | Gets the ID of a PMaxSchedule (DIN 70121). |
| SCC_GetPaymentOptions | Gets the Payment options where 0=ExternalPayment, 1=Contract and 2=both |
| SCC_GetPeakCurrentRipple | Get the value of PeakCurrentRipple of a ChargeParameterDiscoveryRes message. |
| SCC_GetProcessing | Gets the processing state. |
| SCC_GetRCD | Returns the ECD flag from AC_EVSEStatus. |
| SCC_GetResponseCodeString | Gets the response code. |
| SCC_GetRetryCounter | Gets the retry counter of a CertificationUpdateRes. |
| SCC_GetSAScheduleTupleID | Gets the ID of an SAScheduleTuple entry within a ChargeParameterDiscoveryRes message. |
| SCC_GetSalesTariffData | Gets various elements of the Sales Tariff within the SAScheduleTuple with the selected index. |
| SCC_GetSalesTariffEntryCount | Gets the number of SalesTariffEntries in the SalesTariff within the SAScheduleTuple with the selected index. |
| SCC_GetSalesTariffEntryData | Gets the start time, duration, price level and the number of ConsumptionCost subelements of the SalesTariffEntry with the selected indices. |
| SCC_GetServiceData | Get various elements of a service within a ServiceDiscoveryRes message. |
| SCC_GetServiceParameterData | Gets the name and value type of the parameter with the selected indices. |
| SCC_GetServiceParameterNumericalValue | Gets the numerical value of the parameter with the selected indices. |
| SCC_GetServiceParameterPhysicalValue | Gets the physical value of the parameter with the selected indices. |
| SCC_GetServiceParameterSetData | Gets the ParameterSetID with the specified list index < ParameterSetCount. |
| SCC_GetServiceParameterStringValue | Gets the string value of the parameter with the selected indices. |
| EVSE Functions [▲ back] | Short Description |
| SCC_GetAppProtocolData | Gets the content of an AppProtocol element of a SupportedAppProtocolReq message. |
| SCC_GetBulkChargingComplete | Gets the flag BulkChargingComplete from DC_EVPowerDeliveryParameter. |
| SCC_GetBulkSOC | Gets the BulkSOC value of a ChargeParameterDiscoveryReq message. |
| SCC_GetChargingComplete | Gets the flag ChargingComplete from DC_EVPowerDerliveryParameter. |
| SCC_GetChargingProfileData | Gets the content of a Chargingprofile within a ChargeParameterDiscoveryReq message. |
| SCC_GetDC_EVStatus | Gets the elements of DC_EVStatus of a received DC message. |
| SCC_GetDepartureTime | Gets the end of charging time ChargeParameterDiscoveryReq message. |
| SCC_GetFullSOC | Gets the FullSOC value of a ChargeParameterDiscoveryReq message. |
| SCC_GetMaxEntriesSAScheduleTuple | Gets the maximum number of SAScheduleTuples of a ChargeParameterDiscoveryReq message. |
| SCC_GetNumberOfRootCertificateIDs | Gets the number of root certificates IDs transmitted in the message's ListOfRootCertificateIDs. |
| SCC_GetOEMPRovisioningCertificate | Reads the OEM provisioning certificate as base64 string. |
| SCC_GetRemainingTimeToBulkSoC | Gets the RemainingTimeToBulkSoC of a CurrentDemandReq message. |
| SCC_GetRemainingTimeToFullSoC | Gets the RemainingTimeToFullSoC of a CurrentDemandReq message. |
| SCC_GetRootCertificateID | Gets the content of the RootCertificateID element with the specified index. |
| SCC_GetSelectedParameterSetID | Gets the parameter set ID of a ServicePaymentSelectionReq message. |
| SCC_GetSelectedServiceID | Gets the service ID of a ServicePaymentSelectionReq message. |

| Shared Functions | Short Description |
|---|---|
| SCC_GetDCStatusCode | Gets the DC status code. |
| SCC_GetSessionId | Gets the session ID of the current/an existing connection. |
| EV Functions [▲ back] | Short Description |
| SCC_GetBatterySOC | Gets the vehicle's relative battery state in percent. |
| SCC_GetBatteryState | Gets the vehicle's absolute battery state in [Wh]. |
| SCC_GetEVReady | Returns the state of the EVReady flag. |
| SCC_GetRetriesLeft | Gets the number of remaining protocol retries. |
| EVSE Functions [▲ back] | Short Description |
| SCC_GetConnectionCount | Outputs the number of active SCC connections. |
| SCC_GetMessageBodyIdAttr | Gets the Id attribute of the message body. |

| Shared Functions | Short Description |
|---|---|
| SCC_GetPreparedEXIMessage | Finalizes a message without sending. |
| SCC_SLAC_SetAdditionalParameter | Sets an additional parameter after creating a message. |
| SCC_SendPreparedMessage | Sends a message created using one of the Create-functions. |
| SCC_SetOptionalParameter | Sets an optional parameter after using one of the Create-functions. |
| SCC_SetOptionalParameterFromConfig | Sets an optional parameter using the XML test configuration file. |
| SCC_SetOptionalParameterUnsigned | Sets an optional parameter after using one of the Create-functions. |
| SCC_SetPreparedMsgFaultNotification | Sets the fault code and fault message for a prepared message. |
| SCC_SetPreparedMsgHeaderData | Overwrites the SDP/V2G header for a prepared message. |

| Shared Functions | Short Description |
|---|---|
| SCC_GetSimulationState | Checks if the simulation is running, paused or stopped. |
| SCC_LoadCommunicationConfig | Loads global connection parameters from the specified XML configuration. |
| SCC_LoadV2GConfig | Loads V2G message parameters from the specified connection. Requires a running V2G session. |
| SCC_SetMessageDelay | Sets the artificial delay for Tx messages. |
| SCC_SetSchema | Sets the preferred schema for protocol handshake and/or free sending of messages. Overrides the schema definition from the XML file. |
| SCC_SetTLSEnabled | Specifies if TLS is used. |
| SCC_SimulationReset | Stops the simulation and resets the nodelayer DLL to its initial. |
| SCC_SimulationResume | Resume the nodelayer DLL when in pause mode. |
| SCC_SimulationWait | Pauses the nodelayer DLL. the SCC protocol instances will be halted, but test functions will still be available. |
| SCC_StartPassive | Activates the nodelayer DLL as passive. |
| SCC_StartSimulation | Activates the nodelayer DLL. If called for the vehicle, the vehicle will start sending messages. |
| SCC_StopSimulation | Deactivates the nodelayer DLL. |
| SCC_SuspendTx | Drops the next numberOfMessages Tx messages. |
| EV Functions [▲ back] | Short Description |
| SCC_SetChargeLoopInterval | Sets the interval between charge loop request messages. |

| Shared Functions | Short Description |
|---|---|
| SCC_SetDCStatusCode | Sets the DC status. |
| SCC_SetFaultNotification | Sets the fault code and fault message for the next V2G message header. |
| SCC_SetMaxCurrent | Sets the maximum current limit. |
| SCC_SetMaxPower | Sets the maximum power limit. |
| SCC_SetMaxVoltage | Sets the maximum voltage limit. |
| SCC_SetMinCurrent | Sets the minimum current limit. |
| EV Functions [▲ back] | Short Description |
| SCC_SetBatterySoC | Sets the vehicle's relative battery state in percent. |
| SCC_SetBatteryState | Sets the vehicle's absolute battery state in [Wh] |
| SCC_SetCabinConditioning | Sets the flag CabinConditioning (DIN) |
| SCC_SetEVReady | Sets the flag EVReady. |
| SCC_SetRESSConditioning | Sets the flag RESSConditioning (DIN) |
| SCC_SetTargetCurrent | Sets the desired current |
| SCC_SetTargetVoltage | Sets the desired voltage. |
| EVSE Functions [▲ back] | Short Description |
| SCC_ResetDCStatusCode | Sets the DC status to its (protocol version dependent) default value. |
| SCC_SetCurrentRegulationTolerance | Sets lower limits and other electrical values for the message ChargeParameterDiscoveryRes. |
| SCC_SetEVSENotification | Sets the EVSE notification enum. |
| SCC_SetEnergyToBeDelivered | Sets the energy to be delivered. |
| SCC_SetGenChallenge | Sets the challengevalue (16 byte) for the PaymentDetails Response. |
| SCC_SetIsolationStatus | Sets the isolation status. |
| SCC_SetMeterReading | Sets the current meter reading. |
| SCC_SetMinVoltage | Sets the minimum voltage limit. |
| SCC_SetNominalVoltage | Sets the nominal voltage (AC). |
| SCC_SetNotificationMaxDelay | Sets the maximal delay for the notification. |
| SCC_SetPeakCurrentRipple | Sets the peak-to-peak magnitude of the current ripple. |
| SCC_SetPresentCurrent | Sets the present current output. |
| SCC_SetPresentVoltage | Sets the present voltage output. |
| SCC_SetProcessing | Sets the processing state. |
| SCC_SetRCD | Sets the flag RCD. |
| SCC_SetReceiptRequired | Sets the ReceiptRequired flag. |
| SCC_SetResponseCode | Sets the response code for the next SCC message. |
| SCC_SetSelectedSchema | Sets the ID of the schema to be selected in the SupportedAppProtocolRes message. |
| SCC_SetSessionId | Sets the new Session ID during the callback SCC_SessionSetupReq. |
| SCC_SetShutdownRequest | Communicates shutdown of the charging procedure to the vehicle. |

| Shared Functions | Short Description |
|---|---|
| SCC_SetEnergyTransferType | Sets the desired (EV) or offered (EVSE) energy transfer type (DIN 70121) resp. -mode (ISO 15118) |
| EV Functions | Short Description |
| SCC_SetPaymentOption | Sets the desired payment option. |
| SCC_SetSelectedScheduleTableEntry | Selects an entry from the schedule table. |
| SCC_SetSelectedService | Selects an entry from the service list. |
| SCC_SetServiceDetailRequest | Schedules a service details request message. |
| SCC_SetWeldingDetectionCount | Sets the number of WeldingDetection requests for the next welding detection phase. |
| SCC_Shutdown | Initiates shutdown of the charging procedure. |
| SCC_StartCertificateInstallation | Sends a CertificateInstallationReq message during the next protocol run, if possible. |
| SCC_StartCertificateUpdate | Sends a CertificateUpdateReq message during the next protocol run, if possible. |
| SCC_StartRenegotiation | Starts a renegotiation procedure. |
| EVSE Functions [▲ back] | Short Description |
| SCC_SetContractPaymentAllowed | Enables or disables the payment option Contract. |
| SCC_SetExternalPaymentAllowed | Enables or disables the payment option ExternalPayment. |
| SCC_StopSession | Aborts the current/ a charging session, optionally closing of the TCP connection. |

| Shared Functions | Short Description |
|---|---|
| SCC_SLAC_GenerateNID | Generates a matching NID to a given NMK, using the specified algorithm. |
| SCC_SLAC_GetLinkStatus | Gets the stored link status of the simulation module. |
| SCC_SLAC_SetLinkStatus | Overwrites the stored link status of the simulation module. |
| SCC_SLAC_SetLinkStatusPollingInterval | Sets the polling interval in ms (0 = off). |
| SCC_SLAC_SetLinkStatusPollingType | Sets the polling type, where 0 = All, 1 = PILnkStatus and 2 = NwInfo. |
| SCC_SLAC_SetPSD | Sets the power spectral density for Amplitude Map Exchange. |
| EVSE Functions [▲ back] | Short Description |
| SCC_SLAC_GenerateApplyKey | Generates a new NMK and NID pair and sends it to the chip. |
| SCC_SLAC_GetKeyData | Gets the currently stored NID and NMK values. |
| SCC_SLAC_SetAttenuation | Sets the Attenuation mean and standard deviation for simulated measurements. |
| SCC_SLAC_SetAttenuationRx | Sets the attenuation of the Rx path which is subtracted from the AAG values. |
| SCC_SLAC_SetChipPresent | Enables or disables the simulation of attenuation data. Disabled when real GCA7000 is present. |
| SCC_SLAC_SetToggleNum | Sets the number of toggles for the validation message. |

| Shared Functions | Short Description |
|---|---|
| SCC_SLAC_GetApplicationType | Gets the application Type. |
| SCC_SLAC_GetCMSetKeyCnfData | Returns the additional fields of a CM_SetKey.Cnf message. |
| SCC_SLAC_GetDestinationAddress | Returns the destination MAC address of the received message (might differ from local address). |
| SCC_SLAC_GetEthPacketLength | Returns the Ethernet packet of a received MME frame. |
| SCC_SLAC_GetMVFLength | Gets the length of the match variable field. |
| SCC_SLAC_GetPEVAndEVSEId | Gets the EV and EVSE IDs. |
| SCC_SLAC_GetReservedField | Returns the content of reserved fields in the message. |
| SCC_SLAC_GetRespType | Gets the response type. |
| SCC_SLAC_GetResponseId | Gets the response ID. |
| SCC_SLAC_GetSecurityType | Gets the security type. |
| SCC_SLAC_GetSignalType | Gets the signal type. |
| SCC_SLAC_GetSourceId | Gets the source ID. |
| EV Functions [▲ back] | Short Description |
| SCC_SLAC_GetAttenResults | Queries the attenuation results during SLACFinishedInd. |
| SCC_SLAC_GetMSoundTarget | Queries the target MAC Address for the M-Sounds. |
| EVSE Functions [▲ back] | Short Description |
| SCC_SLAC_GetRandomValue | Gets the random value transmitted with CM_MNBC_Sound.Ind. |
| SCC_SLAC_GetResult | Gets the result code. |

| Version 15© Vector Informatik GmbH |
|---|
