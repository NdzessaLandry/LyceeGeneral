from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
admin.site.register(Classe)
admin.site.register(ClassePeriodeCours)
admin.site.register(Cours)
admin.site.register(Directeur)
admin.site.register(Enseignant)
admin.site.register(EnseignantMatiere)
admin.site.register(Etablissement)
admin.site.register(Grade)
admin.site.register(Jour)
admin.site.register(Matiere)
admin.site.register(Niveau)
admin.site.register(Periode)
admin.site.register(Salle)
admin.site.register(SalleEnseignant)
admin.site.register(Senceur)
admin.site.register(Typecours)
admin.site.register(ClasseCours)
#admin.site.register(SallePeriode)
admin.site.register(ClasseEnseignantCours)


admin.site.site_title=_("Gestion des emplois de temps pour le Lycee Technique de Maroua")
admin.site.site_header=_("Gestion des emplois de temps pour le Lycee Technique de Maroua")
admin.site.index_title=_("Gestion des emplois de temps pour le Lycee Technique de Maroua")
# Register your models here.
