import os
import yaml
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load static files based on YAML configuration'

    def handle(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), '../../../config.yaml'), 'r') as file:
            config = yaml.safe_load(file)

        if config.get('staticfiles', {}).get('load', False):
            self.stdout.write(self.style.SUCCESS('Loading static files...'))
            call_command('collectstatic', interactive=False)
            self.stdout.write(self.style.SUCCESS('Static files loaded successfully.'))
        else:
            self.stdout.write(self.style.WARNING('Static files loading is disabled in the configuration.'))