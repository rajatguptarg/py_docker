Beacon Management Portal
=========================
This is basic web application to manage your beacons.

Prerequisites
==========

* Python (v2.7.x)
* Virtual Environment (`virtualenv`)
* Pip


Running the portal
==========
To run this app, we prefer to use **virtualenv**. Follow these steps to run
this application:

* Create the virtual environment with following command:
```
virtualenv -p <path-to-python-2.7.x> <path-to-virtualenv>/<name-of-virtualenv>
```

* Activate the newly created virtual environment by
```
source <path-to-virtualenv>/<name-of-virtualenv>/bin/activate
```
* Inside virtual env, fire this command
```
pip install -r requirements.txt
```

* This app uses Google OAuth for authentication. To configure it, you need to have to have your `client_secrets.json` file in the `config` folder of your check out directory. For development box setup, you could download from [here](https://drive.google.com/open?id=0BxIPzUlJFkTqRTI3Nml5N0NCOEE)

* Run your app by firing command
```
python run.py config_directory=./config
```
Go to browser and open the URL: [http://localhost:9020/beacons](http://localhost:9020/beacons)

If you want to run from vagrant box, open the URL: [http://local.vagrant.com/beacons](http://local.vagrant.com/beacons)


How to get Advertised ID from UUID+Major+Minor
==============================================


* Let suppose here is the UUID - `B9407F30-F5F8-466E-AFF9-25556B57FE6D` which is 16 byte hex string. According to Google documentation, UUID is the namespace(10 bytes).

* So now we have to convert UUID(16 bytes) into namespace(10 bytes). For that we remove 6 bytes from middle. Now our namespace id is `B9407F3025556B57FE6D`. I removed 6 bytes from UUID `-F5F8-466E-AFF9-`. Here I removed removed from position 8 to 23 (indexing starts at 0).

* Now we have to convert Major into hex. For example Major is `65268`. Let hex representation of major is `0x6e2f`

* Similarly convert minor into hex. For example if minor is `13744`. Hex representation of minor is `0x23f2`

* Now concatenate hex representation of Major+Minor which is `6e2f23f2` in our case. Note: This is 4 bytes. We need 2 more bytes to convert into instance id.

* We add padding of 2 bytes with Major+Minor. So now instance id will be `ffff6e2f23f2` which is now 6 bytes.

* You have now 10 bytes of namespace id and 6 bytes of instance id.
      Namespace: B9407F3025556B57FE6D
      Instance: ffff6e2f23f2

* Now concatenate Namespace+Instance. So it will be like  `b9407f3025556b57fe6dffff6e2f23f2` which is 16  bytes.

* Convert above string into byte array and encode that byte array into base64 encoding.

* Now the encoded string is `uUB/MCVVa1f+bf///vQ1sA==` which is your advertised id.
