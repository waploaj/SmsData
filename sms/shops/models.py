# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MarketInfo(models.Model):
    field_quantity = models.CharField(db_column='\tquantity', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    date = models.DateTimeField()
    item = models.ForeignKey('OsposItems', models.DO_NOTHING, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey('OsposCustomers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Market_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    last_name = models.CharField(max_length=150)
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
    action_flag = models.PositiveSmallIntegerField()
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


class Keys(models.Model):
    id = models.IntegerField()
    key = models.CharField(max_length=40)
    level = models.IntegerField()
    ignore_limits = models.IntegerField()
    is_private_key = models.IntegerField()
    ip_addresses = models.TextField(blank=True, null=True)
    date_created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keys'


class Logs(models.Model):
    id = models.IntegerField()
    uri = models.CharField(max_length=255)
    method = models.CharField(max_length=6)
    params = models.TextField(blank=True, null=True)
    api_key = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=45)
    time = models.IntegerField()
    rtime = models.FloatField(blank=True, null=True)
    authorized = models.CharField(max_length=1)
    response_code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class OsposAppConfig(models.Model):
    key = models.CharField(primary_key=True, max_length=50)
    value = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ospos_app_config'


class OsposAttendence(models.Model):
    att_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey('OsposEmployees', models.DO_NOTHING)
    customer = models.ForeignKey('OsposCustomers', models.DO_NOTHING)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ospos_attendence'


class OsposCallCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING)
    visit = models.ForeignKey('OsposVisit', models.DO_NOTHING)
    employee = models.ForeignKey('OsposPeople', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_call_card'


class OsposChannel(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    channel_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_channel'


class OsposCompHoldingStocks(models.Model):
    hold_id = models.AutoField(primary_key=True)
    comp = models.ForeignKey('OsposCompItems', models.DO_NOTHING)
    customer = models.ForeignKey('OsposCustomers', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=15, decimal_places=3)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ospos_comp_holding_stocks'


class OsposCompItems(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    customer = models.ForeignKey('OsposCustomers', models.DO_NOTHING)
    description = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    comp_id = models.AutoField(primary_key=True)
    pic_filename = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_comp_items'


class OsposCompSalesItems(models.Model):
    sale_time = models.DateTimeField()
    sale_id = models.AutoField(primary_key=True)
    comp = models.ForeignKey(OsposCompItems, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=3)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    customer = models.ForeignKey('OsposCustomers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ospos_comp_sales_items'


class OsposCustomers(models.Model):
    person_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    taxable = models.IntegerField()
    sales_tax_code = models.CharField(max_length=32)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    package_id = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    date = models.DateTimeField()
    retail = models.ForeignKey('OsposRetailType', models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(OsposChannel, models.DO_NOTHING, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey('OsposStockLocations', models.DO_NOTHING, blank=True, null=True)
    visit = models.ForeignKey('OsposVisit', models.DO_NOTHING, blank=True, null=True)
    store_bussiness_name = models.CharField(max_length=255, blank=True, null=True)
    card = models.ForeignKey(OsposCallCard, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_customers'


class OsposCustomersPackages(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255, blank=True, null=True)
    points_percent = models.FloatField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_customers_packages'


class OsposCustomersPoints(models.Model):
    person_id = models.IntegerField()
    package_id = models.IntegerField()
    sale_id = models.IntegerField()
    points_earned = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_customers_points'


class OsposDinnerTables(models.Model):
    dinner_table_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    status = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_dinner_tables'


class OsposEmployees(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    person_id = models.IntegerField()
    deleted = models.IntegerField()
    hash_version = models.IntegerField()
    language = models.CharField(max_length=48, blank=True, null=True)
    language_code = models.CharField(max_length=8, blank=True, null=True)
    token = models.CharField(max_length=255)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ospos_employees'


class OsposExpenseCategories(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    category_description = models.CharField(max_length=255)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_expense_categories'


class OsposExpenses(models.Model):
    expense_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_type = models.CharField(max_length=40)
    expense_category = models.ForeignKey(OsposExpenseCategories, models.DO_NOTHING)
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(OsposEmployees, models.DO_NOTHING)
    deleted = models.IntegerField()
    supplier_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_tax_code = models.CharField(max_length=255, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_expenses'


class OsposGiftcards(models.Model):
    record_time = models.DateTimeField()
    giftcard_id = models.AutoField(primary_key=True)
    giftcard_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    deleted = models.IntegerField()
    person_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_giftcards'


class OsposGrants(models.Model):
    permission_id = models.CharField(primary_key=True, max_length=255)
    person_id = models.IntegerField()
    menu_group = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_grants'
        unique_together = (('permission_id', 'person_id'),)


class OsposInventory(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_items = models.IntegerField()
    trans_user = models.IntegerField()
    trans_date = models.DateTimeField()
    trans_comment = models.TextField()
    trans_location = models.IntegerField()
    trans_inventory = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_inventory'


class OsposItemKitItems(models.Model):
    item_kit_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    quantity = models.DecimalField(max_digits=15, decimal_places=3)
    kit_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_item_kit_items'
        unique_together = (('item_kit_id', 'item_id', 'quantity'),)


class OsposItemKits(models.Model):
    item_kit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    item_id = models.IntegerField()
    kit_discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    price_option = models.IntegerField()
    print_option = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_item_kits'


class OsposItemQuantities(models.Model):
    item_id = models.IntegerField(primary_key=True)
    location_id = models.IntegerField()
    quantity = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_item_quantities'
        unique_together = (('item_id', 'location_id'),)


class OsposItems(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    supplier_id = models.IntegerField(blank=True, null=True)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    reorder_level = models.DecimalField(max_digits=15, decimal_places=3)
    receiving_quantity = models.DecimalField(max_digits=15, decimal_places=3)
    item_id = models.AutoField(primary_key=True)
    pic_filename = models.CharField(max_length=255, blank=True, null=True)
    allow_alt_description = models.IntegerField()
    is_serialized = models.IntegerField()
    stock_type = models.IntegerField()
    item_type = models.IntegerField()
    tax_category_id = models.IntegerField()
    deleted = models.IntegerField()
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    custom6 = models.CharField(max_length=255, blank=True, null=True)
    custom7 = models.CharField(max_length=255, blank=True, null=True)
    custom8 = models.CharField(max_length=255, blank=True, null=True)
    custom9 = models.CharField(max_length=255, blank=True, null=True)
    custom10 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_items'


class OsposItemsTaxes(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_items_taxes'
        unique_together = (('item_id', 'name', 'percent'),)


# class OsposMarketQnsComp(models.Model):
#     qns_id = models.AutoField(unique=True)
#     qns_text = models.CharField(max_length=255)
#     delete = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'ospos_market_qns_comp'


class OsposMigrations(models.Model):
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_migrations'


class OsposModules(models.Model):
    name_lang_key = models.CharField(unique=True, max_length=255)
    desc_lang_key = models.CharField(unique=True, max_length=255)
    sort = models.IntegerField()
    module_id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_modules'


class OsposPeople(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    comments = models.TextField()
    person_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ospos_people'


class OsposPermissions(models.Model):
    permission_id = models.CharField(primary_key=True, max_length=255)
    module_id = models.CharField(max_length=255)
    location_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_permissions'


# class OsposQnsSurvey(models.Model):
#     qns_id = models.AutoField(unique=True)
#     qns_text = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ospos_qns_survey'


class OsposReceivings(models.Model):
    receiving_time = models.DateTimeField()
    supplier_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    receiving_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospos_receivings'


class OsposReceivingsItems(models.Model):
    receiving_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    description = models.CharField(max_length=30, blank=True, null=True)
    serialnumber = models.CharField(max_length=30, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=3)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    item_location = models.IntegerField()
    receiving_quantity = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'ospos_receivings_items'
        unique_together = (('receiving_id', 'item_id', 'line'),)


class OsposRetailType(models.Model):
    retail_id = models.IntegerField(primary_key=True)
    retail_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_retail_type'


class OsposSales(models.Model):
    sale_time = models.DateTimeField()
    customer_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    invoice_number = models.CharField(unique=True, max_length=32, blank=True, null=True)
    quote_number = models.CharField(max_length=32, blank=True, null=True)
    sale_id = models.AutoField(primary_key=True)
    sale_status = models.IntegerField()
    dinner_table_id = models.IntegerField(blank=True, null=True)
    work_order_number = models.CharField(max_length=32, blank=True, null=True)
    sale_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales'


class OsposSalesItems(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    serialnumber = models.CharField(max_length=30, blank=True, null=True)
    line = models.IntegerField()
    quantity_purchased = models.DecimalField(max_digits=15, decimal_places=3)
    item_cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    item_unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=15, decimal_places=2)
    item_location = models.IntegerField()
    print_option = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_items'
        unique_together = (('sale_id', 'item_id', 'line'),)


class OsposSalesItemsTaxes(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    line = models.IntegerField()
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=15, decimal_places=4)
    tax_type = models.IntegerField()
    rounding_code = models.IntegerField()
    cascade_tax = models.IntegerField()
    cascade_sequence = models.IntegerField()
    item_tax_amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'ospos_sales_items_taxes'
        unique_together = (('sale_id', 'item_id', 'line', 'name', 'percent'),)


class OsposSalesPayments(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    payment_type = models.CharField(max_length=40)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ospos_sales_payments'
        unique_together = (('sale_id', 'payment_type'),)


class OsposSalesRewardPoints(models.Model):
    sale_id = models.IntegerField()
    earned = models.FloatField()
    used = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_reward_points'


class OsposSalesTaxes(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    tax_type = models.SmallIntegerField()
    tax_group = models.CharField(max_length=32)
    sale_tax_basis = models.DecimalField(max_digits=15, decimal_places=4)
    sale_tax_amount = models.DecimalField(max_digits=15, decimal_places=4)
    print_sequence = models.IntegerField()
    name = models.CharField(max_length=255)
    tax_rate = models.DecimalField(max_digits=15, decimal_places=4)
    sales_tax_code = models.CharField(max_length=32)
    rounding_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_sales_taxes'
        unique_together = (('sale_id', 'tax_type', 'tax_group'),)


class OsposSessions(models.Model):
    id = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=45)
    timestamp = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ospos_sessions'


class OsposStockLocations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_stock_locations'


class OsposSuppliers(models.Model):
    person_id = models.IntegerField()
    company_name = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    account_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_suppliers'


class OsposSurvey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(OsposCustomers, models.DO_NOTHING)
    like = models.IntegerField()
    rate = models.IntegerField()
    sugested = models.IntegerField(blank=True, null=True)
    use_again = models.IntegerField()
    item_liked = models.ForeignKey(OsposItems, models.DO_NOTHING, db_column='item_liked')
    reason_not = models.CharField(max_length=255)
    customer_comment = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ospos_survey'


class OsposTaxCategories(models.Model):
    tax_category_id = models.AutoField(primary_key=True)
    tax_category = models.CharField(max_length=32)
    tax_group_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_tax_categories'


class OsposTaxCodeRates(models.Model):
    rate_tax_code = models.CharField(primary_key=True, max_length=32)
    rate_tax_category_id = models.IntegerField()
    tax_rate = models.DecimalField(max_digits=15, decimal_places=4)
    rounding_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_tax_code_rates'
        unique_together = (('rate_tax_code', 'rate_tax_category_id'),)


class OsposTaxCodes(models.Model):
    tax_code = models.CharField(primary_key=True, max_length=32)
    tax_code_name = models.CharField(max_length=255)
    tax_code_type = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ospos_tax_codes'


class OsposVisit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    visit1 = models.CharField(max_length=255, blank=True, null=True)
    visit2 = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_visit'


class OsposWard(models.Model):
    ward_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ospos_ward'


class Ward(models.Model):
    ward_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ward'
