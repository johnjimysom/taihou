// ****************************************************************************
// Function: TEMPLATE
//
// Standard template for PSM JavaScript macros.
//
// Language: JScript
// Written by: Raphaël Lalonde Lefebvre - Objectif Lune
// *** This macro is provided as is, it will not be supported, and no rights can be claimed ***
// *** Use at your own risk ***
//
// INSTRUCTIONS:
//
// To install, place this .js file in "Macro" folder of the PrintShop Mail's directory. If you do not see it, create it. Once done, restart PrintShop Mail,
// and the "TEMPLATE" function will appear.
//
// Unfortunately, there is no built-in function to convert decimal to hex or hex to decimal. Pretty much the only way you could do this is through a custom javascript macro, though I don't have one that does this specifically.
// ****************************************************************************


// Function descriptor.
function psmGetFunctionDescriptor(index)
{
	// Descriptor syntax explanation:
	// The first "STRING" is the function's category under which it will appear in the Expression Editor's list of functions.
	// It does not have any impact on what the function returns, it's only used to place it in the right category. Ideally, it will
	// be the same as the function's return type.
	
	// The second "STRING" is the function's return type.

	// Some supported types are:
	// STRING: A string.
	// NUMBER: A number.
	// LOGICAL: True/False value.
	
	// "index" seems to be a PSM system variable, and should be left alone.
	
	// For the usage examples, precede the double quotes by a '\' character.
	if (index == 0) return "STRING STRING TEMPLATE(STRING{string1;First string.},STRING{string2;Second string.})\tEnter function's description here. It is followed by usage examples. \t TEMPLATE(\"Hello\", \"World\") => Hello World";

	return "";
}

// Main function.
// This is the macro's main code. It should always have "psm" as the prefix.
// If you want a TEMPLATE macro, you need to call the main function "psmTEMPLATE".
// This template's sample code takes 2 strings as parameters, and displays them
// with a CRLF between them.
function psmTEMPLATE(string1, string2)
{
	// Variables definitions.
	var mystring = "";

	// Write your code here.
	mystring = string1 + String.fromCharCode(13) + String.fromCharCode(10) + string2

	// Return final string.
	return mystring;
}

// Below are some system functions. They should not be altered unless you know what you're doing.

var Warning="";
function psmGetWarning()
{
	var result = Warning;
	Warning = "";
	return result;
}


var causeParameterNo = -1;
function psmGetWarningCauseParameter()
{
	var result = causeParameterNo;
	causeParameterNo = -1;
	return result;
}

var LanguageSet = ""; 
function psmSetLanguage(lan)
{
	LanguageSet = lan;
}
