import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()
import random
from first_app.models import Webpage,Topic,AccessRecord
from faker import Faker

fakegen = Faker()

sample_topics = ['topic_1','topic_2','topic_3','topic_4','topic_5']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(sample_topics))[0]

    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        print('populating ',entry)
        fake_url = fakegen.url()
        fake_names = fakegen.company()
        fake_date = fakegen.date()
        wbpg = Webpage.objects.get_or_create(topic = add_topic(), name = fake_names, url = fake_url)[0]
        access_record = AccessRecord.objects.get_or_create(name = wbpg, date = fake_date)[0]

if __name__ == "__main__":
    print("populating...")
    populate(30)
    print('populated')