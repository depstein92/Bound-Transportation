# Bound-Transportation Backend

## Setup

1. Clone the repo
1. run: `cd Bound-Transportation/backend`
1. run: `pipenv shell`
1. run: `pip install -r requirements.txt`
1. run: `python main.py`


## DB

Currently using sqlite. 

If error on write, confirm that all db tables are up to date. 

To do so, stop the app; run: `rm -rf bt.db`; then restart the app to recreate db.

To inspect the contents of the local db, run:
`cd Bound-Transportation/backend`

`sqlite3`

`.open bt.db`

`.dump`

## s3 Image Uploads (Update User)

The application currently accepts a POST request containing a file, which it then reads in memory and writes to the s3 bucket, gets a url for said upload, and writes url to `User` model in `bt.db`.

### AWS Creds

Create hidden dir called `.aws` in home dir. 

Within `.aws/credentials`, add the following:

```
[default]
aws_access_key_id = <your aws access key id>
aws_secret_access_key = <your aws secret access key>
```

Within `.aws/config`, add the following:

```
[default]
region = <your preferred region code> Ex: us-west-2
```