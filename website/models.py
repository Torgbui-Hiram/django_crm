from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from member.models import CustomUser

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default='')
    user_mail = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, )
    details = models.CharField(
        max_length=500, blank=True, null=True, default='')
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.status}'


class Departments(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default='')
    duties = models.CharField(
        max_length=500, blank=True, null=True, default='')

    def __str__(self):
        return self.name


class Managers(models.Model):
    all_titles = [('MR', 'Mr'), ('MAD', 'MADAM'), ('MSS', 'Miss')]
    title = models.CharField(choices=all_titles, default=1, max_length=10)
    first_name = models.CharField(
        max_length=50, blank=True, null=True, default='')
    last_name = models.CharField(
        max_length=50, blank=True, null=True, default='')
    department = models.ForeignKey(
        Departments, on_delete=models.CASCADE, default='', blank=True, null=True)
    position = models.CharField(
        max_length=50, blank=True, null=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


class Products(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default='')
    details = models.CharField(
        max_length=500, blank=True, null=True, default='')
    price = models.DecimalField(
        max_digits=5, decimal_places=2, default='', null=True, blank=True)
    authorise_by = models.ForeignKey(Managers, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name='followed_by', symmetrical=False, blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)


