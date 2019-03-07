from django.contrib import admin

from pet.models import Breed, Pet, Picture


class PetPictureInline(admin.StackedInline):
    model = Pet.pictures.through
    raw_id_fields = ('picture',)
    extra = 0


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    list_filter = ('kind', 'date_added')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', 'kind')}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'situation', 'sex', 'rescued', 'kind', 'breed', 'lost_date', 'found_date'
    )
    exclude = ('pictures',)
    list_filter = (
        'situation',
        'rescued',
        'sex',
        'kind',
        'rescued_date',
        'lost_date',
        'found_date',
        'breed',
    )
    search_fields = ('name', 'description')
    raw_id_fields = ('picture', 'breed')
    prepopulated_fields = {'slug': ('name', 'kind', 'situation')}
    inlines = (PetPictureInline,)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date_added')
    list_filter = ('date_added', 'date_changed')
