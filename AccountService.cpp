#define RAPIDJSON_HAS_STDSTRING 1

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "AccountService.h"
#include "ClientError.h"

#include "rapidjson/document.h"
#include "rapidjson/prettywriter.h"
#include "rapidjson/istreamwrapper.h"
#include "rapidjson/stringbuffer.h"

using namespace std;
using namespace rapidjson;

AccountService::AccountService() : HttpService("/users") {
  
}

void AccountService::get(HTTPRequest *request, HTTPResponse *response) {

}

void AccountService::put(HTTPRequest *request, HTTPResponse *response) {
	Document document;
	Document::AllocatorType& a = document.GetAllocator();
	Value o;

	// This gets an authenticated user.
	User* tokenu = HttpService::getAuthenticatedUser(request);

	string email_string;
	int balance_int = 0;

	// This gets the email from the line
	auto emailname = request->formEncodedBody();
	email_string = emailname.get("email");

	// This checks if the email is empty
	if (email_string == "")
	{
		throw ClientError::badRequest();
	}

	o.SetObject();
	o.AddMember("balance", balance_int, a);
	o.AddMember("email", email_string, a);

	document.Swap(o);
	StringBuffer buffer;
	PrettyWriter<StringBuffer> writer(buffer);
	document.Accept(writer);


	response->setStatus(200);
	response->setContentType("application/json");
	response->setBody(buffer.GetString() + string("\n"));
	delete tokenu;
}
