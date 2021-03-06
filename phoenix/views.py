from django.template import loader
from django.http import HttpResponse, JsonResponse
import json
import difflib
from .models import Signal, Trigger, Action

operations = {
    'lt': '<',
    'lte': '<=',
    'eq': '=',
    'gt': '>',
    'gte': '=>'
}

def index(request):
    signals_list = Signal.objects.all()

    triggers_list = Trigger.objects.all()
    all_triggers = []

    for trigger in triggers_list:
        status = 'deactivated'
        color = '#f82831'
        if trigger.status is True:
            status = 'activated'
            color = '#4bec13'
        all_triggers.append({'id': trigger.id, 'name': trigger.name, 'threshold': '{}'.format(trigger.threshold_level), 'status': status, 'color': color})

    template = loader.get_template('phoenix/index.html')
    context = {
        'signals_list': signals_list,
        'triggers_list': all_triggers,
    }
    return HttpResponse(template.render(context, request))

def run_rule():
    pass

def check_duplicate_email(request):
    new_email = request.GET.get('email', '').lower()
    with open('./phoenix/data/email_cluster.json') as data_file:
        cluster_data = json.load(data_file)
    clusters = cluster_data['clusters']
    high_risk_emails = []
    for cluster in clusters:
        if cluster['size'] > 4:
            high_risk_emails.append(cluster['value'])
    for email in high_risk_emails:
        seq = difflib.SequenceMatcher(a=new_email, b=email.lower())
        if seq.ratio() > 0.8:
            print(email, seq.ratio())
            return JsonResponse({'email': email, 'score': seq.ratio(), 'match': True})
    return JsonResponse({'match': False})
