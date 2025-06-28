import json
from django.core.management.base import BaseCommand
from certification.models import Course, Category, Topic, Institutions, Prerequisites, Languages


class Command(BaseCommand):
    help = 'Importe des cours depuis un fichier JSON'

    def handle(self, *args, **kwargs):
        try:
            with open('data/courses.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Fichier 'data/courses.json' non trouvé."))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Erreur lors de la lecture du fichier JSON."))
            return

        for item in data:
            name = item['name'].strip()

            # Récupérer l'institution
            institution_name = item.get('institution')
            institution = None
            if institution_name:
                try:
                    institution = Institutions.objects.get(name=institution_name)
                except Institutions.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f"Institution '{institution_name}' non trouvée pour le cours '{name}'. Ignoré."))
                    continue

            # Créer ou mettre à jour le cours
            course, created = Course.objects.update_or_create(
                name=name,
                defaults={
                    'description': item.get('description'),
                    'level_of_difficulty': item.get('level_of_difficulty', '0'),
                    'price': item.get('price', 0),
                    'duration_of_validity': item.get('duration_of_validity'),
                    'link': item.get('link'),
                    'discounts': item.get('discounts'),
                    'institution': institution,
                    'duration': item.get('duration'),
                }
            )

            # Gestion des relations ManyToMany
            # Catégories
            for cat in item.get('category', []):
                try:
                    category = Category.objects.get(name=cat.strip())
                    course.category.add(category)
                except Category.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Catégorie '{cat}' non trouvée."))

            # Topics
            for top in item.get('topic', []):
                try:
                    topic = Topic.objects.get(name=top.strip())
                    course.topic.add(topic)
                except Topic.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Topic '{top}' non trouvé."))

            # Prérequis
            for prereq in item.get('prerequisites', []):
                try:
                    prerequisite = Prerequisites.objects.get(title=prereq.strip())
                    course.prerequisites.add(prerequisite)
                except Prerequisites.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Prérequis '{prereq}' non trouvé."))

            # Langues
            for lang in item.get('languages', []):
                try:
                    language = Languages.objects.get(name=lang.strip())
                    course.languages.add(language)
                except Languages.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Langue '{lang}' non trouvée."))

            status = "créé" if created else "mis à jour"
            self.stdout.write(self.style.SUCCESS(f"Cours '{name}' {status}."))

        self.stdout.write(self.style.SUCCESS("Import des cours terminé."))