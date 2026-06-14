# Communication Objects CAPL Functions

> Category: `CommunicationObjects` | Type: `notes`

## Description

Event Procedures

Functions

Methods

Objects

on SD_connection_established

Abstract_CreateAddress

Abstract_GetConsumerId

Abstract_GetDisplayName

Abstract_GetProviderId

Abstract_ReleaseAddress

Abstract_SubscribeEvent

Communication Concept | Programming with Communication Concept

| COMMUNICATION OBJECTS Overview of objects, event procedures, functions and methods to work with communication objects. |
|---|

| Event Procedures Functions Methods Objects |
|---|

| Event Procedures | Short Description |
|---|---|
| on Abstract_EventSubscribed | Is called when an event is subscribed at a provider. |
| on Abstract_EventUnsubscribed | Is called when an event is unsubscribed at a provider. |
| on Abstract_FieldSubscribed | Is called when a field is subscribed at a provider. |
| on Abstract_FieldUnsubscribed | Is called when a field is unsubscribed at a provider. |
| on fct_Called | Is called when a service function is called. |
| on fct_Calling | Is called when a service function is about to be called. |
| on fct_Returned | Is called when a service function answer is returned to the consumer. |
| on fct_Returning | Is called when a service function is about to return its answer. |
| on PDU_change | Is called when a PDU (of the new communication concept) is changed. |
| on PDU_Subscribed | Is called when a PDU is subscribed at a provider. |
| on PDU_Unsubscribed | Is called when a PDU is unsubscribed at a provider. |
| on PDU_update | Is called when a PDU (of the new communication concept) is updated. |
| on SD_connection_established | Is called when a connection is established. |
| on SD_connection_failed | Is called when a connection attempt fails. |
| on SD_connection_requested | Is called when a connection is requested by a consumer. |
| on SD_consumer_discovered | Is called when a new consumer is discovered. |
| on SD_provider_discovered | Is called when a new provider is discovered. |
| on SD_service_discovery | Is called when a new consumer is discovered. |
| on SOMEIP_EventGroupSubscribed | Is called when an event group is subscribed at a provider. |
| on SOMEIP_EventGroupUnsubscribed | Is called when an event group is unsubscribed at a provider. |
| on value_change | Is called when a communication object value changes. |
| on value_update | Is called when a communication object value is updated. |

| Functions | Short Description |
|---|---|
| Abstract_CreateAddress | Creates a pseudo-address for abstract binding. |
| Abstract_GetConsumerId | Gets an Id for a consumer with an abstract binding pseudo-address. |
| Abstract_GetDisplayName | Gets a display name for an endpoint with an abstract binding pseudo-address. |
| Abstract_GetProviderId | Gets an Id for a provider with an abstract binding pseudo-address. |
| Abstract_ReleaseAddress | Releases a pseudo-address for abstract binding, freeing resources. |
| Abstract_SubscribeEvent | Subscribes for a service event if abstract binding is used. |
| Abstract_SubscribeField | Subscribes for a service field if abstract binding is used. |
| Abstract_SubscribePdu | Subscribes for a service PDU if abstract binding is used. |
| Abstract_UnsubscribeEvent | Unsubscribes for a service event if abstract binding is used. |
| Abstract_UnsubscribeField | Unsubscribes for a service field if abstract binding is used. |
| Abstract_UnsubscribePdu | Unsubscribes for a service PDU if abstract binding is used. |
| GetNrOfCOConsumers | Gets the number of consumers at the communication object. |
| GetNrOfCOProviders | Gets the number of providers at the communication object. |
| GetNrOfCOReceivers | Gets the number of receivers at the communication object. |
| GetNrOfCOSenders | Gets the number of senders at the communication object. |
| LookupConsumedEvent | Searches for the specified consumed event. |
| LookupConsumedField | Searches for the specified consumed field. |
| LookupConsumedMethod | Searches for the specified consumed method. |
| LookupConsumedPDU | Searches for the specified consumed PDU. |
| LookupConsumedService | Searches for the specified consumed service. |
| LookupEventConsumer | Searches for the specified event consumer. |
| LookupEventProvider | Searches for the specified event provider. |
| LookupFieldConsumer | Searches for the specified field consumer. |
| LookupFieldProvider | Searches for the specified field provider. |
| LookupMeasuredEvent | Searches for the specified measured event. |
| LookupMeasuredField | Searches for the specified measured field. |
| LookupMeasuredMethod | Searches for the specified measured method. |
| LookupMeasuredPDU | Searches for the specified measured PDU. |
| LookupMeasuredService | Searches for the specified measured service. |
| LookupPDUConsumer | Searches for the specified PDU consumer. |
| LookupPDUProvider | Searches for the specified PDU provider. |
| LookupProvidedEvent | Searches for the specified provided event. |
| LookupProvidedField | Searches for the specified provided field. |
| LookupProvidedMethod | Searches for the specified provided method. |
| LookupProvidedPDU | Searches for the specified provided PDU. |
| LookupProvidedService | Searches for the specified provided service. |
| LookupRxPDU | Searches for the specified rx PDU. |
| LookupRxSignal | Searches for the specified rx signal. |
| LookupServiceConsumer | Searches for the specified service consumer. |
| LookupServiceProvider | Searches for the specified service provider. |
| LookupTxPDU | Searches for the specified tx PDU. |
| LookupTxSignal | Searches for the specified tx signal. |
| SD_AddConsumer | Dynamically adds a consumer endpoint to a service. |
| SD_AddProvider | Dynamically adds a provider endpoint to a service. |
| SD_AnnounceProvider | Announces that a service provider is running. |
| SD_ConnectAsync | Requests the establishment of a connection between a service provider and consumer. |
| SD_Disconnect | Disconnects a service provider and consumer. |
| SD_DiscoverProviders | Discovers all running providers of a service in the role of a consumer. |
| SD_RemoveConsumer | Dynamically removes a consumer endpoint from a service. |
| SD_RemoveProvider | Dynamically removes a provider endpoint from a service. |
| SD_SetAddress | Sets the address for a service endpoint. |
| SD_UnnnounceProvider | Announces that a service provider is no longer running. |
| SetSubscriptionStateIsolated | Sets the subscription state for a service sub-member. |
| SOMEIP_InjectPDU | Injects the PDU into the Communication Concepts SOME/IP-BindingBlock, where its then send. |
| SOMEIP_SubscribeEventGroup | Subscribes for a service event group if SOME/IP binding is used. |
| SOMEIP_UnsubscribeEventGroup | Unsubscribes for a service event group if SOME/IP binding is used. |
| TestWaitForAnswer | Waits for the answer to a method call. |
| TestWaitForChange | Waits for the next change of a communication object value. |
| TestWaitForChangeCountGreater | Waits for changes of a communication object value. |
| TestWaitForChangeFlag | Waits for the change flag of a communication object value to be set. |
| TestWaitForNextCall | Waits for the next call of the method to occur at the simulated provider. |
| TestWaitForUpdate | Waits for the next update of a communication object value. |
| TestWaitForUpdateCountGreater | Waits for update of a communication object value. |
| TestWaitForUpdateFlag | Waits for the update flag of a communication object value to be set. |
| TestWaitForValue | Waits for a (complex) communication object value to reach a certain value. |
| TestWaitForValueFloat | Waits for a communication object value to reach a certain value. |
| TestWaitForValueSInt | Waits for a communication object value to reach a certain value. |
| TestWaitForValueString | Waits for a communication object value to reach a certain value. |
| TestWaitForValueUInt | Waits for a communication object value to reach a certain value. |

| Callbacks | Short Description |
|---|---|
| callcontext::CreatePermanentHandle | Creates a permanent handle for a call context. |
| callcontext::DeferAnswer | Defers the answer for a function call indefinitely. |
| callcontext::FromHandle | Retrieves a call context from a permanent handle. |
| callcontext::ReleaseHandle | Releases a permanent handle for a call context. |
| callcontext::ReturnCall | Returns the call, sending an answer. |
| callcontext::SetDefaultAnswer | Sets return value and out parameter values to defaults. |
| callcontext::SetTimeToAnswer | Defines the time until the call shall be returned. |
| consumedEventRef::AbstractIsEventRequested | Returns whether the specified event is currently requested. |
| consumedEventRef::AbstractReleaseEvent | Releases subscription of a specific event. |
| consumedEventRef::AbstractRequestEvent | Requests subscription of a specific event. |
| consumedEventGroupRef::SOMEIPIsEventGroupRequested | Returns whether the specified event group is currently requested. |
| consumedEventGroupRef::SOMEIPReleaseEventGroup | Releases subscription of a specific event group. |
| consumedEventGroupRef::SOMEIPRequestEventGroup | Requests subscription of a specific event group. |
| consumedFieldRef::AbstractIsFieldRequested | Returns whether the specified field is currently requested. |
| consumedFieldRef::AbstractReleaseField | Releases subscription of a specific field. |
| consumedFieldRef::AbstractRequestField | Requests subscription of a specific field. |
| consumedMethodRef::CallAsync | Calls a service method. |
| consumedMethodRef::CallAsyncPhys | Calls a service method. |
| consumedPduRef::AbstractIsPduRequested | Returns whether the specified service PDU is currently requested. |
| Clear | Clears the reference. |
| consumedPduRef::AbstractReleasePdu | Releases subscription of a specific PDU. |
| consumedPduRef::AbstractRequestPdu | Requests subscription of a specific PDU. |
| consumedServiceRef::IsServiceRequested | Returns whether the service is requested. |
| consumedServiceRef::ReleaseService | Releases usage of a specific service. |
| consumedServiceRef::RequestService | Requests usage of a specific service. |
| eventProviderRef::GetNrOfSubscribedConsumers | Returns the number of currently subscribed consumers. |
| eventProviderRef::GetSubscribedConsumer | Returns a subscribed consumer. |
| eventProviderRef::Trigger | Triggers the specified event. |
| fieldProviderRef::GetNrOfSubscribedConsumers | Returns the number of currently subscribed consumers. |
| fieldProviderRef::GetSubscribedConsumer | Returns a subscribed consumer. |
| GetConsumedFieldRef | Returns the referred field. |
| GetConsumedServiceRef | Returns the referred service. |
| GetConsumer | Returns the consumer participant. |
| GetConsumerIndex | Returns the consumer index. |
| GetProvidedFieldRef | Returns the referred field. |
| GetProvidedServiceRef | Returns the referred service. |
| GetProvider | Returns the provider participant. |
| GetProviderIndex | Returns the provider index. |
| GetReceiver | Returns the receiver participant. |
| GetReceiverIndex | Returns the receiver index. |
| GetSender | Returns the sender participant. |
| GetSenderIndex | Returns the sender index. |
| pduProviderRef::GetNrOfSubscribedConsumers | Returns the number of currently subscribed consumers. |
| pduProviderRef::GetSubscribedConsumer | Returns a subscribed consumer. |
| providedEventRef::Trigger | Triggers the specified event. |
| serviceProviderRef::IsServiceProvided | Returns whether the service is provided. |
| serviceProviderRef::ProvideService | Provides the service at the endpoint. |
| serviceProviderRef::ReleaseService | Provides the service at the endpoint. |
| SetConsumer | Set the consumer endpoint. |
| SetEvent | Sets the event. |
| SetField | Sets the field. |
| SetMethod | Sets the method. |
| SetPDU | Sets the PDU/referred PDU object. |
| SetProvider | Set the provider endpoint. |
| SetReceiver | Set the receiver endpoint. |
| SetSender | Set the sender endpoint. |
| SetService | Sets the service. |
| SetSignal | Sets the referred signal object. |
| valueHandle::ClearChangeFlag | Clears the change flag of the value. |
| valueHandle::ClearUpdateFlag | Clears the update flag of the value. |
| valueHandle::GetChangeCount | Returns the change count of the value. |
| valueHandle::GetUpdateCount | Returns the update count of the value. |
| valueHandle::GetValueState | Returns the state of the value. |
| valueHandle::ResetValueState | Resets the state of the value. |

| Objects | Short Description |
|---|---|
| callContext | Contains data of a function call. |
| consumedEventRef | References a consumed event endpoint. |
| consumedFieldRef | References a consumed field endpoint. |
| consumedMethodRef | References a consumed method endpoint. |
| consumedPDURef | References a consumed PDU endpoint. |
| consumedServiceRef | References a consumed service endpoint. |
| eventConsumerRef | References an event consumer endpoint. |
| eventProviderRef | References an event provider endpoint. |
| fieldConsumerRef | References a field consumer endpoint. |
| fieldProviderRef | References a field provider endpoint. |
| measuredEventRef | References an event measurement point. |
| measuredFieldRef | References a field measurement point. |
| measuredMethodRef | References a method measurement point. |
| measuredPDURef | References a PDU measurement point. |
| measuredServicePDURef | References a service PDU measurement point. |
| measuredServiceRef | References a service measurement point. |
| pduConsumerRef | References a PDU consumer endpoint. |
| pduProviderRef | References a PDU provider endpoint. |
| providedEventRef | References a provided event endpoint. |
| providedFieldRef | References a provided field endpoint. |
| providedMethodRef | References a provided method endpoint. |
| providedPDURef | References a provided PDU endpoint. |
| providedServiceRef | References a provided service endpoint. |
| rxPDURef | References an rx PDU endpoint. |
| rxSignalRef | References an rx signal endpoint. |
| serviceConsumerRef | References a service consumer endpoint. |
| serviceProviderRef | References a service provider endpoint. |
| txPDURef | References a tx PDU endpoint. |
| txSignalRef | References a tx signal endpoint. |

| Version 15© Vector Informatik GmbH |
|---|
