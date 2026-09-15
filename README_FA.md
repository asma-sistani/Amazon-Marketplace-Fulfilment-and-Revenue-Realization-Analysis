<div dir="rtl" align = "justify">

# تحلیل تحقق درآمد و فرآیند انجام سفارش در بازارگاه آمازون <img src="Images/logo.png" alt="Logo" width="55" align="left"/>

### *خط لوله داده پایتون + داشبوردهای Tableau*

ریسک عملیاتی | تحقق درآمد | بهینه‌سازی چرخه سفارش تا وصول

![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?logo=tableau&logoColor=white)

---

![Dashboard – GIF](Images/Amazon_Analysis_Animation.gif)

---

🔹 خلاصه فارسی (برای مدیران و کارفرمایان):

این پروژه یک تحلیل عملیاتی از وضعیت فروش بازارگاه آمازون است. یافته‌های اصلی نشان می‌دهد که با وجود تقاضای قوی (بیش از ۸۳ میلیون INR)، تحقق درآمد به دلیل مشکلات زنجیره تأمین و عملیات (Fulfilment) دچار چالش جدی است. این گزارش با تفکیک داده‌ها به مدیران نشان می‌دهد که مشکل اصلی «کمبود تقاضا» نیست، بلکه «شکست در اجرای سفارش‌ها» است و ارائه می‌دهد که چگونه با اولویت‌بندی عملیاتی می‌توان بخش بزرگی از درآمدِ از دست رفته را بازیابی کرد.

**درآمد ثبت شده است، اما هنوز به نقدینگی تبدیل نشده است.**
این تحلیل فراتر از گزارش‌گیری ساده فروش است و مشخص می‌کند فرآیند تبدیل سفارش‌ها به درآمد واقعی دقیقاً در کدام مرحله دچار اختلال می‌شود. 

## 📸 نمای کلی داشبوردها

### ۱. نمای کلی سفارش‌ها و تحقق درآمدها

<div align = "center">

<img src="Images/dashboard1_order_revenue.png" width="900"/>

</div>

### ۲. کارایی کاتالوگ و تمرکز تجاری

<div align = "center">

<img src="Images/dashboard2_catalogue_performance.png" width="900"/>

</div>

### ۳. چرخه سفارش تا نقدینگی و کارایی تبلیغات

<div align = "center">

<img src="Images/dashboard3_cash_flow.png" width="900"/>

</div>

---

## مسئله تجاری و اهداف

درآمد بازارگاه قوی است، اما **تحقق درآمد (Revenue Realization) ضعیف است.**
اختلال در فرآیند تکمیل سفارش (لغوها، مرجوعی‌ها و تأخیر در ارسال) مانع از تبدیل بخش بزرگی از سفارش‌ها به نقدینگی وصول‌شده می‌شود.

**هدف تجاری:** افزایش جریان نقدی از طریق بهبود اجرای فرآیند Fulfilment و کاهش درآمد تحقق‌نیافته آمازون.

---

## پرسش‌های کلیدی کسب‌وکار
این تحلیل به دنبال پاسخ به سه پرسش عملیاتی است که برای عملکرد بازارگاه حیاتی هستند:

- چه مقدار از درآمد ثبت‌شده واقعاً به نقدینگی تبدیل شده است؟
- نقدینگی در کدام مرحله از چرخه «سفارش تا وصول» متوقف می‌شود؟
- کدام اقدامات عملیاتی می‌توانند بیشترین تأثیر مالی را در کوتاه‌مدت داشته باشند؟

----

## یافته‌های کلیدی (Key Insights):
<div dir="rtl" align="center">
  <table style="width: 100%; border-collapse: collapse; text-align: right; border: 1px solid #ddd;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 12px; border: 1px solid #ddd; width: 25%;">یافته تحلیلی</th>
        <th style="padding: 12px; border: 1px solid #ddd; width: 40%;">مفهوم مدیریتی</th>
        <th style="padding: 12px; border: 1px solid #ddd; width: 35%;">تأثیر تجاری</th>
      </tr>
    </thead>
    <tbody>
      <tr>
       <td style="padding: 10px; border: 1px solid #ddd;">حدود ۷۰٪ از کل درآمد، مربوط به درآمد تحقق‌نیافته در سفارش‌های Amazon Fulfilled است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">سفارش‌ها ثبت شده‌اند اما به دلیل تأخیر در ارسال، وجهی دریافت نشده است</td>
        <td style="padding: 10px; border: 1px solid #ddd;"><strong>بالاترین اولویت:</strong> اصلاح فرآیند ارسال برای آزادسازی نقدینگی بلوکه شده</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">تنها ۲۲.۴۱٪ سفارش‌ها تحویل شده‌اند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">نرخ تبدیل سفارش به نقدینگی با وجود تقاضای بالا، بسیار پایین است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">نشان‌دهنده ضعف عملیاتی است، نه کمبود تقاضا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">سفارش‌های انبارش آمازون تأخیر شدیدی دارند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">سرویس انبارش آمازون گلوگاه اصلی در تحقق درآمد است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">ریسک عملیاتی اصلی در بخش Fulfilment نهفته است</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">سفارش‌های انبارش فروشنده نرخ تحویل ۸۷٪ دارند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">روش جایگزین ارسال عملکرد بسیار بهتری دارد</td>
        <td style="padding: 10px; border: 1px solid #ddd;">فرصتی برای بازنگری در استراتژی ارسال یا استفاده از روش ترکیبی</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">۶۱٪ سفارش‌ها از کدهای تخفیف استفاده می‌کنند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">حجم فروش به شدت به تخفیف‌ها وابسته است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">رشد درآمد ناشی از تخفیف است، نه رشد ارگانیک تقاضا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">کدهای تخفیف AOV را تنها ۱.۱۷ برابر افزایش می‌دهند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">تخفیف‌ها باعث افزایش تعداد سفارش می‌شوند اما سبد خرید را بزرگتر نمی‌کنند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">تبلیغات برای ارزش‌آفرینی (Value Creation) کارآمد نیستند</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">۷۷.۳٪ درآمد متعلق به دو دسته Set و Kurta است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">درآمد به شدت بر روی دو دسته محصول متمرکز شده است</td>
        <td style="padding: 10px; border: 1px solid #ddd;"><strong>ریسک استراتژیک:</strong> وابستگی بالا؛ نیاز به تنوع‌بخشی به کاتالوگ</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">۱۲.۶٪ از کالاها (SKUs) کم‌گردش یا مرده هستند</td>
        <td style="padding: 10px; border: 1px solid #ddd;">تلاش عملیاتی صرف کالاهای با بازده پایین می‌شود</td>
        <td style="padding: 10px; border: 1px solid #ddd;">فرصتی برای بهینه‌سازی کاتالوگ و کاهش هزینه‌های نگهداری</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">تحقق درآمد ماهانه رو به کاهش است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">ورود نقدینگی به مرور زمان کندتر شده است</td>
        <td style="padding: 10px; border: 1px solid #ddd;">ریسک جریان نقدی در کوتاه‌مدت رو به افزایش است</td>
      </tr>
    </tbody>
  </table>
</div>

---

## خلاصه شاخص‌های کلیدی (Q2 2022)

- **کل درآمد:** ۸۳.۱۸ میلیون INR
- **کل سفارش‌ها:** ۱۲۰,۱۹۲
- **نرخ تحویل نهایی:** ۲۲.۴۱٪
- **نرخ لغو سفارش:** ۱۳.۸٪
- **نرخ مرجوعی:** ۱.۶۷٪
- **نرخ سفارش‌های در جریان:** ۶۲.۱۲٪
- **درآمد تحقق‌نیافته (آمازون):** ۵۷.۹ میلیون INR (حدود ۶۹.۶٪ از کل درآمد)

 اکثر سفارش‌ها در وضعیت «در جریان» (In-Progress) باقی مانده‌اند، که نشان‌دهنده دلیل اصلی عدم تبدیل بخش بزرگی از درآمد ثبت‌شده به نقدینگی وصول‌شده است.

---

## اقدامات استراتژیک پیشنهادی

<div dir="rtl" align = "center">
  <table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 12px; border: 1px solid #ddd; width: 45%; text-align: right;">اقدام</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 15%;">تأثیر</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 20%;">سطح تلاش</th>
        <th align="center" style="padding: 12px; border: 1px solid #ddd; width: 20%;">اولویت</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">رفع تأخیرهای ارسال آمازون برای بهبود تبدیل سفارش به نقدینگی</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">کاهش نرخ لغو (۱۳.۸٪) از طریق بهبود مدیریت سفارش‌ها</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">حذف ۱۲.۶٪ کالاهای کم‌گردش و مرده برای ساده‌سازی کاتالوگ</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">پایین</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">بازنگری در تخفیف‌ها و تمرکز بر کالاهای استراتژیک</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">استفاده از عملکرد ارسال فروشنده به عنوان بنچمارک عملیاتی</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">پایین</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd; text-align: right;">برخورد با عملکرد ارسال به عنوان محرک اصلی جریان نقدی</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">متوسط</td>
        <td align="center" style="padding: 10px; border: 1px solid #ddd;">بالا</td>
      </tr>
    </tbody>
  </table>
</div>

---

## تأثیر تجاری مورد انتظار (سناریو)

اگر فرآیند ارسال بهبود یابد و نرخ بازیابی لغوها به **۱۵٪** برسد، کل درآمد تحقق‌یافته می‌تواند در کوتاه‌مدت حدود **۲ تا ۳ درصد افزایش** یابد. این تأثیر عمدتاً ناشی از تسریع در چرخه تبدیل سفارش به نقدینگی و کاهش اتلاف درآمد در سفارش‌های لغو شده است.

---

## نکات برجسته تحلیلی

- **ریسک تحقق:** میزان تحقق درآمد ماه به ماه در حال کاهش است؛ در حالی که سفارش‌های ارسال شده توسط فروشنده به مراتب قابل‌اعتمادتر از ارسال‌های آمازون هستند.
- **اتلاف در کاتالوگ:** ۱۲.۶٪ از کاتالوگ محصولات عملاً «موجودی مرده» است. حذف این موارد بار عملیاتی را کاهش می‌دهد.
- **کارایی تبلیغات:** تخفیف‌ها حجم سفارش را بالا می‌برند اما در افزایش ارزش مشتری (AOV) شکست خورده‌اند. پیشنهاد می‌شود استراتژی قیمت‌گذاری از «تخفیف‌محور» به «ارزش‌محور» تغییر کند.

---

## ابزارها و مهارت‌های به کار رفته

<div dir="rtl" align="center">
  <table style="width: 100%; border-collapse: collapse; text-align: right; border: 1px solid #ddd;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 12px; border: 1px solid #ddd; width: 25%;">حوزه</th>
        <th style="padding: 12px; border: 1px solid #ddd; width: 75%;">نحوه پیاده‌سازی</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Python</td>
        <td style="padding: 10px; border: 1px solid #ddd;">کتابخانه‌های pandas, numpy, matplotlib, seaborn</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">Data Engineering</td>
        <td style="padding: 10px; border: 1px solid #ddd;">استانداردسازی، پاک‌سازی داده‌ها و نقشه‌برداری وضعیت سفارش‌ها</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">مدل‌سازی تحلیلی</td>
        <td style="padding: 10px; border: 1px solid #ddd;">چارچوب درآمد تحقق‌نیافته و دسته‌بندی سلامت SKU</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">BI & Viz</td>
        <td style="padding: 10px; border: 1px solid #ddd;">داشبوردهای Tableau برای تحلیل ریسک عملیاتی و تمرکز محصول</td>
      </tr>
      <tr>
        <td style="padding: 10px; border: 1px solid #ddd;">تأثیر تجاری</td>
        <td style="padding: 10px; border: 1px solid #ddd;">تبدیل داده‌های خام به استراتژی «محافظت از جریان نقدی»</td>
      </tr>
    </tbody>
  </table>
</div>

---

## ساختار پروژه

<div dir="ltr">

```text
Amazon_Marketplace_Analysis/
├─ Data/
│   └─ Amazon_Sales_Report.xlsx
├─ Docs/
│   └─ data_quality_report.md
├─ Executive_Summary/
│   ├─ Amazon_Marketplace_Insights_and_Recommendations.pdf
│   └─ Amazon_Marketplace_Insights_and_Recommendations_FA.pdf
├─ Images/
│   ├─ dashboard1_order_revenue.png
│   ├─ dashboard2_catalogue_performance.png
│   ├─ dashboard3_cash_flow.png
│   ├─ Amazon_Analysis_Animation.gif
│   └─ logo.png
├─ Results/
│   ├─ cleaned_data.csv
│   ├─ kpi_summary.csv
│   └─ sku_performance.csv
├─ Scripts/
│   ├─ data_quality_report.py
│   ├─ cleaning.py
│   └─ analysis.py
├─ Dashboards/
│   └─ Amazon_Marketplace_Fulfilment.twbx  # Tableau workbook
├─ README.md
└─ README_FA.md
```
</div>

---

## نحوه اجرا

### اجرای خط لوله داده (پایتون)
```bash
python Scripts/cleaning.py --input Data/Amazon_Sales_Report.xlsx --output Results/cleaned_data.csv
python Scripts/analysis.py --input Results/cleaned_data.csv --output_dir Results
```

#### خروجی‌های Pipeline:
- `Results/cleaned_data.csv`: داده‌های آماده برای تحلیل
- `Results/kpi_summary.csv`: جدول KPIهای استفاده شده در داشبورد
- `Results/sku_performance.csv`: رتبه‌بندی و وضعیت سلامت کالاها

### استفاده از داشبوردهای Tableau
داشبوردها به طور خودکار داده‌ها را از فایل‌های تولید شده توسط پایتون می‌خوانند.
۱. فایل `Dashboards/Amazon_Marketplace_Fulfilment.twbx` را باز کنید.
۲. اطمینان حاصل کنید که منابع داده به فایل‌های محلی در پوشه `Results` اشاره دارند.
۳. از تب‌های موجود برای جابه‌جایی بین تحلیل‌ها استفاده کنید.

این داشبوردها طوری طراحی شده‌اند که یک مدیر غیر فنی بتواند سریع به پرسش‌هایی مانند موارد زیر پاسخ دهد:

- ما واقعاً چقدر پول به‌دست می‌آوریم؟
- دقیقاً درآمد در کدام مرحله گیر می‌کند؟
- کدام SKUها باید گسترش داده شوند، بهبود پیدا کنند یا حذف شوند؟

---

## 🗃 مجموعه داده (Dataset)

- **منبع:** گزارش فروش عمومی آمازون از data.world
- **تعداد رکوردها:** حدود ۱۲۹ هزار ردیف
- **ستون‌های کلیدی:** کد سفارش، تاریخ، وضعیت سفارش، روش ارسال، SKU، دسته‌بندی، مبلغ، تعداد، کد تخفیف و نوع مشتری (B2B/Retail)

---

## 📁 خروجی‌های نهایی (Deliverables)

👈 **خلاصه مدیریتی ([PDF – English](Executive_Summary/Amazon_Marketplace_Fulfilment_and_Revenue_Realization_Analysis_Insights_and_Recommendations.pdf)):**
نمای کلی از تقاضا، عملکرد ارسال و توصیه‌های استراتژیک.

👈 **خلاصه مدیریتی ([PDF – Persian](Executive_Summary/Amazon_Marketplace_Fulfilment_and_Revenue_Realization_Analysis_Insights_and_Recommendations_FA.pdf)):**  
ترجمه فارسی خلاصه مدیریتی برای درک بهتر ذینفعان محلی.

👈 **نمایش تعاملی داشبورد ([Dashboard Walkthrough – GIF](Images/Amazon_Analysis_Animation.gif)):**
مروری تعاملی بر چرخه سفارش تا تحقق درآمد همراه با نمایش تأثیر لحظه‌ای تغییر پارامترها بر شاخص‌های مالی.

---

## 👤 درباره نویسنده

**اسما سیستانی – تحلیلگر داده**  
تبدیل پیچیدگی‌های عملیاتی به بینش‌های شفاف و تجاری.

💻 **GitHub:** [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/asma-sistani)

🔗 **LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asma-sistani)

🌐 **Portfolio:** [![Portfolio](https://img.shields.io/badge/Portfolio-2563EB?style=for-the-badge&logo=google-chrome&logoColor=white)](https://asmatheanalyst.github.io/portfolio.html)

---

**این پروژه نشان می‌دهد چگونه تحلیل داده می‌تواند از «گزارش آنچه اتفاق افتاده» فراتر رفته و به «تصمیم‌سازی درباره آنچه باید انجام شود» تبدیل شود؛ با تمرکز بر تحقق درآمد به جای صرفاً حجم فروش.**

---


</div>
