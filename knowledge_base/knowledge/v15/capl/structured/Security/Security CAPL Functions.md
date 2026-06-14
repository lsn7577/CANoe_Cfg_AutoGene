# Security CAPL Functions

> Category: `Security` | Type: `notes`

## Description

Callback Handler

Low Level Crypto Functions

Secure Onboard Communication (SecOC)

Test

Test Callback Handler

Utility

X.509 Certificates

SecurityLocalGetOperationParameterKeys

Returns a list of operation parameters the Security Source supports.

Sets an operation parameter.

Returns the value of the specified operation parameter.

SecurityOfNodeGetOperationParameterKeys

Allows to register and unregister to network related security data.

| SECURITY To use the CAPL functions, the node layer SecMgrCANoeClient.dll must be included. You can include the node layer by using the configuration dialog of the node on page Components. |
|---|

| Callback Handler Low Level Crypto Functions Secure Onboard Communication (SecOC) Test | Test Callback Handler Utility X.509 Certificates |
|---|---|

| Functions | Short Description |
|---|---|
| OnSecurityLocalApplicationProtocolRxFinished | This callback handler is called the reception of an application protocol is finished. |
| OnSecurityLocalApplicationProtocolTxFinished | This callback handler is called when the transmission of an application protocol is finished. |
| OnSecurityLocalPDUPreTx | This callback handler is called, after all data updates and the automatic Authenticator (CMAC) calculation has be done. |
| OnSecurityLocalPDUValidated | This callback handler is called, when a secured PDU is received in the node. Besides to the verification result all values which have been used for verification can be analyzed. |
| OnSecurityLocalQueryFreshness | This callback handler is called, when a node a secured PDU receives and when a secured PDU is transmitted. |

| Functions | Short Description |
|---|---|
| SecurityLocalDecryptAES128CBC | Decrypts ciphered data with a given key and initialization vector using AES128 (CBC), Padding Mode PKCS5. |
| SecurityLocalDecryptAES128CTR | Decrypts ciphered data with a given key and initialization vector using AES128 (CTR). |
| SecurityLocalDecryptAES128ECB | Decrypts ciphered data with a given key using AES128 (ECB), Padding Mode PKCS5. |
| SecurityLocalDecryptAES256CBC | Decrypts ciphered data with a given key and initialization vector using AES256 (CBC). |
| SecurityLocalEncryptAES128CBC | Encrypts data with a given key and initialization vector using AES128 (CBC), Padding Mode PKCS5. |
| SecurityLocalEncryptAES128CTR | Encrypts data with a given key and initialization vector using AES128 (CTR). |
| SecurityLocalEncryptAES128ECB | Encrypts data with a given key using AES128 (ECB), Padding Mode PKCS5. |
| SecurityLocalEncryptAES256CBC | Encrypts data with a given key and initialization vector using AES256 (CBC). |
| SecurityLocalGenerateCMAC | Generates a hash for the given data and key. The generated Hash is a CMAC. |
| SecurityLocalGenerateSHA256 | Generates a SHA256 hash for the given data and key. |
| SecurityLocalGenerateSHA512 | Generates a SHA512 hash for the given data and key. |
| SecurityLocalGenerateSharedSecretECDH | Generates a Shared Secret using the Elliptic Curve Diffie-Hellman (ECDH) protocol (X25519). |

| Functions | Short Description |
|---|---|
| SecurityLocalActivateRxPDUs | Allows a node (e.g. gateway) to validate Rx Secured-I-PDUs of another node. |
| SecurityLocalActivateTxPDUs | Allows a node (e.g. gateway) to do a MAC calculation for Tx secured PDUs of another node. |
| SecurityLocalCalculateAuthenticator | Calculates the authenticator (MAC) for the given payload and freshness according to the active Security Profile on the network. |
| SecurityLocalGetFreshness | Gets the freshness value for the specified Id. |
| SecurityLocalGetOperationParameter | Returns the value of the specified operation parameter. |
| SecurityLocalGetOperationParameterKeys | Returns a list of operation parameters the Security Source supports. |
| SecurityLocalSetFreshness | Set the freshness for the specified Id. |
| SecurityLocalSetKey | Changes a key at the node. |
| SecurityLocalSetOperationParameter | Sets an operation parameter. |
| SecurityLocalTransmitApplicationProtocol | Transmits an special message of sequence of message, specifically to the active Security Profile on the network. |
| SecurityLocalVerifyAuthenticationInformation | Verifies the specified authentication information according to the active Security Profile on the network. |
| SecurityOfNodeGetOperationParameter | Returns the value of the specified operation parameter. |
| SecurityOfNodeGetOperationParameterKeys | Returns a list of operation parameters the Security Source supports. |
| SecurityOfNodeSetOperationParameter | Sets an operation parameter. |

| Functions | Short Description |
|---|---|
| SecurityOfNodeCalculateAuthenticator | Calculates the authenticator (MAC) on the specified node on the specified network for the given payload and freshness according to the active Security Profile on the network. |
| SecurityOfNodeGetFreshness | Gets the freshness value of the specified node on the specified network for the specified Id. |
| SecurityOfNodeSetFreshness | Sets the freshness value of the specified node on the specified network for the specified Id. |
| SecurityOfNodeSetKey | Changes a key at the node the specified node on the specified network. |
| SecurityOfNodeSetVerbosity | Configures the notification level for the specified node on the specified network from low (0) to high (5). |
| SecurityOfNodeTransmitApplicationProtocol | Transmits an special message of sequence of message protocol from the specified node on the specified network, specifically to the active Security Profile on the network. |
| SecurityOfNodeVerifyAuthenticationInformation | Verifies the specified authentication information of the specified node on the specified network according to the active Security Profile on the network. |
| SecurityLocalStartControlSimulationNode | Controls the specified simulation node on the specified network. |
| SecurityLocalStopControlSimulationNode | Stops controlling the specified simulation node on the specified network. |

| Functions | Short Description |
|---|---|
| OnSecurityOfNodeApplicationProtocolRxFinished | This callback handler is called the reception of an application protocol is finished. |
| OnSecurityOfNodeApplicationProtocolTxFinished | This callback handler is called when the transmission of an application protocol is finished. |
| OnSecurityOfNodePDUPreTx | This callback handler is called before the specified node on the specified network transmits a secured PDU. |
| OnSecurityOfNodePDUValidated | This callback handler is called, when the specified node on the specified network secured PDU and verified the authentication information. |
| OnSecurityOfNodeQueryFreshness | This callback handler is called, when the specified node receives or transmits a secured PDU on the specified network. It provides the possibility to influence the freshness value. |

| Functions | Short Description |
|---|---|
| SecurityLocalAllowNetworkWideRegistrations | Allows to register and unregister to network related security data. |
| SecurityLocalGetNodeLayerVersion | Get NodeLayer version. |
| SecurityLocalRegisterApplicationProtocol | Allows to register and unregister to network related security data. |
| SecurityLocalSetVerbosity | Configures the notification level for a node from low (0) to high (5). |
| SecurityLocalUnregisterApplicationProtocol | Allows to register and unregister to network related security data. |

| Functions | Short Description |
|---|---|
| GetX509ObjectFactory | Get Handle for X509 object factory. |
| Pkcs10SigningRequest_GetExtensionRequest | Get content of field Extension Request. Returns handle of Type X509Extensions. |
| Pkcs10SigningRequest_GetPublicKey | Get content of field public key. |
| Pkcs10SigningRequest_GetPublicKeyAlgIdentifier | Get content of Public Key Algorithm Identifier. Returns handle of Type X509AlgIdentifier. |
| Pkcs10SigningRequest_GetSignature | Get content of field Signature. |
| Pkcs10SigningRequest_GetSignatureAlgIdentifier | Get content of field SignatureAlgorithmIdentifier. Returns handle of Type X509AlgIdentifier. |
| Pkcs10SigningRequest_GetSubjectDN | Get content of field Subject. Returns handle of Type X509DN. |
| Pkcs10SigningRequest_GetVersion | Get content of field Version. |
| X509AlgIdentifier_GetOid | Get content of field Oid. Returns handle of Type X509Oid. |
| X509AlgIdentifier_GetParameters | Get content of field Parameters. |
| X509AlgIdentifier_SetOid | Set content of field Oid. Valid argument handle must have type X509Oid or value 0 (= NULL) to delete the field. |
| X509AlgIdentifier_SetParameters | Set content of field Parameters. |
| X509Certificate_GetAuthorityKeyIdentifier | Get content of Extension AuthorityKeyIdentifier AKID / OID 2.5.29.35. |
| X509Certificate_GetExtensions | Get content of field Extensions. Returns handle of Type X509Extensions. |
| X509Certificate_GetIssuerDN | Get content of field Issuer. Returns handle of Type X509DN. |
| X509Certificate_GetPublicKey | Get content of field Public Key. |
| X509Certificate_GetPublicKeyAlgIdentifier | Get content of field PublicKeyAlgorithmIdentifier. Returns handle of Type X509AlgIdentifier. |
| X509Certificate_GetSerialNo | Get content of field SerialNumber. |
| X509Certificate_GetSignature | Get content of field Signature. |
| X509Certificate_GetSignatureAlgIdentifier | Get content of field SignatureAlgorithmIdentifier. Returns handle of Type X509AlgIdentifier. |
| X509Certificate_GetSubjectDN | Get content of field Subject. Returns handle of Type X509DN. |
| X509Certificate_GetSubjectKeyIdentifier | Get content of Extension SubjectKeyIdentifier AKID / OID 2.5.29.14. |
| X509Certificate_GetValidFrom | Get content of field NotBefore. Returns string in format ASN.1 GeneralizedTime or UTCTime. |
| X509Certificate_GetValidTo | Get content of field NotAfter. Returns string in format ASN.1 GeneralizedTime or UTCTime. |
| X509Certificate_GetVersion | Get content of field Version. |
| X509Certificate_SetAuthorityKeyIdentifier | Set content of Extension AuthorityKeyIdentifier AKID / OID 2.5.29.35. If the extension is not present, it will be added. |
| X509Certificate_SetAuthorityKeyIdentifierFromKey | Set content of Extension AuthorityKeyIdentifier AKID / OID 2.5.29.35 to SHA1 of public key value. If the extension is not present, it will be added. |
| X509Certificate_SetExtensions | Set content of field Extensions. Valid argument handle must have type X509Extensions or value 0 (= NULL) to delete the field. |
| X509Certificate_SetIssuerDN | Set content of field Issuer. Valid argument handle must have type X509DN or value 0 (= NULL) to delete the field. |
| X509Certificate_SetPublicKey | Set content of field PublicKey. Set value 0 (= NULL) to delete the field. |
| X509Certificate_SetPublicKeyAlgIdentifier | Set content of field PublicKeyAlgorithmIdentifier. Valid argument handle must have type X509AlgIdentifier or value 0 (= NULL) to delete the field. |
| X509Certificate_SetSerialNo | Set content of field SerialNumber. Set value 0 (= NULL) to delete the field. |
| X509Certificate_SetSignature | Set content of field Signature. Set value 0 (= NULL) to delete the field. |
| X509Certificate_SetSignatureAlgIdentifier | Set content of field SignatureAlgorithmIdentifier. Valid argument handle must have type X509AlgIdentifier or value 0 (= NULL) to delete the field. |
| X509Certificate_SetSubjectDN | Set content of field Subject. Valid argument handle must have type X509DN or value 0 (= NULL) to delete the field. |
| X509Certificate_SetSubjectKeyIdentifier | Set content of Extension SubjectKeyIdentifier AKID / OID 2.5.29.14. If the extension is not present, it will be added. |
| X509Certificate_SetSubjectKeyIdentifierFromKey | Set content of Extension SubjectKeyIdentifier AKID / OID 2.5.29.14 to SHA1 of public key value. If the extension is not present, it will be added. |
| X509Certificate_SetValidFrom | Set content of field NotBefore. String is expected in format ASN.1 GeneralizedTime or UTCTime. Set value 0 (= NULL) to delete the field. |
| X509Certificate_SetValidTo | Set content of field NotAfter. String is expected in format ASN.1 GeneralizedTime or UTCTime. Set value 0 (= NULL) to delete the field. |
| X509Certificate_SetVersion | Set content of field Version. Set value 0 (= NULL) to delete the field |
| X509Certificate_ToString | Get certificate content in textual representation. |
| X509Decoder_DecodeCertificate | Decode the certificate passed as binary data from DER or PEM format. Returns Handle of type X509Certificate. |
| X509Decoder_DecodeSigningRequest | Decode the PKCS#10 Certificate Signing Request passed as binary data from DER or PEM format. Returns handle of Type Pkcs10SigningRequest. |
| X509DN_GetAttributes | Get content of field Attributes. Returns handle of Type X509Attributes. |
| X509DN_GetValueForAttribute | Look up the attribute and get content for the given OID in textual representation. OID has point notation 0.1.2.3.4.5 |
| X509DN_SetAttributes | Set content of field Attributes. Valid argument handle must have type X509Attributes or value 0 (= NULL) to delete the field. |
| X509DN_SetValueForAttribute | Look up the attribute and set the content for the given OID in textual representation. Will insert the attribute if it does not exist. OID has point notation 0.1.2.3.4.5 |
| X509DNAttribute_GetAttribute | Get content of field Attribute. Returns handle of Type X509Oid. |
| X509DNAttribute_GetValue | Get content of field Value. |
| X509DNAttribute_GetValueAsn1Tag | Get content of field ASN.1 Tag. |
| X509DNAttribute_SetAttribute | Set content of field Attribute. Valid argument handle must have type X509Oid or value 0 (= NULL) to delete the field. |
| X509DNAttribute_SetValue | Set content of field Value. Set value 0 (= NULL) to delete the field |
| X509DNAttribute_SetValueAsn1Tag | Set content of field ASN.1 Tag. Set value 0 (= NULL) to delete the field |
| X509DNAttributes_Add | Add entry for DN Attributes, field will be appended to the end of the ordered attribute list. Valid argument handle must have type X509Attribute. |
| X509DNAttributes_Erase | Erase entry for DN Attributes. Valid argument handle must have type X509Attribute. |
| X509DNAttributes_GetElement | Get an existing element from the attributes list at specific position. Will fail in case the position is not in valid range of the list. Returns handle of Type X509Attribute. |
| X509DNAttributes_InsertElement | Insert entry for DN Attributes at specific position. Will fail in case the position is not in valid range of the list. Valid argument handle must have type X509Attribute. |
| X509DNAttributes_SetElement | Update content of an existing element for DN Attributes at specific position. Will fail in case the position is not in valid range of the list. Valid argument handle must have type X509Attribute. |
| X509DNAttributes_Size | Get size of the list. |
| X509Encoder_EncodeCertificate | Encode a certificate into binary DER format. This function will encode any certificate structure, even if the content of the certificate is invalid in terms of X.509 specification (-> Error testing). Valid argument handle must have type X509Certificate. |
| X509Encoder_EncodeSigningRequest | Encode PKCS#10 Signing Request into binary DER format. This function will encode any structure, even if the content of the structure is invalid in terms of X.509 specification (-> Error testing). Valid argument handle must have type Pkcs10SigningRequest. |
| X509Encoder_EncodeTbsCertificate | Encode ToBeSigned part of certificate into binary DER format. This function will encode any certificate structure, even if the content of the certificate is invalid in terms of X.509 specification (-> Error testing). Valid argument handle must have type X509Certificate. |
| X509Encoder_EncodeTbsSigningRequest | Encode ToBeSigned part of PKCS#10 Signing Request into binary DER format. This function will encode any structure, even if the content of the structure is invalid in terms of X.509 specification (-> Error testing). Valid argument handle must have type Pkcs10SigningRequest. |
| X509Extension_GetIsCritical | Get content of field Critical. |
| X509Extension_GetOid | Get content of field Oid. Returns handle of Type X509Oid. |
| X509Extension_GetValue | Get content of field Value. |
| X509Extension_SetIsCritical | Set content of field Critical. |
| X509Extension_SetOid | Set content of field OID. Valid argument handle must have type X509Oid or value 0 (= NULL) to delete the field. |
| X509Extension_SetValue | Set value for the extension. |
| X509Extensions_Add | Add entry for Extensions, field will be appended to the end of the ordered attribute list. Valid argument handle must have type X509Extension. |
| X509Extensions_Erase | Erase entry for Extensions. Valid argument handle must have type X509Extension. |
| X509Extensions_GetElement | Get an existing element from the extensions list at specific position. Will fail in case the position is not in valid range of the list. Returns handle of Type X509Extension. |
| X509Extensions_InsertElement | Insert entry for Extension at specific position. Will fail in case the position is not in valid range of the list. Valid argument handle must have type X509Extension. |
| X509Extensions_SetElement | Update content of an existing element for Extensions at specific position. Will fail in case the position is not in valid range of the list. Valid argument handle must have type X509Extension. |
| X509Extensions_Size | Get size of the list. |
| X509ObjectFactory_BytesFromHexString | Convert string with hexadecimal representation into byte buffer. |
| X509ObjectFactory_BytesToHexString | Convert byte buffer into hexadecimal representation as string in format AABBCCDD. |
| X509ObjectFactory_copyX509AlgorithmIdentifier | Create deep copy of handle with type X509AlgIdentifier. |
| X509ObjectFactory_copyX509Certificate | Create deep copy of handle with type X509Certificate. |
| X509ObjectFactory_copyX509DN | Create deep copy of handle with type X509DN. |
| X509ObjectFactory_copyX509DNAttribute | Create deep copy of handle with type X509DNAttribute. |
| X509ObjectFactory_copyX509DNAttributes | Create deep copy of handle with type X509DNAttributes. |
| X509ObjectFactory_copyX509Extension | Create deep copy of handle with type X509Extension. |
| X509ObjectFactory_copyX509Extensions | Create deep copy of handle with type X509Extensions. |
| X509ObjectFactory_copyX509Oid | Create deep copy of handle with type X509Oid. |
| X509ObjectFactory_createPkcs10SigningRequest | Create empty handle of type Pkcs10SigningRequest. |
| X509ObjectFactory_createX509AlgorithmIdentifier | Create empty handle of type X509AlgIdentifier. |
| X509ObjectFactory_createX509Certificate | Create empty handle of type X509Certificate. |
| X509ObjectFactory_createX509CertificateFromCsr | Create new certificate handle with content copied from PKCS#10 CSR. Valid argument handle must have type Pkcs10SigningRequest. |
| X509ObjectFactory_createX509Decoder | Create handle of type X509Decoder. |
| X509ObjectFactory_createX509DN | Create empty handle of type X509DN. |
| X509ObjectFactory_createX509DNAttribute | Create empty handle of type X509DNAttribute. |
| X509ObjectFactory_createX509DNAttributes | Create empty handle of type X509DNAttributes. |
| X509ObjectFactory_createX509Encoder | Create handle of type X509Encoder. |
| X509ObjectFactory_createX509Extension | Create empty handle of type X509Extension. |
| X509ObjectFactory_createX509Extensions | Create empty handle of type X509Extensions. |
| X509ObjectFactory_createX509Oid | Create empty handle of type X509Oid. |
| X509ObjectFactory_createX509PkiAccess | Create handle of type X509PkiAccess. |
| X509ObjectFactory_createX509Verifier | Create handle of type X509Verifier. |
| X509Oid_GetOid | Get the content of the numeric OID value. |
| X509Oid_GetOidString | Get the content of the OID as string representation in point notation. |
| X509Oid_SetOid | Set the content of the numeric OID value. |
| X509Oid_SetOidFromString | Set the content of the OID from string representation in point notation. |
| X509PkiAccess_CreateSigner | Create signer handle from raw key material. The hash function will be used for algorithms that require specific hash function (e.g. ECDSA). For Algorithms with predefined Hash function (e.g. Ed25519) this will be ignored. Algorithm will be determined from certificate. Returns handle of Type X509Signer. |
| X509PkiAccess_LoadCertificateByKeyIdentifier | Load signer certificate handle in Security Profile by subject key identifier in Security Profile. Returns handle of Type X509Certificate. |
| X509PkiAccess_LoadCertificateByName | Load signer certificate handle from key material in Security Profile by name. Returns handle of Type X509Certificate. |
| X509PkiAccess_LoadSignerByKeyIdentifier | Load signer handle from key material in Security Profile by certificate subject key identifier. The hash function will be used for algorithms that require specific hash function (e.g. ECDSA). For Algorithms with predefined Hash function (e.g. Ed25519) this will be ignored. Algorithm will be determined from certificate. Returns handle of Type X509Signer. |
| X509PkiAccess_LoadSignerByName | Load signer handle from key material in Security Profile by name. The hash function will be used for algorithms that require specific hash function (e.g. ECDSA). For Algorithms with predefined Hash function (e.g. Ed25519) this will be ignored. Algorithm will be determined from certificate. Returns handle of Type X509Signer. |
| X509Signer_CreateCertificateSignature | Create signature for the certificate using the signers private key and the algorithm from signers certificate subject key algorithm. Will not update the certificate but only create the signature. Valid argument handle must have type X509Certificate. |
| X509Signer_CreateDataSignature | Create signature for the data using the signers private key and the algorithm from signers certificate subject key algorithm. |
| X509Signer_GetAuthorityKeyIdentifier | Get the AuthorityKeyIdentifier of the signer certificate (if extension is available). |
| X509Signer_GetSignatureAlgIdentifier | Get the signature algorithm identifier of the signer certificate. Returns handle of Type X509AlgIdentifier. |
| X509Signer_GetSignerCertificate | Get the signer certificate. Returns handle of Type X509Certificate. |
| X509Signer_GetSubjectKeyIdentifier | Get the SubjectKeyIdentifier of the signer certificate (if extension is available). |
| X509Signer_UpdateAndSignCertificate | Create update all relevant fields (Issuer, AuthorityKeyIdentifier, SignatureAlgorithm) in the certificate and update the signature using the signers key material. Valid argument handle must have type Pkcs10SigningRequest. |
| X509Verifier_AddTrustedCertificate | Add certificate to the verifiers trust store to be used for chain verification. Valid argument handle must have type X509Certificate. |
| X509Verifier_ClearTrustedCertificates | Clear the verifiers trust store and remove all trusted certificates. |
| X509Verifier_VerifyCertificateChain | Verify certificate chain using the stored and trusted certificates. Valid argument handle must have type X509Certificate. |
| X509Verifier_VerifyDataSignature | Verify signature of data block. Valid argument handle must have type X509Certificate. The hash function will be used for algorithms that require specific hash function (e.g. ECDSA). For Algorithms with predefined Hash function (e.g. Ed25519) this will be ignored. |
| X509Verifier_VerifySelfSignedCertificate | Verify signature of self signed certificate. Valid argument handle must have type X509Certificate. |
| X509Verifier_VerifySigningRequest | Verify signature of PKCS#10 Certificate Signing Request. Valid argument handle must have type Pkcs10SigningRequest. |

| Version 15© Vector Informatik GmbH |
|---|
