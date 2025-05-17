from django.db import models


class Certifications(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    level_of_difficulty = models.CharField(
        choices=(
            ("0", "easy"),
            ("1", "je ne sais pas 1"),
            ("2", "je ne sais pas 2"),
            ("3", "je ne sais pas 3"),
            ("4", "je ne sais pas 4"),
        ),
        max_length=20,
        default="0",
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    duration_of_validity = models.CharField(null=True)
    institution = models.ForeignKey("Institutions", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="certification")
    exam_site = models.CharField
    prerequisites = models.ForeignKey("Prerequisites", models.CASCADE)
    link = models.URLField()
    discounts = models.CharField(null=True)
    languages = models.ForeignKey("Languages", on_delete=models.CASCADE)

    class Meta:
        db_table = "certifications"
        verbose_name_plural = "Certifications"


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
    
    def __str__(self, *args, **kwargs):
        return f"{self.name} - {self.code}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "category"
        verbose_name_plural = "Categories"
