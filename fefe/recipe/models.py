# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FoodExperience(models.Model):
    year = models.CharField(db_column='YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    engn_nm = models.CharField(db_column='ENGN_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cttpc = models.CharField(db_column='CTTPC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adres = models.CharField(db_column='ADRES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rdnamdr = models.CharField(db_column='RDNAMDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nw_zip = models.CharField(db_column='NW_ZIP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    la = models.CharField(db_column='LA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lo = models.CharField(db_column='LO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_experience'


class FoodGood(models.Model):
    bssh_nma = models.CharField(db_column='BSSH_NMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telno = models.CharField(db_column='TELNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    main_menu = models.CharField(db_column='MAIN_MENU', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_good'


class FoodMasters(models.Model):
    year = models.CharField(db_column='YEAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ordr = models.CharField(db_column='ORDR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asign = models.CharField(db_column='ASIGN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nm = models.CharField(db_column='NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hold_skill = models.CharField(db_column='HOLD_SKILL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apntdt = models.CharField(db_column='APNTDT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_masters'


class FoodRecipeBasic(models.Model):
    recipe_id = models.CharField(db_column='RECIPE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recipe_nm_ko = models.CharField(db_column='RECIPE_NM_KO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sumry = models.CharField(db_column='SUMRY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nation_code = models.CharField(db_column='NATION_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nation_nm = models.CharField(db_column='NATION_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ty_code = models.CharField(db_column='TY_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ty_nm = models.CharField(db_column='TY_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cooking_time = models.CharField(db_column='COOKING_TIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    calorie = models.CharField(db_column='CALORIE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qnt = models.CharField(db_column='QNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level_nm = models.CharField(db_column='LEVEL_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_code = models.CharField(db_column='IRDNT_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pc_nm = models.CharField(db_column='PC_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_recipe_basic'

    def __str__(self):
        return "%s" % (self.recipe_nm_ko)


class FoodRecipeSource(models.Model):
    recipe_id = models.CharField(db_column='RECIPE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_sn = models.CharField(db_column='IRDNT_SN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_nm = models.CharField(db_column='IRDNT_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_cpcty = models.CharField(db_column='IRDNT_CPCTY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_ty_code = models.CharField(db_column='IRDNT_TY_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    irdnt_ty_nm = models.CharField(db_column='IRDNT_TY_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_recipe_source'

    def __str__(self):
        return "%s" % (self.irdnt_nm)


class FoodRecipeStep(models.Model):
    recipe_id = models.CharField(db_column='RECIPE_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cooking_no = models.CharField(db_column='COOKING_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cooking_dc = models.CharField(db_column='COOKING_DC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stre_step_image_url = models.CharField(db_column='STRE_STEP_IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    step_tip = models.CharField(db_column='STEP_TIP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'food_recipe_step'

    def __str__(self):
        return "%s" % (self.cooking_no)


class Info(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info'
