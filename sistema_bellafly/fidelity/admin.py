from django.contrib import admin
from .models import CheckboxSell
from django.forms import ModelForm
from django.core.mail import send_mail

class CheckboxSellForm(ModelForm):
    class Meta:
        model = CheckboxSell
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna os campos de data readonly
        for i in range(1, 11):
            data_field = f'data_checkbox_{i}'
            if data_field in self.fields:
                self.fields[data_field].widget.attrs['readonly'] = True

@admin.register(CheckboxSell)
class CheckboxTaskAdmin(admin.ModelAdmin):
    form = CheckboxSellForm
    
    list_display = ('nome', 'created_at', 'checkboxes_concluidos', 'progresso')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('nome',)
    
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('nome',)
        }),
        ('Vendas 1-10', {
            'fields': (
                ('checkbox_1', 'data_checkbox_1'),
                ('checkbox_2', 'data_checkbox_2'),
                ('checkbox_3', 'data_checkbox_3'),
                ('checkbox_4', 'data_checkbox_4'),
                ('checkbox_5', 'data_checkbox_5'),
                ('checkbox_6', 'data_checkbox_6'),
                ('checkbox_7', 'data_checkbox_7'),
                ('checkbox_8', 'data_checkbox_8'),
                ('checkbox_9', 'data_checkbox_9'),
                ('checkbox_10', 'data_checkbox_10'),
            )
        }),
    )
    
    readonly_fields = tuple(f'data_checkbox_{i}' for i in range(1, 11))
    
    def checkboxes_concluidos(self, obj):
        """Conta quantos checkboxes foram marcados"""
        count = 0
        for i in range(1, 11):
            if getattr(obj, f'checkbox_{i}'):
                count += 1
        return f"{count}/10"
    checkboxes_concluidos.short_description = "Concluídos"
    
    def progresso(self, obj):
        """Mostra uma barra de progresso visual"""
        count = 0
        for i in range(1, 11):
            if getattr(obj, f'checkbox_{i}'):
                count += 1
        
        porcentagem = (count / 10) * 100
        
        if porcentagem == 100:
            return f"🟢 {porcentagem:.0f}%"
        elif porcentagem >= 50:
            return f"🟡 {porcentagem:.0f}%"
        else:
            return f"🔴 {porcentagem:.0f}%"
    
    progresso.short_description = "Progresso"
    
    def save_model(self, request, obj, form, change):
        """Override para capturar mudanças no admin"""
        if change:
            # Pega o objeto original para comparar
            original = CheckboxSell.objects.get(pk=obj.pk)
            
            # Verifica quais checkboxes mudaram
            for i in range(1, 11):
                checkbox_field = f'checkbox_{i}'
                original_value = getattr(original, checkbox_field)
                new_value = getattr(obj, checkbox_field)
                
                # if original_value != new_value:
                #     if new_value:
                #         send_mail(
                #             'Tarefa Marcada',
                #             f"🎯 ADMIN: Usuário {request.user.username} marcou a Tarefa {i}",
                #             'danilo0123499@gmail.com',  # De
                #             ['gamerotaku83@gmail.com'],  # Para
                #             fail_silently=False,
                #         )

                #     else:
                #         send_mail(
                #             'Tarefa Desmarcada',
                #             f"⚠️  ADMIN: Usuário {request.user.username} desmarcou a Tarefa {i}",
                #             'danilo0123499@gmail.com',  # De
                #             ['gamerotaku83@gmail.com'],  # Para
                #             fail_silently=False,
                #         )
        super().save_model(request, obj, form, change)
