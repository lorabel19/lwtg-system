from django.db import models

class BeltLevel(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    order_rank = models.IntegerField(unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'belt_levels'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('student', 'Student'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    profile_photo = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.full_name


class StudentProfile(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    belt_level = models.ForeignKey(BeltLevel, on_delete=models.SET_DEFAULT, default=1)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        db_table = 'student_profiles'

    def __str__(self):
        return self.user.full_name