## MVP Web App on AIOHttp

Application where you can store and manage virtual devices.

### Prerequisites:
   - python3.10+
   - docker, docker compose



### Install and Run:

    pip install -r requirements.txt
    
> run commands below from app root folder

    docker compose up -d 
> "docker compose up -d" build and run postgresql container on localhost:5432
> it's required to run application and perform CRUD operations
    
    python src/main.py
    
> run application on localhost:8080
    
### API Endpoints:

#### Users:

* **/users** (GET, POST: retrieve or create user)
* **/users/{id}** (GET, PUT, DELETE: perform specific request on user)

#### Devices:

* **/devices** (GET, POST: retrieve or create device)
* **/devices/{id}/** (GET, PUT, DELETE: perform specific request on device)

#### Locations:

* **/locations** (GET, POST: retrieve or create location)
* **/locations/{id}/** (DELETE: perform specific request on location)

#### TODO:
- [ ] Extract sensitive variables from code base (db connections, credentials and so on)
- [ ] Create test code base
- [ ] Manage containerization for independent running
- [ ] Implement full logging
- [ ] Manage service transactions. Implement UnitOfWork
- [ ] Implement authentication
- [ ] Implement password hashing (encoding, decoding). Will use bcrypt
- [ ] Implement robust exception handling and processing


