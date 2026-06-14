# Example for Automatic Variant Identification

> Category: `Diagnostics` | Type: `notes`

## Description

This test case checks if the identified variant matches the configured one.

// This test case checks if the variant found by the identification// algorithm is the configured one

testcase IdentifyConfiguredVariant(){ char configuredVariant[50]; char identifiedVariant[50]; long status; // Retrieve the qualifier of the configured variant diagGetConfiguredVariant("ECU", configuredVariant, elcount( configuredVariant)); TestStep( "Expected:", configuredVariant); // Start variant identification status = diagStartVariantIdentification("ECU"); if( 0 == status) { TestStepPass( "Variant Identification was started!"); } else if( status == -97) { TestStepFail( "Variant identification not defined in diagnostic description"); } else { TestStepFail( "Variant identification could not be started"); } // Wait explicitly status = TestWaitForDiagVariantIdentificationCompleted( configuredVariant); // Evaluate the result switch( status) { case 1: TestStepPass( "Configured variant identified."); break; case 0: TestStepFail( "Variant identification ran into timeout!"); break; case -100: TestStepFail( "Variant identification not running!"); break; case -98: TestStepFail( "Variant identification algorithm not successful!"); break; case -90: TestStepFail( "TestWaitFor... functions are only possible in tester modules!"); break; case -83: diagGetIdentifiedVariant( "ECU", identifiedVariant, elcount(identifiedVariant)); TestStep( "Found:", identifiedVariant); TestStepFail( "Identified variant is not the expected one!"); break; default: TestStepFail( "Variant identification failed!"); break; }}
