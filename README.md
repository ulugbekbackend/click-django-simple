# click-django-simple

Ushbu loyiha Django + Django REST Framework yordamida yaratilgan oddiy buyurtma va Click to'lov integratsiyasi ishlaydigan backend ilovadir. Loyiha asosiy maqsadi foydalanuvchidan buyurtma olish, uni ma'lumotlar bazasiga saqlash va Click to'lov tizimi orqali to'lovni yakunlashdan iborat.

## Xususiyatlar

- Buyurtma yaratilishi (`Order` modeli)
- REST API orqali yangi buyurtma qo'shish
- `payment_method == "click"` bo'lganda avtomatik to'lov havolasi yaratish
- Click webhook orqali to'lov holatini yangilash
- SQLite bilan ishlovchi standart Django konfiguratsiyasi

## Loyiha tuzilishi

- `config/` - loyiha konfiguratsiyasi va URL manzillar
- `shop/` - buyurtma modeli, serializer, view va endpointlar
- `payment/` - Click webhook ishlovchi logika
- `manage.py` - Django management skripti
- `requirements.txt` - loyiha dependency'lari

## Ishga tushirish

1. Virtual muhit yarating:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Kutubxonalarni o'rnating:

   ```bash
   pip install -r requirements.txt
   ```

3. Loyihaning bosh root katalogida `.env` faylini yarating. Quyidagi o'zgaruvchilar kerak bo'ladi:

   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   CSRF_TRUSTED_ORIGINS=http://localhost:8000
   CLICK_SERVICE_ID=your_click_service_id
   CLICK_MERCHANT_ID=your_click_merchant_id
   CLICK_SECRET_KEY=your_click_secret_key
   ```

   > `.env` faylida shaxsiy/qo'shimcha ma'lumotlarni saqlang. Repozitordagi `.env` faylini commit qilmang.

4. Ma'lumotlar bazasini ishga tushiring:

   ```bash
   python manage.py migrate
   ```

5. Dev serverni ishga tushiring:

   ```bash
   python manage.py runserver
   ```

6. Brauzerda quyidagi URL manzilga kiring:

   - `http://127.0.0.1:8000/shop/create/`
   - `http://127.0.0.1:8000/payment/click/update/`

## API

### 1) Buyurtma yaratish

`POST /shop/create/`

Request body namunalari:

```json
{
  "customer_name": "Ali Valiyev",
  "address": "Andijon",
  "total_cost": 250000,
  "payment_method": "click",
  "is_paid": false
}
```

Agar `payment_method` qiymati `click` bo'lsa, server buyurtma yaratgandan keyin Click uchun to'lov havolasini qaytaradi.

### 2) Click webhook

`POST /payment/click/update/`

Bu endpoint Click tizimi orqali kelgan to'lov statuslarini qabul qiladi va buyurtma holatini `is_paid` bo'yicha yangilaydi.

## Muhim eslatma

- `SECRET_KEY`, `CLICK_SERVICE_ID`, `CLICK_MERCHANT_ID` va `CLICK_SECRET_KEY` qiymatlari maxfiy bo'lgani sababli, ulardan `.env` faylida foydalaning.
- Mahsulotni production muhiti uchun `DEBUG` ni `False` qilib o'rnating va `ALLOWED_HOSTS` / `CSRF_TRUSTED_ORIGINS` sozlamalarini to'g'ri konfiguratsiya qiling.

## Asosiy fayllar

- `config/settings.py` - loyiha konfiguratsiyasi
- `shop/models.py` - `Order` modeli
- `shop/views.py` - buyurtma yaratuvchi view
- `payment/views.py` - Click webhook ishlovi

