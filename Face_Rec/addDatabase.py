import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-a92d4-default-rtdb.firebaseio.com/"
})

ref = db.reference('Student')

data = {
    "22210004": {
        "Name": "Akshata Vibhute",
        "Rollno": "401",
        "Batch": "D1",
        "PRN No": "22210004"
    },
    "22210026": {
        "Name": "Aditya Patil",
        "Rollno": "403",
        "Batch": "D1",
        "PRN No": "22210026"
    },
    "22210053": {
        "Name": "Shubham Mahalle",
        "Rollno": "404",
        "Batch": "D1",
        "PRN No": "22210053"
    },
    "22210069": {
        "Name": "Ankita Ugale",
        "Rollno": "405",
        "Batch": "D1",
        "PRN No": "22210069"
    },
    "22210085": {
        "Name": "Gyanesh Choudhary",
        "Rollno": "406",
        "Batch": "D1",
        "PRN No": "22210085"
    },
    "22210101": {
        "Name": "Prathmesh Gumal",
        "Rollno": "407",
        "Batch": "D1",
        "PRN No": "22210101"
    },
    "22210117": {
        "Name": "Sanket Nabade",
        "Rollno": "408",
        "Batch": "D1",
        "PRN No": "22210117"
    },
    "22210133": {
        "Name": "Ashish Kumar Yadav",
        "Rollno": "409",
        "Batch": "D1",
        "PRN No": "22210133"
    },
    "22210134": {
        "Name": "chirag singh",
        "Rollno": "509",
        "Batch": "E1",
        "PRN No": "22210134"
    },
    "22210165": {
        "Name": "Pritam Sable",
        "Rollno": "411",
        "Batch": "D1",
        "PRN No": "22210165"
    },
    "22210197": {
        "Name": "Vivek Ranalkar",
        "Rollno": "413",
        "Batch": "D1",
        "PRN No": "22210197"
    },
    "22210229": {
        "Name": "Neha Lokhande",
        "Rollno": "415",
        "Batch": "D1",
        "PRN No": "22210229"
    },
    "22210293": {
        "Name": "Sujit Giri",
        "Rollno": "419",
        "Batch": "D1",
        "PRN No": "22210293"
    },
    "22210313": {
        "Name": "Rohit Dongre",
        "Rollno": "421",
        "Batch": "D1",
        "PRN No": "22210313"
    },
    "22210360": {
        "Name": "Parth Wange",
        "Rollno": "423",
        "Batch": "D1",
        "PRN No": "22210360"
    },
    "22210361": {
        "Name": "Rupesh Ambavane",
        "Rollno": "424",
        "Batch": "D1",
        "PRN No": "22210361"
    },
    "22210389": {
        "Name": "Akash Gangurde",
        "Rollno": "425",
        "Batch": "D1",
        "PRN No": "22210389"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
