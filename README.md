# **HaaS**

Hashmaps as a service. We've implemented our own (fixed-size) hashmap in Python - but we're taking it a step further. You can now take advantage of our groundbreaking, state of the art data structure on YOUR applications, with our easy to use API. 

## Setup

1. Use `git clone https://github.com/vwsong/HaaS.git` to clone the repo.
2. Make sure you have Python and Flask installed - `pip install Flask`
3. Run `$ FLASK_APP=main.py flask run` in your terminal to start the server!

## API Documentation

* **URL:** \create

  **Method:** POST
  
  **DATA PARAMS:** 
	
  ``` 
  BODY = {
  	"id": "unique_id_of_new_hashmap",
    "size": "fixed_size_of_hashmap_as_integer"
  }
  ```
  
  i.e.
  ``` 
  BODY = {
  	"id": "12",
    "size": "200"
  }
  ```
  **Error Responses:**
	```
	 {
		"Code" : 400
        "Message": "Database `id` already set!"
     }
     ```
     ```
	 {
		"Code" : 400
        "Message": "Failure - hashmap is full."
     }
     ```

  **Success Responses:**
	```
	 {
		"Code" : 200
        "Message": "Success - data set!	"
     }
     ```
* **URL:** \set

  **Method:** POST
  
  **DATA PARAMS:** 
	
  ``` 
  BODY = {
  	"id": "unique_id_of_new_hashmap",
    "key": "key",
    "value": "value"
  }
  ```
  
  i.e.
  ``` 
  BODY = {
  	"id": "12",
    "key": "vincent",
    "value": "song"
  }
  ```
  **Error Responses:**
	```
	 {
		"Code" : 400
        "Message": "Database `id` doesn't exist!"
     }
     ```

  **Success Responses:**
	```
	 {
		"Code" : 200
        "Message": "Success - data set!	"
     }
     ```
* **URL:** \get

  **Method:** GET
  
  **URL PARAMS:** 
	
  ``` 
  id="unique_id_of_new_hashmap"
  key="key"
  ```
  
  i.e.
  ``` 
  id="12"
  key="vincent"
  ```
  **Error Responses:**
	```
	 {
		"Code" : 400
        "Message": "Database `id` doesn't exist!"
     }
     ```

  **Success Responses:**
	```
	 {
		"Code" : "200",
		"Value" : value
	 }
     ```
* **URL:** /load

  **Method:** GET
  
  **URL PARAMS:** 
	
  ``` 
  id="unique_id_of_hashmap"
  ```
  
  i.e.
  ``` 
  id="12"
  ```
  **Error Responses:**
	```
	 {
		"Code" : 400
        "Message": "Database `id` doesn't exist!"
     }
     ```

  **Success Responses:**
	```
	 {
		"Code" : "200",
		"Value" : value
	 }
     ```
* **URL:** \delete

  **Method:** POST
  
  **DATA PARAMS:** 
	
  ``` 
  BODY = {
  	"id": "unique_id_of_new_hashmap",
    "key": "key"
  }
  ```
  
  i.e.
  ``` 
  BODY = {
  	"id": "12",
    "key": "vincent"
  }
  ```
  **Error Responses:**
	```
	 {
		"Code" : 400
        "Message": "Invalid parameters."
     }
     ```
     ```
	 {
		"Code" : 400
        "Message": "Key doesn't exist."
     }
     ```

  **Success Responses:**
	```
	 {
		"Code" : 200
        "value": "song"
     }
     ```
