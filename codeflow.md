Updated models by claude


User model (extend AbstractUser):
- id (UUID, PK)
- email (unique, required)
- first_name
- last_name
- is_active
- is_deleted
- created_at
- updated_at

Tag model:
- id (UUID, PK)  
- name (CharField, max_length=50)
- user (FK to User)
- created_at

Note model:
- id (UUID, PK)
- title (CharField, max_length=200)
- content (TextField)
- tags (ManyToManyField to Tag)
- user (FK to User)
- is_pinned (BooleanField, default=False)
- is_deleted (BooleanField, default=False)
- created_at
- updated_at


Auth:
POST /auth/register/
POST /auth/login/
POST /auth/logout/
POST /auth/token/refresh/

Notes:
GET    /notes/          → list all (with search + tag filter)
POST   /notes/          → create
GET    /notes/{id}/     → retrieve single
PUT    /notes/{id}/     → update
DELETE /notes/{id}/     → soft delete
PATCH  /notes/{id}/pin/ → toggle pin

Tags:
GET    /tags/           → list user's tags
POST   /tags/           → create tag
DELETE /tags/{id}/      → delete tag


-----------------------------------------------------------------------
NOTEKEEPER:

=============CODE-FLOW==========
Registration
Login with OTP
Logout
Reset password
1.Registration FLow
fields: firstname, lastname, email, password
Model : User
Validate(for validation) and create(for saving data in models )
Validate ==> use attrs==>password and confirm password if same then save that user
create Users(**data)
obj.save()

2.Login Flow :
in viewset you just need to provide data to serializer and it will do  all the things.
serailizer flow :
validate==> email, password, otp then validate and raise exception
check if email is already exist
check if password correct or not
otp and then get token from Tokenobtain pair serializer
and save  user and update last login
delete otp and return data