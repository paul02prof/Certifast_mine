from django.db import models


class Certifications(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    level_of_difficulty = models.CharField(
        max_length=20,
        default="0",
        choices=(
            ("0", "easy"),
            ("1", "medium"),
            ("2", "hard"),
            ("3", "very hard"),
            ("4", "impossible"),
        ),
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    duration_of_validity = models.CharField(null=True)
    institution = models.ForeignKey("Institutions", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="certification")
    exam_site = models.CharField
    prerequisites = models.ForeignKey("Prerequisites", models.CASCADE, null=True)
    link = models.URLField()
    discounts = models.CharField(null=True, max_length=50)
    languages = models.ForeignKey("Languages", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "certifications"
        verbose_name_plural = "Certifications"
        unique_together = ("name", "institution")


class Institutions(models.Model):
    name = models.CharField(max_length=50)
    accepted_zones = models.CharField(max_length=250)
    about = models.TextField(null=True)

    class Meta:
        db_table = "institutions"
        verbose_name_plural = "Institutions"


class Prerequisites(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = "prerequisites"
        verbose_name_plural = "Prerequisites"


class Languages(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "languages"
        verbose_name_plural = "Languages"
        unique_together = ("code", "name")

    def __str__(self, *args, **kwargs):
        return f"{self.name} - {self.code}"


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"
