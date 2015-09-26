# Dashboard

Dashboard is a front-end Admin Control Panel for Restaurant managers, Gobbl staff.

Built with Python (Flask framework).

<p align="center">
  <img src="screenshots/benri_logo.png">
</p>


## Prerequisites

Dashboard connects with the Authentication Service (Bouncer) as well as the backend API Service (Snakebite).

You would therefore be required to have Bouncer and Snakebite running in your local environment.


## Instructions

First, clone this repository onto your local machine

```
$ git clone https://github.com/gobbl/dashboard.git
$ cd dashboard
```

We first need to install all the dependencies or packages needed (a virtualenv is recommended).

```
$ pip install -r requirements.txt
```

## Up and Running

```
$ python runserver.py
```

Point your browser to localhost:5000/auth/login, and sign in as usual (assuming you have Bouncer and MongoDB running).

## Testing & Contributing

Before pushing codes, please ensure that the code is checked against flake8 firstly
