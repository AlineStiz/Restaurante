from braces.views import JsonRequestResponseMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib import messages

from .models import Prato, Receita, Atividade
from .forms import ContatoForm
from .utils import GeraPDFMixin


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pratos'] = Prato.objects.all()# .order_by('?').all() -Usar caso queira embaralhar como os icones aparecer na tela
        context['atividades'] = Atividade.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form,*args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form,*args, **kwargs)


############# PDF ###############

class ReceitaPDFView(View, GeraPDFMixin):
    def get(self, request, *args, **kwargs):
        receitas = Receita.objects.all()
        dados = {
            'receitas': receitas,
        }
        pdf = GeraPDFMixin()
        return pdf.reder_to_pdf('PDF/receita.html',dados)


