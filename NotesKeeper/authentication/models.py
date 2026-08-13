from django.db import models
from users.models import User
import uuid


# Create your models here.


OTP_TYPE = (
    (1, 'Login'),
    (2, 'Activation'), # not in use right now
    (3, 'Reset Password'),
)

class OTP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    otp = models.CharField(max_length=6)
    otp_type = models.IntegerField(choices=OTP_TYPE)
    expired_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
