from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model thats supports using email instead of username"""
    USER_TYPE_CHOICES = (
        ('SPORTSMAN', 'Спортсмен'),
        ('TRAINER', 'Тренер'),
        ('GYM', 'Тренажерный зал')
    )
    email = models.EmailField(max_length=255, unique=True)

    date_joined = models.DateField(
        auto_now_add=True,
        verbose_name='Дата регистрации')
    city = models.CharField(max_length=255, blank=True, verbose_name='Город')
    user_type = models.CharField(
        max_length=9,
        choices=USER_TYPE_CHOICES,
        default='SPORTSMAN',
        verbose_name='Тип пользователя')

    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class Sportsman(models.Model):
    GOAL_CHOICES = (
        ('LW', 'Похудение'),
        ('MG', 'Набор мышечной массы'),
        ('MR', 'Сжигание жира(рельеф)'),
        ('PG', 'Увеличение силы'),
        ('ST', 'Выносливость'),
        ('KF', 'Поддержание формы')
    )

    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                primary_key=True, verbose_name='Аккаунт')
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        default='Sportsman')
    surname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Фамилия')
    description = models.TextField(verbose_name='О себе', blank=True)
    height = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name='Рост (см)')
    weight = models.FloatField(blank=True, verbose_name='Вес (кг)')
    age = models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст')
    photo = models.ImageField(
        upload_to='media/sportsmans/photo',
        verbose_name='Фото',
        default='media/muscules/0_i-1.jpg')
    gym = models.ForeignKey(
        'Gym',
        default=1,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='Тренажерный зал')
    goal = models.CharField(
        max_length=2,
        choices=GOAL_CHOICES,
        default='MG',
        verbose_name='Цель')
    exercises = models.ManyToManyField(
        'exercises.Exercise',
        verbose_name='Упражнения',
        blank=True)
    training_programs = models.ManyToManyField(
        'training_programs.TrainingProgram',
        verbose_name='Программы тренировок',
        related_name='sportsman_training_programs',
        blank=True)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'

    def __str__(self):
        return self.name


class Trainer(models.Model):
    SPECIALIZATION_CHOICES = (
        ('FT', 'Фитнес'),
        ('BB', 'Бодибилдинг'),
        ('WO', 'Воркаут'),
        ('CF', 'Кроссфит'),
        ('PL', 'Пауэрлифтинг'),
        ('PT', 'Лечебная физкультура'),
    )
    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                primary_key=True, verbose_name='Аккаунт')
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        default='Trainer')
    surname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Фамилия')
    description = models.TextField(verbose_name='О себе', blank=True)
    age = models.PositiveSmallIntegerField(default=20, verbose_name='Возраст')
    verification = models.BooleanField(
        default=False,
        verbose_name='Верификация')
    specialization = models.CharField(
        max_length=2,
        choices=SPECIALIZATION_CHOICES,
        default='MG',
        verbose_name='Специализация')
    gym = models.ForeignKey(
        "Gym",
        verbose_name='Тренажерный зал',
        on_delete=models.CASCADE,
        blank=True)
    clients = models.ManyToManyField(
        'Sportsman',
        verbose_name='Клиенты',
        blank=True)
    # comments =
    # raiting =

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'

    def __str__(self):
        return self.name


class Gym(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                primary_key=True, verbose_name='Аккаунт')
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        default='Gym')
    description = models.TextField(verbose_name='Описание', blank=True)
    phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Адрес')
    # coordinates =
    site = models.CharField(max_length=100, blank=True, verbose_name='Сайт')
    training_programs = models.ManyToManyField(
        'training_programs.TrainingProgram',
        verbose_name='Программы тренировок',
        related_name='gym_training_programs',
        blank=True)

    class Meta:
        verbose_name = 'Тренажерный зал'
        verbose_name_plural = 'Тренажерные залы'

    def __str__(self):
        return self.name
