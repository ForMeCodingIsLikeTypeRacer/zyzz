#define RAPIDJSON_HAS_STDSTRING 1

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "AuthService.h"
#include "StringUtils.h"
#include "ClientError.h"

#include "rapidjson/document.h"
#include "rapidjson/prettywriter.h"
#include "rapidjson/istreamwrapper.h"
#include "rapidjson/stringbuffer.h"

#include <cctype>

using namespace std;
using namespace rapidjson;

AuthService::AuthService() : HttpService("/auth-tokens") {
  
}

void AuthService::post(HTTPRequest *request, HTTPResponse *response) {
	//Authenticate a new user.
	Document document;
	Document::AllocatorType& a = document.GetAllocator();
	Value o;
	
	string auth_token;
	string userID;
	string user_name;
	string pass_word;

	bool username_exists = false;
	
	User* u = new User();

	// This gets the username and password from the line. It's the words after "username=" and "password=".
	auto usenametom = request->formEncodedBody();
	user_name = usenametom.get("username");

	auto passwordtom = request->formEncodedBody();
	pass_word = passwordtom.get("password");

	// This checks that the username is all lower case, if not, it returns an error.
	for (long unsigned int i = 0; i < user_name.length(); i++)
	{
		if (islower(user_name[i]) == false)
		{
			throw ClientError::badRequest();
		}
	}

	// This makes sure the username actually exists.
	if (m_db->users.count(user_name) > 0)
	{
		username_exists = true;
	}

	// Go here if the username has not already been created.
	// This creates a user id, sets it, creates an auth token, adds the auth token to the database, and adds the username to the database
	if(username_exists == false)
	{
		u->username = user_name;
		u->password = pass_word;
		u->balance = 0;

		userID = StringUtils::createUserId();
		auth_token = StringUtils::createAuthToken();

		u->user_id = userID;
		
		
		o.SetObject();
		o.AddMember("auth_token", auth_token, a);
		o.AddMember("user_id", userID, a);

		m_db->auth_tokens.insert(pair<string, User*>(auth_token,u));
		m_db->users.insert(pair<string, User*>(user_name, u));
		
		document.Swap(o);
		StringBuffer buffer;
		PrettyWriter<StringBuffer> writer(buffer);
		document.Accept(writer);

		response->setStatus(201);
		response->setContentType("application/json");
		response->setBody(buffer.GetString() + string("\n"));
	}
	// Go here if the username already exists.
	// This throws an error if password does not match, creats an auth token, adds the auth token and username to the database. 
	else if(username_exists == true)
	{
		u = m_db->users[user_name];
		
		
		if (pass_word != u->password)
		{
			throw ClientError::forbidden();
		}
		
		
		userID = u->user_id;

		auth_token = StringUtils::createAuthToken();

		o.SetObject();
		o.AddMember("auth_token", auth_token, a);
		o.AddMember("user_id", userID, a);

		m_db->auth_tokens.insert(pair<string, User*>(auth_token,u));
		//m_db->users.insert(pair<string, User*>(user_name, u));

		document.Swap(o);
		StringBuffer buffer;
		PrettyWriter<StringBuffer> writer(buffer);
		document.Accept(writer);

		response->setStatus(200);
		response->setContentType("application/json");
		response->setBody(buffer.GetString() + string("\n"));
	}
	
	
}

void AuthService::del(HTTPRequest *request, HTTPResponse *response) {
	User* tokenu = HttpService::getAuthenticatedUser(request);
	string auth_token_string = request->getPathComponents()[1];

	m_db->auth_tokens.erase(auth_token_string);


	response->setStatus(200);

	
	delete tokenu;
}
