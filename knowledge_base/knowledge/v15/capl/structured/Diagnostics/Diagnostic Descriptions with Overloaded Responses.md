# Diagnostic Descriptions with Overloaded Responses

> Category: `Diagnostics` | Type: `notes`

## Description

ODX allows the specification of more than one positive response primitive for a diagnostic service (also for negative responses). A diagnostic client (i.e. tester) cannot know which one of the valid primitives the ECU will respond a request with. Therefore it may have to try all primitives of the service until finding one that matches the received data.

The following use cases exist:

| Version 15© Vector Informatik GmbH |
|---|
