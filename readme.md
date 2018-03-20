**PharmEasy Assignment https://pharmeasyapp.herokuapp.com**
 - 3 types of Roles Patient, Doctor and Pharmacist.
 - Patient’s data can be shared only if they approve it.
 - Doctor and Pharmacist can ask for Permission to view Patient's prescription.

----------

**To Run on Local Machine**

Python 3 Used
 - Create a Virtual environment and install the dependencies `pip3 install -r requirements.txt`
 - Migrate `python3 manage.py migrate`
 - Run Server `python3 manage.py runserver`

----------
**Existing Users:-**
Username and Password Respectively
 - patient1 : patient1
 - patient2 : patient2
 -  patient3 : patient3
 -  patient4 : patient4
 - patient5 : patient5
 - doctor1 : doctor1
 - doctor2 : doctor2
 - doctor3 : doctor3
 -  doctor4 : doctor4
 - pharmacist1 : pharmacist1
 - pharmacist2 : pharmacist2
 - pharmacist3 : pharmacist3
 - coolkps : Qwerty123 (admin)
Few sample Prescriptions are also corresponding various patients for illustration purpose.
****
**Main Features**
 - Custom User model used for User profile
 - Custom User SignUp view
 -  Doctor/Pharmacist can ask for Patient's approval to view patient's prescription
 - Patient can approve request of Doctor/Pharmacist
****
**ShortComings/Limitations**
 - For the sake of simplicity, content of Prescriptions and Medical Records are considered simple String.
 - Prescriptions can currently only be added through admin
 - Medical records can currently only be added through admin
 - Doctors/Pharmacists can see user's prescription if accessed directly (through url), using `django-guardian` to fix this issue. Other Suggestions are welcome.