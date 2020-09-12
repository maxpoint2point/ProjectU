from django.db import models

class OU(models.Model):
    """Организации"""
    name = models.CharField('Имя', max_length=70)
    inn = models.CharField('ИНН', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class WorkPlaces(models.Model):
    """Рабочие места"""
    name = models.CharField('Имя', max_length=70)
    fsrarID = models.CharField('ФСРАР ИД', max_length=12)
    UtmIPAddress = models.GenericIPAddressField('Адрес УТМ', )
    UtmPort = models.PositiveIntegerField('Порт УТМ', )
    DeleteRequests = models.BooleanField()
    LoadTTN = models.BooleanField()
    disabled = models.BooleanField()
    ouID = models.ForeignKey(OU, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

class UTMRequestsIN(models.Model):
    """Входящие документы УТМ"""

    WAYBILL = 'WayBill_v3'
    TTNHISTORYF2REG = 'TTNHISTORYF2REG'
    FORM2REGINFO = 'FORM2REGINFO'
    RESTS = 'ReplyRests'
    RESTS_SHOP = 'ReplyRestsShop_v2'
    NATTN = 'ReplyNATTN'
    TICKET = 'Ticket'

    TYPE_DOC = (
        (WAYBILL, 'Накладная'),
        (TTNHISTORYF2REG, 'История накладных'),
        (FORM2REGINFO, 'История справок по форме 2'),
        (RESTS, 'Остатки 1 регистра'),
        (RESTS_SHOP, 'Остатки 2 регистра'),
        (NATTN, 'Список неподтвержденных накладных'),
        (TICKET, 'Тикет'),
    )

    replyID = models.CharField(max_length=40)
    type = models.CharField(max_length=20, choices=TYPE_DOC)
    timestamp = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=100)
    used = models.BooleanField(default=False)
    workplaceID = models.ForeignKey(WorkPlaces, on_delete=models.CASCADE)

    def __str__(self):
        return self.type + ' ('+self.replyId+')'

    class Meta:
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящие документы'

    class UTMRequestsOUT(models.Model):
        """Исходящие документы УТМ"""

        WAYBILL = 'WayBill_v3'
        TTNHISTORYF2REG = 'TTNHISTORYF2REG'
        FORM2REGINFO = 'FORM2REGINFO'
        RESTS = 'ReplyRests'
        RESTS_SHOP = 'ReplyRestsShop_v2'
        NATTN = 'ReplyNATTN'
        TICKET = 'Ticket'

        TYPE_DOC = (
            (WAYBILL, 'Накладная'),
            (TTNHISTORYF2REG, 'История накладных'),
            (FORM2REGINFO, 'История справок по форме 2'),
            (RESTS, 'Остатки 1 регистра'),
            (RESTS_SHOP, 'Остатки 2 регистра'),
            (NATTN, 'Список неподтвержденных накладных'),
            (TICKET, 'Тикет'),
        )

        replyID = models.CharField(max_length=40)
        type = models.CharField(max_length=20, choices=TYPE_DOC)
        timestamp = models.DateTimeField(auto_now_add=True)
        used = models.BooleanField(default=False)
        workplaceID = models.ForeignKey(WorkPlaces, on_delete=models.CASCADE)

        def __str__(self):
            return self.type + ' (' + self.replyId + ')'

        class Meta:
            verbose_name = 'Исходящий документ'
            verbose_name_plural = 'Исходящие документы'

class Producer(models.Model):
    """Контрагенты"""
    ProducerClientRegId = models.CharField('ФСРАР ИД', max_length=12)
    ProducerINN = models.CharField('ИНН', max_length=12)
    ProducerKPP = models.CharField('КПП', max_length=12)
    ProducerFullName = models.CharField('Полное наименование', max_length=200)
    ProducerShortName = models.CharField('Сокращенное наименование', max_length=100)
    addressCountry = models.PositiveIntegerField()
    addressRegionCode = models.PositiveIntegerField()
    addressdescription = models.CharField('Адрес', max_length=200)

    def __str__(self):
        return self.ProducerShortName + ' (' + self.ProducerClientRegId + ')'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

class AlcoholVCode(models.Model):
    """Виды алкогольной продукции"""
    vcode = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Alcohol(models.Model):
    """Алкогольная продукция"""
    ProductFullName = models.CharField('Полное наименование', max_length=200)
    ProductAlcCode = models.CharField('Алкокод', max_length=200, unique=True)
    ProductCapacity = models.FloatField('Объем')
    ProductAlcVolume = models.FloatField('Крепость')
    ProductVCodeID = models.ForeignKey(AlcoholVCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductFullName

    class Meta:
        verbose_name = 'Алкогольная продукция'
        verbose_name_plural = 'Алкогольная продукция'

class FA(models.Model):
    """Справки по форме А"""
    regID = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.regID

    class Meta:
        verbose_name = 'Справка по форме А'
        verbose_name_plural = 'Справки по форме А'

class FB(models.Model):
    """Справки по форме B"""
    regID = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.regID

    class Meta:
        verbose_name = 'Справка по форме Б'
        verbose_name_plural = 'Справки по форме Б'

class RestsList(models.Model):
    """Список документов с остатками"""

    LOADED = 'loaded'
    SEND_AC = 'send_ac'
    ERROR = 'error'

    STATUS_CHOICES = (
        (LOADED, 'Загружены'),
        (SEND_AC, 'Передан в УТМ'),
        (ERROR, 'Ошибка'),
    )

    requestID = models.ForeignKey(UTMRequestsIN, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default=LOADED)

    def __str__(self):
        return self.date

    class Meta:
         verbose_name = 'Документ с остатками'
         verbose_name_plural = 'Документы с остатками'